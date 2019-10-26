
# property 将方法变成属性调用

from datetime import date, datetime

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0
    def get_age(self):
        return datetime.now().year - self.birthday.year

    # get
    @property
    def age(self):
        if self._age > 0:
            return self._age
        return datetime.now().year - self.birthday.year

    # set
    @age.setter
    def age(self, value):
        self._age = value

if __name__ == "__main__":
    user = User("bob", date(year=1992, month=3, day=14))

    print(user.get_age())
    print(user.age)


    user.age = 13
    print(user.age)
    print(user._age)



