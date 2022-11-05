fizz = int(input("fizz: "))
buzz = int(input("buzz: "))
num = int(input("num: "))

print((i % fizz == 0 and i % buzz == 0) and "FB" or i % buzz==0 and "B" or i % fizz==0 and "F" or i for i in range(1, num + 1))