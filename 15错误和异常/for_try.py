

res = []

for i in range(1, 5):

    try:
        a = i+10
        res.append(a)
    except NameError as e:
        res.append(i)


print(res)


