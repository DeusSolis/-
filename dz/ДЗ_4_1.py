list_1 = [1, 12, 12, 4, 5, 6, 7, 8, 14, 11.55, 11.55, 3.14]

# a. Виведіть усі елементи списку з парними індексами
if len(list_1) >= 10:

    print([x for x in list_1 if x % 2 == 0])
# b. Знайти суму елементів всього списку.

    sum = 0
    for x in list_1:
        sum += x
    print(sum)

# c. Знайти суму парних елементів списку та окремо непарних елементів списку.

    print([x + x for x in list_1 if x % 2 == 0])
    print([x + x for x in list_1 if x % 2 != 0])

# d. Виведіть значення найбільшого елемента у списку, а потім індекс цього елемента у списку.

    print("Max value element : ", max(list_1))
    print("Max value element : ", list_1.index(max(list_1)))
else:
    print("Not enough characters")

