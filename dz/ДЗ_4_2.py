

with open("file_1.txt", encoding="utf-8") as f:
    my_list = f.read().splitlines()
    for x in my_list:
        my_list_1 = x.split()
        num_1 = [int(p) for p in my_list_1]
        fizz = int(num_1[0])
        buzz = int(num_1[1])
        num = int(num_1[2])
        for i in range(1, num + 1):
            print((i % fizz == 0 and i % buzz == 0) and "FB" or i % buzz == 0 and "B" or i % fizz == 0 and "F" or i,
                  end="")
        print("")

f.close()














