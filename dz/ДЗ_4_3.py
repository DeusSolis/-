list_1 = [32,43,1,3,4,5,34,5,1,7,10,34,17,11]

for i in range(len(list_1)):
    if i % 5 == 0:
        list_1[i: i + 5] = sorted(list_1[i:i + 5])
    if i % 5 == 0 and i % 10:
        list_1[i: i + 5] = sorted(list_1[i:i + 5], reverse=True)

print(list_1)