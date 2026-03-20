import os
from openai import OpenAI

# 从环境变量中获取您的API KEY
api_key = os.getenv('ARK_API_KEY')

client = OpenAI(
    base_url='https://ark.cn-beijing.volces.com/api/v3',
    api_key=api_key
)

completion = client.chat.completions.create(
    # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    model = "deepseek-v3-2-251201",
    messages = [
        {"role": "system", "content": "你是人工智能助手"},
        {"role": "user", "content": "你好"}
    ],
    stream = False
)

print(completion.choices[0].message.content)