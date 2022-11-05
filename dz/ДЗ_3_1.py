str_1 = input("Enter first string: ")
str_2 = input("Enter second string: ")
str_3 = input("Enter third string: ")

print(str_1[len(str_1)//2] if len(str_1) % 2 else str_1[(len(str_1)-1)//2])
if len(str_2) % 2:
    print(str_2[len(str_2)//2])
else:
    print(str_2[(len(str_2)-1)//2])
print(str_3[len(str_3)//2] if len(str_3) % 2 else str_3[(len(str_3)-1)//2])

