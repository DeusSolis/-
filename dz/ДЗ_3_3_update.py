str_1 = 'ABCDEF'
str_2 = str_1[-3:].lower()
center_str = len(str_1[:-3]) // 2
str_3 = str_1[:center_str] + str_2 + str_1[center_str:-3]
if 4 < len(str_1) < 10:
    print(str_3)
else:
    print("Error")

