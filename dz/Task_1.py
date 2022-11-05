with open("input.txt", encoding="utf-8", mode="r") as f:
    ww = f.read().split("\n")
    result_Alibaba = 0
    result_Jafar = 0
    result_Jago = 0
    for i in ww:
        temp = i.split()
        for x in temp:
            if x.isdigit():
                if temp[0] == "Alibaba":
                    result_Alibaba += int(x)
                elif temp[0] == "Jafar":
                    result_Jafar += int(x)
                elif temp[0] == "Jago":
                    result_Jago += int(x)
    if result_Jafar < result_Alibaba > result_Jago:
        print("Winner is Alibaba", result_Alibaba)
    elif result_Alibaba < result_Jafar > result_Jago:
        print("Winner is Jafar", result_Jafar)
    else:
        print("Winner is Jago", result_Jago)

f.close()
