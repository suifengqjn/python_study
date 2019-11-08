def func_a(func, func_a_arg_a,  **kwargs):
    print(func_a_arg_a)
    func(**kwargs)

def func_b(arg_b):
    print(arg_b)

def func_c():
    print('Hello World')



def check(v):

    if v * 6 == 36:
        return True
    else:
        return False

def get_data(f, func):
    for f in range(f, f+10):
        if func(f) == True:
            return f

    return -1


if __name__ == '__main__':
    func_a(func=func_b,func_a_arg_a='temp', arg_b='Hello Python')
    func_a(func_a_arg_a='temp', func=func_c)




    v = get_data(f=2, func=check)

    print("----", v)


    s = "pp--"

    s2 = s[4:]
    print("s2 value",s2, len(s2))
    print(s2 == None)