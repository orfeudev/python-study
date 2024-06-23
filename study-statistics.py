import statistics

# Built-in Python functions

# abs(): Returns the absolute value of a number (modulus).
print(abs(-5))

# max(): Returns the largest item in an iterable or the largest of two or more arguments.
print(max(1, 2, 3, 4, 121))

# min(): Returns the smallest item in an iterable or the smallest of two or more arguments.
print(min(-2, 0, 3, 88))

# round(): Rounds the first number to the number of decimal places given in the second argument.
print(round(3.14159, 3))

# sum(): Sums all numbers in an iterable.
print(sum([2, 6, 7, 10, 15]))

# Statistics

# mean(): Calculates the arithmetic mean of the given data.
# The arithmetic mean is the sum of all values divided by the number of values.
# median(): The median is the value that divides the data set in half.
# For an odd number of values, it is the middle value. For an even number, it is the average of the two central values.
# mode(): The mode is the value that appears most frequently in the data set.
# stdev(): The standard deviation is a measure that expresses the degree of dispersion of a data set.
# The closer to 0 the standard deviation is, the more homogeneous the data.
# variance(): Variance is a measure of dispersion that checks the distance between values from the arithmetic mean.

# DATA

heights = [1.50, 1.60, 1.70, 1.80, 1.90, 2.00, 2.10, 2.20, 2.30, 2.40]
print(heights)

# Mean
mean = statistics.mean(heights)
print(f'Mean = {mean}')

# Median
median = statistics.median(heights)
print(f'Median = {median}')

# Check for duplicates values to calculate mode
# When converting something to a set, all duplicate values are removed.

if len(set(heights)) == len(heights):
    print('All values are unique, there is no mode.')
else:
    mode = statistics.mode(heights)
    print(f'Mode = {mode}')

# Standard Deviation
standard_deviation = statistics.stdev(heights)
print(f'Standard deviation = {standard_deviation}')

# Variance
variance = statistics.variance(heights)
print(f'Variance = {variance}')

# Reading tips
# books.goalkicker.com/pythonbook
# fluentpython.com