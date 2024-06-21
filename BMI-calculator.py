#A BMI calculator to train the python fundaments 

print('Welcome to the BMI calculator')

name = input('Whats your name?: ') 
print(f'Hi, {name}, lets calculate your BMI.')

weight = float(input("What is your weight?"))
height = float(input("Whats your height?"))
print('wait...')

calc_BMI = weight/(height)**2
print(round(calc_BMI,2))


if calc_BMI < 18.5:
    print(f'{name}, your BMI indicates that you are underweight.')
elif 18.5 <= calc_BMI < 25:
    print(f'{name}, great job! Your BMI shows that you have a normal weight.')
elif 25 <= calc_BMI < 30:
    print(f'{name}, your BMI indicates that you are overweight.')
elif 30 <= calc_BMI < 35:
    print(f'{name}, your BMI suggests that you are in the Obesity Class I.')
elif 35 <= calc_BMI < 39.9:
    print(f'{name}, your BMI suggests that you are in the Obesity Class II.')
else: 
    print(f'{name}, your BMI suggests that you are in the Obesity Class III.')