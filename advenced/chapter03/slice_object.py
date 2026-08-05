from numbers import Integral

class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staff):
        self.group_name = group_name
        self.company_name = company_name
        self.staff = staff

    def __getitem__(self,item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self.group_name, self.company_name, self.staff[item])
        elif isinstance(item, Integral):
            return cls(self.group_name, self.company_name, [self.staff[item]])


    def __reversed__(self):
        self.staff.reverse()

    def __len__(self):
        return len(self.staff)

    def __iter__(self):
        return iter(self.staff)

    def __contains__(self,item):
        return item in self.staff

group = Group('group_name', 'company_name', ['bob', 'jane', 'leo'])

sub_group = group[:2]
print (sub_group)

sub_group = group[2]
print (sub_group)

reversed(group)
print (group)