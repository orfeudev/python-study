# a report card to train decision structures

print('What are your three score?')
      
a = float(input('score 1: '))      
b = float(input('score 2: '))    
c = float(input('score 3: '))    

score_mean = (a + b + c) / 3
print(('Your mean is: '), round(score_mean , 1))

if score_mean <= 3.9:
    print('you shall not pass!!')
elif 4 <= score_mean <= 6.9:
    print('final avaliation')
elif 7 <= score_mean <= 8:
    print('Good job!')
else: 
    print('Congratulations!')   
