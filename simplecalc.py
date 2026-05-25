print("Enter a number for operation")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
print("5 for percentage calculation")


print("Enter 2 numbers")
num1=int(input())
num2=int(input())
print("Enter operation:")
op=input()

if op=='1':
    print((num1+num2))
elif op=='2':
    print((num1-num2))
elif op=='3':
    print((num1*num2))
elif op=='4':
    if num2==0:
        print("Division by zero is not allowed!!")
    else:
        print((num1/num2))
elif op=='5':
    if num2==0:
        print("Division by zero is not allowed!!")
    else:
        print(float((num1/num2)*100))
else:
    print("Invalid input :)")
    print("Enter a valid one!!")



