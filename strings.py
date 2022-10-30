# String is an ordered, immutable, text reprsentation
from timeit import default_timer as timer
my_string = "I'm a programmer"
# print(my_string)
# print(my_string[::-1])
white_space= "__Hello World+++"
print(white_space)
print(white_space.lstrip("_").rstrip("+"))

name="Asfakul Islam"
# invalid since strings are immutable 
# name[0] = "F"

# step index , every second character 
substring = name[::2]
print(substring)

print(name[::-1])
# greeting = "Hello"

# for i in greeting:
#    print(i)


# find 
print(name.find("Is"))
# count 
print(name.upper().count("A"))
# repalce a substring

print(name.replace("fa","FA"))
# sting to list 
greetings = "How_are_you_doing"
list1= greetings.split("_")

print(list1)

# from list to string
print(' '.join(list1))

# create a list of 6 'a'
repeated_list = ['ab'] * 6
print(repeated_list)


