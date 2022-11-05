with open("file_3.txt", encoding="utf-8", mode="r+") as file:
    my_list = file.read().splitlines()
    # print(my_list)
    for x in my_list:
        my_list_1 = x.rstrip()
        try:
            my_list = eval(x)
        except ZeroDivisionError:
            result = "Error"

        file.write(f"\t = {result if eval(x) == ZeroDivisionError else eval(x) }\n")

file.close()
