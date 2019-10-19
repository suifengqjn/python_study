
class Date:
    name = "Date class" #类变量

    # 构造函数
    def __init__(self, year, month, day):
        self.year = year #实例变量
        self.month = month
        self.day = day

    # 实例方法
    def tomorrow(self):
        self.day += 1

    #静态方法
    @staticmethod
    def parse_from_str(date_str):
        year, mon, day = tuple(date_str.split("-"))
        return Date(year, mon, day)

    #类方法
    @classmethod
    def parse2_from_str(cls, date_str):
        year, mon, day = tuple(date_str.split("-"))
        return cls(year, mon, day)

    @classmethod
    def valid_str(cls, date_str):
        year, mon, day = tuple(date_str.split("-"))
        if int(year) > 0 and (int(mon) > 0 and int(mon) <= 12) and int(day) < 31:
            return True
        else:
            return False

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month,day=self.day)




class User:

    def __init__(self, birthday):
        self.__birthday = birthday  # 私有属性

    def get_age(self):
        return 2019 - self.__birthday

    def __get_bir(self):# 私有方法
        print(self.__birthday)






if __name__ == "__main__":

    d = Date("2019",10, 23)
    print(d)
    d.tomorrow()
    print(d)

    d2 = Date.parse_from_str("2018-02-03")
    print(d2)

    d3 = Date.parse2_from_str("2017-02-03")
    print(d3)

    print(Date.valid_str("2017-02-33"))



    user = User(2001)
    print("年龄", user.get_age())

