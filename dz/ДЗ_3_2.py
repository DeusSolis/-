str_1 = "qwerty"
if 5 < len(str_1) < 15:
    print(str_1[len(str_1)//2::-1] + str_1[:len(str_1)//2:-1][:3] + str_1[:len(str_1)//2:-1][3:].upper())
else:
    print("Error")





