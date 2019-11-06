

def get_value():

    arr = [1, 2, 3]
    try:
        print("first try")
        v = arr[0]
        return v
    except Exception as e:
        print(e)
        pass

    try:
        print("second try")
        v = arr[1]
        return v
    except ValueError as e:
        print(e)
        pass

def get_value2():
    arr = [1, 2, 3]
    try:
        v = arr[0]
        return v
    except Exception as e:
        print(e)
        pass
    finally:
        return "fff"

if __name__ == "__main__":

    v = get_value()
    print("v",v)

    v2 = get_value2()
    print("v2",v2)