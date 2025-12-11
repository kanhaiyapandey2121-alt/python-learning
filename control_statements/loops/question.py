start = int(input('enter start= '))
stop = int(input('enter stop= '))

skip = int(input('number you want skip= '))

for i in range(start, stop):
    if i == skip:
        continue
    print(i)