
# 只要函数里面有yield 关键字 ，就是生成器


def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

def fib2(index):
    re_list = []
    n,a,b = 0,0,1
    while n<index:
        re_list.append(b)
        a,b = b, a+b
        n += 1
    return re_list

def gen_fib(index):
    n,a,b = 0,0,1
    while n<index:
        yield b
        a,b = b, a+b
        n += 1

for data in gen_fib(10):
    print (data)
    

def gen_func():
    yield 1
    yield 2
    yield 3

if __name__ == "__main__":

    gen = gen_func()
    print(iter(gen).__next__())

    for v in gen:
        print(v)