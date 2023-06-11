from add import add_numbers
from subtract import subtract_numbers
from multiply import multiply_numbers
from modulus import calculate_modulus
from squareroot import calculate_square_root
from divide import divide_numbers

# Take input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# Call the add function and store the result
result = add_numbers(a, b)

# Display the result
print("The sum is:", result)


# Take input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# Call the add function and store the result
result = subtract_numbers(a,b)

# Display the result
print("The subtract is:", result)



# Take input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# Call the multiplication function and store the result
result = multiply_numbers(a,b)

# Display the result
print("The multiplication is:", result)


# Take input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# Call the modulus function and store the result
result= calculate_modulus(a,b)
# Display the result
print("The modulus is:", result)



# Take input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# Call the squareroot function and store the result
result=calculate_square_root(a,b)
# Display the result
print("The squareroot is:", result)



# Take input from the user
dividend = int(input("Enter the dividend number: "))
divisor = int(input("Enter the divisor number: "))
# Call the squareroot function and store the result
result=divide_numbers(dividend,divisor)
# Display the result
print("The division is:", result)


