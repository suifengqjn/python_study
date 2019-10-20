
import numbers
# 自定义支持切片操作的对象
class Group:

    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return Group(self.group_name, self.company_name, self.staffs[item])
        elif isinstance(item,numbers.Integral):
            return Group(self.group_name, self.company_name, [self.staffs[item]])
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __contains__(self, item):
        pass


if __name__ == "__main__":
    staffs = ["a", "b", "c"]
    group = Group("ic", "user", staffs)
    print(group)


sub_g = group[:2]
print(sub_g)

sub_g2 = group[0]
print(sub_g)

