
# is 的用法

a = [1, 2, 3,4]
b = a
print(id(a), id(b))

print(a is b)

class Person:
    pass

p = Person()
if type(p) is Person:
    print("1")

if isinstance(p, Person):
    print("1")