def fun (list_1, start_sort, end_sort):

    a = sorted(list_1[start_sort:end_sort])
    list_1.extend(a)
    return list_1
fun([1,10,9,4,5,7,2,0], 2, 6)