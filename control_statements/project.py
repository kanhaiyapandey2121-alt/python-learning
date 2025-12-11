num_1 = float(input('enter number 1 = '))
num_2 = float(input('enter number 2 = '))

choise = input('enter your choise + - * =')
if choise == '+':
    print(f'addition: {num_1 + num_2}')

elif choise == '-':
 print(f'subtraction: {num_1 - num_2}')

elif choise =='*':
 print(f'multiplication:{num_1 * num_2}')
 
else:
    print('Invalid choise')
