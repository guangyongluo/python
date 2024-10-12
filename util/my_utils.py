import json

data = [{"name": "zhangsan", "age": 30}, {"name": "lisi", "age": 25}, {"name": "wangwu", "age": 20}]

json_str = json.dumps(data)

string = '[{"name": "zhangsan", "age": 30}, {"name": "lisi", "age": 25}, {"name": "wangwu", "age": 20}]'

person_list = json.loads(string)

if __name__ == '__main__':
    print(type(json_str), json_str)

    print(type(person_list), person_list)
