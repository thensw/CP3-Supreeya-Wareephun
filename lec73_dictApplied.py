systemMenu = {'rice':30,'chic':15, 'cow':60} #ใช้dict
menuList = []
while True:
    menuName = input('please enter menu: ')
    if menuName.lower() == 'exit':
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

def showBill():
    total = 0
    print("--- Receipt ---")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        total +=int(menuList[i][1])
    print(f'Total : {total}')

showBill()