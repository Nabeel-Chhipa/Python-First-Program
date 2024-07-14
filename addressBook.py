import json

data = {}
data['Nabeel'] = {
    'name': 'Nabeel',
    'city': 'Karachi'
}
data['Usama'] = {
    'name': 'Usama',
    'city': 'Lahore'
}
data['Saad'] = {
    'name': 'Saad',
    'city': 'Islamabad'
}
# WRITE DTAA IN .TXT FILE
usersData = json.dumps(data)
with open('E:/Development/Python/data.txt', 'w') as f:
    f.write(usersData)
# print('user data', usersData)

# READ DATA FROM .TXT FILE
# file = open('E:/Development/Python/data.txt', 'r')
# fileText = file.read() #STRING FILE TYPE
# print('File Data', fileText, 'File Type', type(fileText))

# READ DATA FROM .TXT FILE
file = open('E:/Development/Python/data.txt', 'r')
fileData = file.read() #DIST FILE TYPE
fileText = json.loads(fileData)
# print('File Data', fileText, 'File Type', type(fileText))
# print('Data', fileText['Saad']['city'])
for item in fileText:
    print(fileText[item]['city'])