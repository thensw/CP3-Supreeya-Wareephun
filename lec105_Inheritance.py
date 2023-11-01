# แม่แบบภาพรวมของยานพาหนะ : Inheritance
class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirCondition(self):
        print("Turn On : Air")

# สืบทอดแม่แบบ : ใส่ชื่อclassแม่แบบไว้ในวงเล็บinput
class PickUp(Vehicle):
    # เพิ่ม func. ในเฉพาะ class ย่อยนี้ (PickUp) : ไม่ได้ไปยุ่งกับ class หลัก (Vehicle)
    def sayHello(self):
        print("Hello PickUp")

class Car(Vehicle):
    def sayHello(self):
        print("Hello Car")
class Van(Vehicle):
    def sayHello(self):
        print("Hello Van")
class EstateCar(Vehicle):
    def sayHello(self):
        print("Hello EstateCar")

# เรียกใช้งาน Class และ function
PickUp1 = PickUp()
PickUp1.turnOnAirCondition()
PickUp1.sayHello()

Car1 = Car()
Car1.turnOnAirCondition()
Car1.sayHello()
Van1 = Van()
Van1.turnOnAirCondition()
Van1.sayHello()
EstateCar1 = EstateCar()
EstateCar1.turnOnAirCondition()
EstateCar1.sayHello()