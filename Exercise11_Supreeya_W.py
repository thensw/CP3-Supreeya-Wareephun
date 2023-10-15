user = int(input('Enter row: '))
for r in range(user):
    space = (user-(r+1))*' '
    show = ((2*r)+1)*'*'
    print(space,show,space)