# 1/0
# 'Nabeel'+27

num_1 = input('Enter Number 1: ')
num_2 = input('Enter Number 2: ')
try:
    total = int(num_1) / int(num_2)
except Exception as e:
    print('Exception Occured: ', e)
    total = None
print('Division is: ', total)