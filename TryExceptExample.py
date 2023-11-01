import sys

randomList = ['a',2,0]
for entry in randomList:
    try:
        print(f'the entry is {entry}')
        r = 1/int(entry)
        break
    except:
        print(f'Oops! {sys.exc_info()[0]} occured.')
        print('Next entry.')
        print()
print(f'the reciprocal of {entry} is {r}')

assert randomList == [2,3,1],'Error you key incorrect.'