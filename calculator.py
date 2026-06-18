print("Simple calculator")
print("Operations: + - * /")
num1 = float(input("Enter first number:"))
operation = (input("Enter operation: "))
num2 = float(input("Enter second number:"))
print(num1,operation,num2)
if operation == "+":
 print(num1+num2)
elif operation =="-":
    print (num1-num2)
elif operation == "*":
    print (num1*num2)  
elif operation == "/" :
    print(num1/num2) 
else:
    print("invalid operation")




