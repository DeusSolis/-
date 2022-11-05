str_1 = "ASDF"
b = len(str_1) // 2
str_2 = str_1[::-1]
str_3 = str_2[b:] + str_2[:b]
if 5 < len(str_1) < 15:
    print(str_3[:-3] + str_3[-3:].upper())
else:
    print("Error")
