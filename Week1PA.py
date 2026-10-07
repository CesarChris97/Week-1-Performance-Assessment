# Student Identification
name = input("Please enter your name: ")
student_id = input("Please enter your Student ID: ")

# Input Numbers
num1 = int(input("Please enter a whole number: "))
num2 = int(input("Please enter a different second whole number: "))

# Math Calculations
mult_res = num1 * num2
div_res = num1 / num2
add_res = num1 + num2

# Display Calculation Results formatted to 2 decimal places
print(f"The result of {num1} times {num2} is: {mult_res:.2f}")
print(f"The result of {num1} divided by {num2} is: {div_res:.2f}")
print(f"The result of {num1} plus {num2} is: {add_res:.2f}")

# Comparison Logic
if num1 > num2:
    print(f"Number 1 is larger than Number 2")
elif num1 < num2:
    print(f"Number 1 is smaller than Number 2")
else:
    print(f"Number 1 is equal to Number 2")

# Output Name and Student ID
print(name)
print(student_id)
