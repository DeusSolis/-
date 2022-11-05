# list_1 = [32, 4.43, 'lister', False, None, [1,2,3,4]]
def new(list_1):
    str_1 = " ".join(map(str,list_1))
    return str_1
print(new([32, 4.43, 'lister', False, None, [1,2,3,4]]))