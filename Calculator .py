from os import system

a = round(int(input('Write the first number: ')))
b = round(int(input('Write the second number: ')))
operators = input('Choose operations: \n'
                  "1 - Multiplication \n"
                  "2 - Divide \n"
                  "3 - Substraction \n"
                  "4 - Addition \n")
if(operators == '4'):
    _ = system('cls')
nswer = x + y
    print(f'{x} + {y} = answer}')
elif(operators == '3'):
    _ = system('cls')
nswer = x - y
    print(f'{x} - {y} = nswer}')
elif(operators == '1'):
    _ = system('cls')
nswer = x * y
    print(f'{x} * {y} = nswer}')
else:
    _ = system('cls')
nswer = x / y
    print(f'{x} / {y} = nswer}')
