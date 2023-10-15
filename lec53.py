def vatCal(totPrice):
    result = totPrice+(totPrice*7/100)
    return result
user = int(input('Enter total price: '))
print(vatCal(user))