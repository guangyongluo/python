import json

obj = {
    "name": "张三",
    "age": 20,
    "gender": "male",
    "hobbies": ["reading", "swimming"]
}

with open("resource/session.json", "w") as f:
    json.dump(obj, f, ensure_ascii=False, indent=4)

with open("resource/session.json") as f:
    obj = json.load(f)
    print(obj)