from volcenginesdkarkruntime import Ark

def chat_dance():
    client = Ark(api_key='your key')
    response = client.chat.completions.create(
        model="your model",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "这是什么？"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7d2e7e810f054952aa8854fc99577260~tplv-goo7wpa0wc-image.image"
                        }
                    }
                ],
            }
        ]
    )

    print(response.choices[0].message.content)

if __name__ == '__main__':
    chat_dance()