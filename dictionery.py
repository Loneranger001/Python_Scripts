# dictionaries
# key-value pair , unordered and mutable 

from turtle import clear


mydict = {
   "name":"Asfakul",
   "familyName":"Laskar",
   "Country":"India"
}

# print(mydict)

value=mydict["name"]
# print(value)

# this will be error
# value=mydict["State"]
# print(value)

value=mydict.get("name")
# print(value)
# add 1 new element 
mydict["State"] = "WB"
# print(mydict)

#delete an element

# del mydict["name"]
# print(mydict)

value = mydict.pop("State")
# print(value)
# print(mydict)

# check if a key is in a dict
# if "name" in mydict:
#    print(mydict["name"])

# capitals dictionery
capitals ={
   "India":"Delhi",
   "USA":"Washington",
   "Canada":"Ottawa",
   "Poland":"Warshaw"
}

# print(capitals["India"])
capitals["Sri Lanka"] = "Colombo"
# print(capitals)
# print(capitals.get("India"))
# if "India" in capitals:
#    print(capitals["India"])

# loop
# for key in capitals.keys():
#    print(capitals[key])
# for key,value in capitals.items():
#    print("Country :" + key + ", Capital :" + value)
# copy a dictionery

copied_dict = capitals.copy()
# print(copied_dict)
value = copied_dict.pop("India")
# print(value)

# update a dictionery

dict1 = {"name":"Asfakul","age":13}
dict2 = {"name":"Fraser","age":18,"occupation":"doctor"}
#update dictionery 1
dict1.update(dict2)
# print(dict1)
# print(dict2)

# numbers=[1,2,3]
# num_sqrt=[x*x for x in numbers]
# print(num_sqrt)