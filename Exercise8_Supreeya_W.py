user = input('Username: ')
password = input('Password: ')
if user == 'noon' and password == '1234':
    print('Welcome to my cafe!')
    print('------- MENU -------')
    print('1) Americano      3$')
    ame = 3
    print('2) Matcha Latte   4$')
    matcha = 4
    order = int(input('What would you like to drink? (1 or 2) :'))
    if order == 1:
        num = int(input('How many cups? :'))
        print(f'Order total : Americano {num} = {ame*num}$')
    elif order == 2:
        num = int(input('How many cups? :'))
        print(f'Order total : Matcha Latte {num} = {matcha * num}$')
    else:
        print('please order again.')