import json
import os
from openai import OpenAI
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="ai智能伴侣",
    page_icon="🤖",
    # 布局
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': "https://streamlit.io/"
    }

)


def save_session():
    if not st.session_state.messages:
        return

    if st.session_state.current_session is not None:
        # 构建新的会话对象
        session_info = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "messages": st.session_state.messages,
            "current_session": st.session_state.current_session
        }

        # 创建保存会话的目录
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        # 保存当前会话信息
        with open(f"sessions/{st.session_state.current_session}.json", "w") as f:
            json.dump(session_info, f, ensure_ascii=False, indent=4)


def generate_session_id():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def load_sessions():
    session_list = []
    if os.path.exists("sessions"):
        for filename in os.listdir("sessions"):
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    return session_list


def load_session(session_id):
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            with open(f"sessions/{session_id}.json", "r", encoding="utf-8") as f:
                session_info = json.load(f)
                st.session_state.nick_name = session_info["nick_name"]
                st.session_state.nature = session_info["nature"]
                st.session_state.messages = session_info["messages"]
                st.session_state.current_session = session_info["current_session"]
    except Exception:
        st.error("会话加载失败")

def delete_session(session_id):
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            os.remove(f"sessions/{session_id}.json")
            if st.session_state.current_session == session_id:
                st.session_state.current_session = generate_session_id()
                st.session_state.messages = []
    except Exception:
        st.error("会话删除失败")


# 大标题
st.title("AI智能伴侣")

api_key = os.getenv('ARK_API_KEY')

# 创建与AI大模型交互的客户端对象（api_key是你在云上的大模型访问Token）
client = OpenAI(
    base_url='https://ark.cn-beijing.volces.com/api/v3',
    api_key=api_key
)

# 系统提示词
system_prompt = "你叫%s, %s"

if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"

if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的湖北女孩"

# 初始化聊天消息
if "messages" not in st.session_state:
    st.session_state.messages = []
# 会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_id()

# 会话名称
st.text(f"会话名称：{st.session_state.current_session}")

# 展示聊天消息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

with st.sidebar:
    # 会话信息
    st.subheader("AI控制面板")

    if st.button("新建会话", width="stretch", icon="✏️"):
        # 1. 保存当前会话信息
        save_session()
        # 2. 创建新的会话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_id()
            st.rerun()

    st.text("会话历史")
    session_list = load_sessions()
    session_list.sort(reverse=True)
    for session in session_list:
        session_name, opt = st.columns([4, 1])
        with session_name:
            if st.button(session, key=f"load_{session}", width="stretch", icon="📄",
                         type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with opt:
            if st.button("", key=f"session_{session}", width="stretch", icon="🗑️"):
                delete_session(session)
                st.rerun()

    # 左边栏标题
    st.subheader("AI伴侣信息")
    # 输入AI伴侣的昵称
    nick_name = st.text_input("AI伴侣昵称", placeholder="请输入AI伴侣昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    # 输入AI伴侣的性格
    nature = st.text_area("AI伴侣性格", placeholder="请输入AI伴侣的性格", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

# 大模型输入框
prompt = st.chat_input("请输入你想对AI智能伴侣说的话")
if prompt:
    st.chat_message("user").write(prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    completion = client.chat.completions.create(
        # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
        model="deepseek-v3-2-251201",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True
    )

    # 输出大模型返回的结果（流式输出）
    response_message = st.empty()  # 创建一个空的组件，用户展示大模型返回的结果

    full_response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 输出大模型返回的结果（非流式输出）
    # st.chat_message("assistant").write(completion.choices[0].message.content)

    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 保存会话信息
    save_session()
