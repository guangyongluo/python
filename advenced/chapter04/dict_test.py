from collections.abc import Mapping, MutableMapping
#dict属于mapping类型

a = {}
print (isinstance(a, MutableMapping))

a = {"bobby1":{"company":"imooc"},
     "bobby2": {"company": "imooc2"}
     }
#clear
# a.clear()
# pass

#copy, 返回浅拷贝
new_dict = a.copy()
new_dict["bobby1"]["company"] = "imooc3"

#formkeys
new_list = ["bobby1", "bobby2"]

new_dict = dict.fromkeys(new_list, {"company":"imooc"})

new_dict.update((("bobby","imooc"),))

#不建议继承list和dict
class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict = Mydict(one=1)
my_dict["one"] = 1
print (my_dict)

from collections import UserDict

class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict = Mydict(one=1)
# my_dict["one"] = 1
print (my_dict)

from collections import defaultdict

my_dict = defaultdict(dict)
my_value = my_dict["bobby"]
pass