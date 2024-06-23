# Decision structure to check if a number is even or odd.
# The symbol % in Python is called the modulo operator. 
# It returns the remainder of the division of the left-hand operand by the right-hand operand. 
# It is used to obtain the remainder of a division problem.

number = int(input('type a number: '))
remainder = number % 2 
if remainder == 0: 
    print('this number is even')
else:
    print('this number is odd')