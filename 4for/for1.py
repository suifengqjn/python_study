import time
index = 1
while True:

    if index == 1:
        print("1")
    elif index == 2:
        print("2")
    elif index == 3:
        print("3")
    else:
        print(index)
    index += 1
    time.sleep(2)
    if index >3:
        index = 1



