#Tuples : ordered, immutable, allows duplicate
import timeit
mytuple = ("max",28,"boston")
# print(type(mytuple))
# single element is not considered as tuple
mytuple = ("Max")
# print(type(mytuple))
# single element is not considered as tuple but it is if you include a comma
mytuple = ("Max",)
# print(type(mytuple))

# from a list to tuple
mytuple = tuple(["Max",28,"Boston"])
# print(type(mytuple))
# print(mytuple[-1])
# print(mytuple[1])

# Immutable
# mytuple[0] = "Min"

#iteration
# for item in mytuple:
#    print(item)
# if "Max" in mytuple:
#    print("Yes")
# else:
#    print("No")

# count method
numbers = (1,2,3,2,4,2,3)
# print(numbers.count(3))

# index method
index = numbers.index(1)
# print(index)

# from tuple to list
# list = [1,2,3,4]
# converted_tuple = tuple(list)
# print(type(converted_tuple))
lists = (1,2,3,4)
converted_list=list(lists)
# print(type(converted_list))

names= ["jack","ram","kiddle"]
# print(names.count("Ram"))
name= "Asfakul"
# print(name + " Laskar")
#reverse a string
# print(name[::-1])

#reverse a tuple
names = ("A","B","C")
# print(names[::-1])

# unpacking a tuple
cities_tuple=("Delhi","Kolkata","Ahmedabad")
citi1,citi2,citi3 = cities_tuple
# print(citi1)
# print(citi2)
# print(citi3)

# unpacking multiple values

cities_tuple=("Delhi","Kolkata","Ahmedabad","Bangalore","Pune","Burdwan")
citi1, *citi2, citi4  = cities_tuple
# print(citi1)
# print(citi4)
# print(citi2)


# tuples are faster than list 

# print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))
# print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000))

cities= ("Koklata","Delhi","Ahmedabad","Noida")
citi1,*citi2,citi3 = cities
print(citi1)
print(type(citi2))

name= "Asfakul"
family_name=" Laskar"
full_name=name+family_name
print(full_name)
# reverse a name
# print(name[::-1])