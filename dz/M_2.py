str_1 = str(input("Enter string: "))

digit = sum(i.isdigit() for i in str_1)
lower_case = sum(i.islower() for i in str_1)
upper_case = sum(i.isupper() for i in str_1)
sign = len(str_1) - (digit+lower_case+upper_case)
list_1 = [digit,lower_case,upper_case,sign]
print(list_1)

