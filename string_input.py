#!/usr/bin/env python3

name = input('Enter your name:')
#Enter your name:Santosh
#name
#'Santosh'
age = input('Enter your age:')
# Enter your age: 24
print(type(age))
print('My name is {0} and age {1}'.format('Santosh', '24'))
#My name is Santosh and age 24
# Alternative approach
print('my name is {name} and age is {age}'.format(age=24, name='Santosh'))

name = input('Enter your name:')
age = int(input("Enter yoiur age"))
print(f'your name is: {name} and age is: {age}')
print(type(name),type(age))
