with open("file_3.txt", encoding="utf-8", mode="r+") as f:
    my_list = f.readlines()
    f.seek(0)
    for x in my_list:
        # my_list_1 = x.rstrip()
        try:
            my_list = eval(x)
        except ZeroDivisionError as e:
            print(e)
        # print(my_list)

        print(my_list if x != ZeroDivisionError else e, file=f)

f.close()
