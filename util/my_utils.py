import json

data = [{"name": "zhangsan", "age": 30}, {"name": "lisi", "age": 25}, {"name": "wangwu", "age": 20}]

json_str = json.dumps(data)

string = '[{"name": "zhangsan", "age": 30}, {"name": "lisi", "age": 25}, {"name": "wangwu", "age": 20}]'

person_list = json.loads(string)

def str_reverse(s):
    """
    reverse input param string
    :param s: will be reversed parameter
    :return: reversed string
    """
    return s[::-1]

def sub_str(s, x, y):
    """
    according to input index to split the string to a sub one.
    :param s: input string
    :param x: begin index
    :param y: end index
    :return: splice of the input string
    """
    return s[x:y]

if __name__ == '__main__':

    print(type(json_str), json_str)

    print(type(person_list), person_list)

    print(str_reverse('程序员罗小黑'))

    print(sub_str("程序员罗小黑", 1, 3))
