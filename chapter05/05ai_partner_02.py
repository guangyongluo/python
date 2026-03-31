import os
from openai import OpenAI
import streamlit as st

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

# 大标题
st.title("AI智能伴侣")


api_key = os.getenv('ARK_API_KEY')

# 创建与AI大模型交互的客户端对象（api_key是你在云上的大模型访问Token）
client = OpenAI(
    base_url='https://ark.cn-beijing.volces.com/api/v3',
    api_key=api_key
)

# 系统提示词
system_prompt = "你是人工智能助手"

# 初始化聊天消息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 展示聊天消息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

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
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        stream=True
    )

    # 输出大模型返回的结果（流式输出）
    response_message = st.empty() # 创建一个空的组件，用户展示大模型返回的结果

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

