# def employee(*emp_name):
#     print('Employee name: ' + emp_name[0])
# employee('Nabeel', 'Usama', 'Saad', 'Zain', 'Zariyab')

# def data(**kwargs):
#     print('Employee Data: ' + kwargs['fullName'])
# data(fullName = 'Muhammad Nabeel', address = 'Pakistan, Karachi')

def introduction(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} is {value}')
person = {'Name': 'Nabeel', 'city': 'Karachi'}
introduction(**person)

my_string = 'This is a Quiz'
a, b, *c = my_string
print(*c)