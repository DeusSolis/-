str_2 = str(input("Enter string: ").lower())

a = str_2[:str_2.find("h")]
b = str_2[str_2.find("h"):str_2.rfind("h") + 1:]
c = str_2[str_2.rfind("h") +1:]
print(a + b[::-1] + c)
