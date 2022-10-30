mylist = list()
mylist.append("Names")
print(mylist)

# check if an item is in a list
fruits = ["Apple","Banana","Orange"]
if "Kela" in fruits:
   print("Yes")
else:
   print("Not exists")

# length of the list
length = len(fruits)
# print(length)

fruits.insert(1,"Blueberry")
fruits.insert(2,"CranBerry")
# print(fruits)

#remove an item by index 
# fruits.pop(3)
# print(fruits)

# remove an item by actual item
# fruits.remove("Orange")
# print(fruits)

# remove all elements
# fruits.clear()
# print(fruits)
# it changes the original list
# sorted method 
copied_fruits= sorted(fruits)
#original is unchanged
# print(fruits)
# print(copied_fruits)

# tricks
repeated_numbers = [0] * 10
# print(repeated_numbers)
repeated_numbers.append(15)
#reverses the original list  
repeated_numbers.reverse()
# print(repeated_numbers)

#slicing
repeated_numbers = [1,2,3,4,5,6,7,8,9,0] * 10
# print(repeated_numbers)
a = repeated_numbers[1:8]
# print(a)

#copying a list 

fruits = ["apples","banana","oranges","guavas"]
# now create a copy
b = fruits.copy()
b.append("kiwis")
# print(fruits)
# print(b)

# list comprehension

mylist = [1,2,3,4,5]
a = [i*2 for i in mylist]
print(a)
print(mylist)

