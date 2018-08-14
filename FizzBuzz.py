num = input('Please inpu NUMBER!')
num = int(num)
out = ''

if num % 3 == 0:
    out += 'Fizz'
if num % 5 == 0:
    out += 'Buzz'
if out == '':
    out += str(num)

print(out)
