import json

lista = ["beijing","hangzhou", 123, 12.5]

# list to json
data = json.dumps(lista)
print(data, type(data))


# json to list
listb = json.loads(data)
print(listb, type(listb))




