def del_space(string_1):
    q = {"space": 0}
    for i in string_1:
        if i.isspace():
            q["space"] +=1
    string_1 = string_1.replace(" ","",q["space"] -1)
    return string_1




print(del_space('Simple, remove the spaces from the string'))