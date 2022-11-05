def fun(list_1: list, index_start_sort: int, index_end_sort: int) -> list:
    """Фукція для сортування: приймає список, та індекс
	початку сортування та індекс кінця сортування,
	і повертає список у якому відсортовані лише ті елементи,
	які укладені між індексом початку сортування та індексом
	кінця сортування."""
    sort_1 = sorted(list_1[index_start_sort:index_end_sort])
    list_1[index_start_sort:index_end_sort] = sort_1

    return print(list_1)


fun([1, 44, 33, 22, 12, 14], 0, 4)
fun()
