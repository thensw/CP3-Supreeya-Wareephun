import csv

def readCSV():
    with open('lec87_Example_csv.txt') as csv_file: #with .. as .. เหมือนยัดคำสั่ง open(file) ลงในตัวแปร csv_file
        csv_reader = csv.reader(csv_file, delimiter=',') #delimeter : แยกข้อมูลด้วย ',' (comma)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {row}') : จะได้ข้อมูลเป็น <class 'list'>
                print(f'Column names are {",".join(row)}') # ",".join(ตัวแปร) : ใช้ , คั่นระหว่างข้อมูลในตัวแปร
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
            print(f'Processed {line_count} lines.')

def writeCSV(): #runแล้วจะมีไฟล์ใหม่เกิดขึ้นตามชื่อที่ตั้ง (employee_file.csv)
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['Noon', 'jubjub', 'Aug']) # [ <class 'list'> ]
        employee_writer.writerow(['tay', 'rak fan', 'Nov'])

readCSV()