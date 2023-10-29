
from operations2 import add,subtract,multiply,divide,power,module

def game(option,subtract,num_1,num_2,answer,score):
    score = 0
    while True:
        print('======== Menu ========'
        '\n1. Add'
        '\n2. Subtract'
        '\n3. Multiply'
        '\n4. Divide'
        '\n5. Power'
        '\n6. Module'
        '\n0. Exit')
        option = int(input('\nChoice an option: '))

        if option == 0:
            break

        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = float(input('Enter you answer: '))

        if option == 2:
            result = subtract(num_1,num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        
        if option == 3:
            result = multiply(num_1,num_2)
            if result == answer:
                score += 2
                print('Correct!!')
            else:
                print('Incorrect')

        if option == 4:
            result = divide(num_1,num_2)
            if result == answer:
                score += 2
                print('Correct!!')
            else:
                print('Incorrect')
        
        if option == 5:
            result = power(num_1,num_2)
            if result == answer:
                score += 4
                print('Correct!!')
            else:
                print('Incorrect')

        if option == 6:
            result = module(num_1,num_2)
            if result == answer:
                score += 4
                print('Correct!!')
            else:
                print('Incorrect')
        
        print(f'======== Game Over ========'
        f'\nYou score is {score}'
        '\nKeep going!')

game()