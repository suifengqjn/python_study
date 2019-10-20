

#自省是通过一定的机制查询到对象或者类的内部结构

class Person:
    '''
    人
    '''
    name = "person"

class Student(Person):
    def __init__(self,school):
        self.school = school

    def say(self):
        print("my school is %s", self.school)


if __name__ == "__main__":

    # 通过__dict__cha'xu'hchaxuh
    user=Student("qinghua")

    print(user.__dict__) #没有name name 属于person 类
    #动态添加属性
    user.__dict__["school_addr"] = "beida"
    print(user.school_addr)

    #动态修改
    user.__dict__["school"] = "123"
    print(user.school)
    print(Person.__dict__)


    # dir 列出对象的所有属性
    print("dir---",user.__dir__())
    print(dir(user))
