# Faulty calculator
# 23 * 4 = 24, 34 + 23 = 3, 23/3 = 345

num1 = int(input("Enter first number: "))
opt = input("Enter the operation you wanna perform: ")
num2 = int(input("Enter second number: "))

if opt == "*" :
    ans = num1 * num2
    ans = 3
    print(ans)

elif opt == "+" :
    ans = num1 + num2
    ans = 1000
    print(ans)

elif opt == "-" :
    ans = num1 - num2
    print(ans)

elif opt == "+" :
    ans = num1 + num2
    print(ans)

elif opt == "/" :
    ans = num1 + num2
    ans = -2
    print(ans)

elif opt == "%" :
    ans = num1 + num2
    print(ans)

else :
    print("Invalid operator")