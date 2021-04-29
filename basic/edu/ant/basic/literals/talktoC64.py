import random

import dateutil.utils


def reverse(s):
    return s[::-1]


def current_year():
    return dateutil.utils.today().year


print('Hello, world!')
print('I am C64. What is your name?')
name = input()
print('Welcome ' + name)
print('Reversed anagram of your name is:')
print(reverse(name))
print('Random anagram of your name is:')
print(''.join(random.sample(name, len(name))))
print('What is your age?')
age = input()
born = str(current_year() - int(age))
print('So you were born in ' + born)
