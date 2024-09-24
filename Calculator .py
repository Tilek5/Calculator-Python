from os import system

a = round(int(input('Write the first number: ')))
s = round(int(input('Write the second number: ')))
operators = input('Write the operations u want(+ - * /:) ')
if(operators == '+'):
    _ = system('cls')
    asd = a + s
    print(f'{a} + {s} = {asd}')
elif(operators == '-'):
    _ = system('cls')
    asd = a - s
    print(f'{a} - {s} = {asd}')
elif(operators == '*'):
    _ = system('cls')
    asd = a * s
    print(f'{a} * {s} = {asd}')
else:
    _ = system('cls')
    asd = a / s
    print(f'{a} / {s} = {asd}')
