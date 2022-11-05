list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# list_1 = [len([i for i in list_1 if i > 0]), sum([i for i in list_1 if i < 0]) if len(list_1) != 0 else []]
# print(list_1)
# pos = sum(1 for x in list_1 if x > 0)
# neg = sum(x for x in list_1 if x < 0)
# print(pos)
# print(neg)

list_2 =[sum(n > 0 for n in list_1), sum(n for n in list_1 if n < 0)] if list_1 else []

print(list_2)



