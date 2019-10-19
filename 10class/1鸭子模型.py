
class Cat(object):
    def say(self):
        print("i am cat")

class Dog(object):
    def say(self):
        print("i am dog")

class Duck(object):
    def say(self):
        print("i am duck")

# 多态实现
animal = Cat
animal().say()


list = [Cat, Dog, Duck]
for a in list :
    a().say()