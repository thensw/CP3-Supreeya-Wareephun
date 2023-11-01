#พิมพ์เขียว
class Customer:
    name = ""     #เป็นแค่พิมพ์เขียว ให้เว้นไว้ ไม่ต้องใส่ข้อมูล
    lastname = ""
    age = 0    #ค่าเริ่มต้น

    def addCart(self):
        #จะเรียกใช้ตัวแปรในclass ต้องเขียน self.ตัวแปร เป็นการเรียกใช้ในคลาสของตัวมันเอง
        print(f"Added to {self.name} {self.lastname} 's cart")

#เรียกใช้งานจริง สร้างตัวแปรใหม่ขึ้นมา
customer1 = Customer()   #เรียกใช้งาน class
customer1.name = "Supreeya"
customer1.lastname = "W"
customer1.addCart()   #เรียกใช้งาน func ใน class

customer2 = Customer()
customer2.name = "Sadudee"
customer2.lastname = "C"
customer2.addCart()