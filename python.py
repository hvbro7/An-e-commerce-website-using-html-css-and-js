first_number = input("Enter First Number : ")

Operator = input("Enter operator (+,-,*,/)")

second_number = input("Enter second Number : ")

if Operator == '+':
    print(int(first_number) + int(second_number))
elif Operator == '-':
    print(int(first_number) - int(second_number))
elif Operator == '*':
    print(int(first_number) * int(second_number))
elif Operator == '/':
    print(int(first_number) / int(second_number))
else: print("Kuch bhi mat likh")           