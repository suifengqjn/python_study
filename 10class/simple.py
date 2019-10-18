"""一个简单的类实例"""
class MyClass:

#属性
    i = 12345
#方法
    def f(self):
        return 'hello world'

#类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
def __init__(self):
    print("MyClass 初始化")
    self.data = []


# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有


# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


# self代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()

#
# 类的方法
# 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。我的体重%d kg" % (self.name, self.age, self.__weight))


# 实例化类
p = people('runoob', 10, 30)
p.speak()


