#simple calculator using match statmant

def calculator_using_match():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    sign = input('''
enter + for addition
enter - for substraction
enter * for multiplication
enter / for division
enter % for reminder             
''')
    match sign:
        case('+'):
            print(num1 + num2)
        case('-'):
            print(num1 - num2)
        case('*'):
            print(num1*num2)
        case('/'):
            print(num1/num2)
        case('%'):
            print(num1 % num2)
        case _:
            print("enterd input is unvalid ",sign)

# simple calculator using eval statment

def calculator_using_eval():
    num1 = (input("enter first number: "))
    num2 = (input("enter second number: "))
    sign = input('''
enter + for addition
enter - for substraction
enter * for multiplication
enter / for division
enter % for reminder             
''')
    if sign == '+' or '-' or '/' or '*' or '%':
        print(eval(num1 + sign + num2))
    else:
        print("enterd input is unvalid ",sign)


# Except None , 0 ,"",(),[],{},false everything else is true in Python

