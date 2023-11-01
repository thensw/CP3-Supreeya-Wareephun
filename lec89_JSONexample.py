import json
#JSON : "key":value , python : dictionary
def readJSON():
    # JSON: ข้อมูลจะอยู่ในลักษณะ "key":value
    x =  '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x) # *** แปลงJSON -> python

    # the result is a Python dictionary
    print(y["age"])

def writeJSON(): #Convert from Python to JSON:
    # a Python object (dict):
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x) # *** แปลงpython -> JSON

    # the result is a JSON string:
    print(y) #ข้อมูล JSON อยู่ในรูปแบบ String
    #ถ้าเราอยากให้มันเป็นรูปแบบไฟล์ เราก็สามารถนำข้อความไปเก็บเป็นไฟล์ได้เช่นเดียวกัน

readJSON()