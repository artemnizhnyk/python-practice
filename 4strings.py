my_name = 'Artem'
print(my_name)

print(type(my_name))
print(id(my_name))

print("-------------------------")

long_string = """This is a 
very long string"""

print(long_string[0])
print(long_string[0:4])
print(long_string.index("is a"))

print("-------------------------")

my_comment = "This is my short comment"
print(len(my_comment))
my_new_comment = my_comment.replace('short', 'long')

print(my_comment)
print(my_new_comment)

print(my_comment.count(' '))
print(my_comment[-1])
print(my_comment[4:])
print(my_comment[:4])
print(my_comment[:])

print("-------------------------")
