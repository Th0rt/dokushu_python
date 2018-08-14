height = int(input('Please input your height.'))
weight = int(input('Please input your weight.'))

bmi = weight / (height / 100) ** 2

if bmi < 18.5:
    print('you are slim body!')
elif bmi < 25:
    print('you are normal body!')
elif bmi < 35:
    print('you are a little fat body!')
elif bmi > 35:
    print('you are fat body!')
