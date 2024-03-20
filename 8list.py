nums = [1, 2, 3]
another_nums = [1, 3, 2]
print(nums == another_nums)

another_nums.sort()
print(nums == another_nums)

del nums[0]
print(nums)

users = [
    {
        'name': "Artem",
        'age': 22,
        'isNice': True
    },
    {
        'name': "Daniel",
        'age': 23,
        'isNice': True
    }
]

print(users[0]['name'])

strings = []
strings.append('A')
strings.append('B')
strings.append('C')
print(strings)
strings.pop()
print(strings)
strings.pop(0)
print(strings)

print('--------------------------')

greeting = "Hello world"
greeting_letter = list(greeting)
print(greeting_letter)

my_dict = {'a': 10, 'b': True}
list_from_dict = list(my_dict)
print(list_from_dict)

print('--------------------------')

first_list = [1, 2, 3]
second_list = [4, 5, 6]
big_list = first_list + second_list
print(big_list)

first_two_elements = big_list[:2]
middle_two_elements = big_list[2:4]
last_two_elements = big_list[-2:]
print(first_two_elements)
print(middle_two_elements)
print(last_two_elements)

print('--------------------------')
