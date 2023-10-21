menuList = []
while True:
    menuName = input('please enter menu: ')
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = int(input('Price: '))
        menuList.append([menuName,menuPrice])
        #listใน [เมนู,ราคา] ซ้อน listนอก [ตามจำนวนเมนูที่user input เข้ามา]

def showBill():
    print("--- Receipt ---")
    for i in range(len(menuList)):
        print(menuList[i][0]) #เลือกโชว์แค่ menuName จึงเลือกลำดับ 0

showBill()