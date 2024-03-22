my_dict = {
    'name': 'Artem',
    'age': 22,
    'height': 180,
    'weight': 76.5,
}

print(my_dict['name'])
print(dir(my_dict))

my_dict['weight'] = 76.4
print(my_dict)

my_dict['isStraight'] = True
print(my_dict)

del my_dict['age']
print(my_dict)

print('----------------------------------')

key_for_name = 'name'
print(my_dict[key_for_name])
