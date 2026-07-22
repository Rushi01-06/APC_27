num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1>=num2 and num1>=num3:
    print("largest=",num1)
elif num2>=num1 and num2>=num3:
    print("largest=",num2)
else:
    print("largest=",num3)

if num1<num2 and num1<=num3:
    print("smallest=",num1)
elif num2<=num1 and num2<=num3:
    print("smallest=",num2)
else:
    print("smallest=",num3)




    
