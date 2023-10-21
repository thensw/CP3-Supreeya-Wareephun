menuList = []
priceList = []
total = 0
while True:
    menuName = input('please enter menu: ')
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = int(input('Price: '))
        total+=menuPrice
        menuList.append(menuName)
        priceList.append(menuPrice)

def showBill():
    print("--- Receipt ---")
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])
    print(f'Total : {total}')

showBill()