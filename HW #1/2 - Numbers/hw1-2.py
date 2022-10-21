# Zahir Choudhry
# HW 2 - Numbers
# 9/10/21

#Create Number Inputs
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))

#Get sum of numbers
sum = num_1 + num_2

#Get string of nums, then convert back into a number
str_1 = str(num_1)
str_2 = str(num_2)

concat = str_1 + str_2

#Outputs final product
print("Adding the two numbers gives " + str(sum) + ", which is different from " + concat + ".")
