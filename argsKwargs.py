# def employee(*emp_name):
#     print('Employee name: ' + emp_name[0])
# employee('Nabeel', 'Usama', 'Saad', 'Zain', 'Zariyab')

# def data(**kwargs):
#     print('Employee Data: ' + kwargs['fullName'])
# data(fullName = 'Muhammad Nabeel', address = 'Pakistan, Karachi')

# def introduction(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} is {value}')
# person = {'Name': 'Nabeel', 'city': 'Karachi'}
# introduction(**person)

# my_string = 'This is a Quiz'
# a, b, *c = my_string
# print(*c)

# def emp_data(**data):
#     print(f'Employee Name: ' + data['name'] + '\n' + 'City: ' + data['city'])
# employees = {'name': 'M Nabeel', 'city': 'Karachi'}
# emp_data(**employees)