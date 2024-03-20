bool_val = True
int_val = 7
float_val = 4.5
print(int_val + bool_val)
print(bool_val + int_val)
print(float_val + int_val)
print(int_val + float_val)

print(int_val.__add__(float_val))
print(float_val.__radd__(int_val))
# print(float_val.__add__(int_val))

print(bool(-1))

print(help(int_val.__eq__))
