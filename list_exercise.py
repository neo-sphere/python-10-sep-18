names = ['santosh', 'amit', 'kushal', 'aryan']
print('List'.center(50, '#'))
print(names)
# for loop
for name in names:print(name)
print('Capitalize Name'.center(50, '~'))
for name in names:print(name.capitalize())

# special case
print('Different Data type in list'.center(40, '*'))
names = ['santosh', 'amit', 'kushal', 'aryan', 2]
for name in names:print(name.capitalize() if isinstance(name,str) else name)


# Index
print(names[0], names[2])

# slicing


# list comprehension
print('List comprehension'.center(40, '-'))
a = list(range(1, 50))
mul_of_5 = [i for i in a if i%5 is 0] # if only
print(mul_of_5)
names = ['santosh', 'amit', 'kushal', 'aryan']
cap_names = [name.capitalize() for name in names]
print(cap_names)
names = ['santosh', 'amit', 'kushal', 'aryan', 2]
cap_names = [name.capitalize() if isinstance(name, str) else name for name in names] # if else
print(cap_names)



# Ternarry Operator
print('Ternarry Operator'.center(50, '~'))
pass_mark = 40
obtain_mark = 70
is_pass = True if obtain_mark >= pass_mark else False
print(is_pass)

obtain_mark = 30
is_pass = True if obtain_mark >= pass_mark else False
print(is_pass)
