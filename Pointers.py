# In case of integers:

num1 = 11

num2 = num1

print(id(num1))
print(id(num2))

num2 = 50

print(f"Address of num1: {id(num1)}")
print(f"Address of num2: {id(num2)}")




# In case of dictionaries:

dict1 = {
    "value" : 10
}

dict1["value"] = 20

dict2 = dict1



print(f"dict1 is pointing at address: {id(dict1)}")
print(f"dict2 is pointing at address: {id(dict2)}")