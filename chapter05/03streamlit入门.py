import streamlit as st

st.set_page_config(
    page_title="Streamlit入门",
    page_icon="resource/favicon.svg",
    # 布局
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': "https://streamlit.io/"
    }

)

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落
st.write("布偶猫，又称“布拉多尔猫”，是一种体型较大、性格温顺的宠物猫品种，因其在被抱时身体会像软绵绵的布偶一样放松而得名")
st.write("外貌特征：它们拥有迷人的蓝色大眼睛，毛发丰厚柔滑，属于中长毛猫。体色多为重点色，常见的有海豹色、蓝色、双色等，最显著的特点是四肢、尾部、耳朵和面部颜色较深，身体颜色较浅。")
st.write("性格特点：布偶猫以温顺、安静著称，非常亲近人类。它们忍耐力强，对疼痛的感知较弱，喜欢与人互动，甚至会像小狗一样跟随主人，因此非常适合有孩子的家庭或初次养猫的人。")
st.write("饲养注意：虽然性格讨喜，但布偶猫需要主人投入较多时间陪伴，且长毛需定期梳理以防打结。它们体质相对娇弱，需注意肠胃健康和定期体检。")
st.write("总的来说，布偶猫是集美貌与温柔于一身的理想伴侣动物。")

# 图片
st.image("resource/布偶猫.webp")
