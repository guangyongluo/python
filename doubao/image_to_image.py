import base64
from volcengine.visual.VisualService import VisualService

def image_to_base64() -> []:
    with open("luoxiaohei1.jpg", "rb") as f:
        encode_string = base64.b64encode(f.read()).decode("utf-8")
        return encode_string

def base64_to_image(file):

    with open(file, "r") as f:
        base64_string = f.read()

    with open("luoxiaohei1.jpg", "wb") as f:
        f.write(base64.b64decode(base64_string))

if __name__ == '__main__':
    visual_service = VisualService()

    # call below method if you don't set ak and sk in $HOME/.volc/config
    visual_service.set_ak('your access key')
    visual_service.set_sk('your secret key')

    form = {
        "req_key": "img2img_clay_style",
        "sub_req_key": "img2img_clay_style_bubble",
        "binary_data_base64": [image_to_base64()],
        "return_url": True,
    }

    resp = visual_service.img2img_create_rev_animated(form)
    print(resp)

    # base64_to_image("avatar_base64.txt")



