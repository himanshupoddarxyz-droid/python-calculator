StartName = input("Enter your name and start the calculator,capable of performing Addition, Subtraction, Division, IntDivision, Remainder :")
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
add = num1 + num2 #Addition of inputs
sub = num1 - num2 #Subtraction of inputs
multi = num1 * num2 #Multiplication of inputs
division_int = num1//num2 #Output will be an integer because it's an integer division
division = num1/num2 #Output will be float because it's a floor dividion. Implicict(automatic) data type conversion. Division of two integers = Float value
remainder = num1%num2 #Remainder of inputs
print("*******************************************************************************************")
print("                                                                                           ")
print("Addition of entered values = " +str(add))
print("Subtraction of entered values = "+ str(sub))
print("Product of entered values = "+str(multi))
print("Integer Division of entered values = "+str(division_int))
print("Floor Division of entered values = "+ str(division))
print("Remainder of entered values = "+ str(remainder))
print("                                                                                           ")
print("*******************************************************************************************")
print("Thank you! "+StartName+", for using this calculator and showing your interest.")