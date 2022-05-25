#create a program that request two numbers and show division if divisor is 0 return error

number1 = int(input("Please digit the first number -Dividendo: "))
number2 = int(input("Please digit the second number -Divisor: "))
if(number2 == 0):
    print("Error, the second number DIVISOR can't is 0")
else:
    result = int(number1/number2)
    print(f"The result is {result}")