##DICTIONARY AND SETS##


# info = {
#     "key" : "value",
#     "name" : "apnacollege",
#     "learning":"coding",
#     "age" : 35,
#     "is adult" : True,
#     "marks" : 94.45
# }

# print(info)

# info = {
#     "key" : "value",
#     "name" : "apnacollege",
#     "learning" : "coding"
# }

# print(info)

##we can store lists and tuples in dictionaries 


# info = {
#     "key" : "value",
#     "subjects" : ["python", "C", "Java"], #list
#     "name" : "apnacollege",
#     "topics" : ("dict","sets"), #tuples
#     "learning" : "coding",
#     "age" : 35,
#     "is_adult" : True,
#     "marks": 94.4
# }

# print(type(info))

#keys me str boolean int float tup sb chlega pr list nhi chlega cause list mutable hota hai
#dic are unorderd mutable and dont allow duplicate keys


##Accesing values from dictianaries

# dict = {
#     "key" : "value",
#     "name" : "apnacollege",
#     "learning" : "coding",
#     "age" : 35,
#     "is_adult" : True,
#     "marks": 94.4
# }

# print(dict["key"])
# print(dict["age"])
# print(dict["marks"])
# print(dict["learning"])

#assigning and adding values is also possible

# dict = {
#     "key" : "value",
#     "name" : "apnacollege",
#     "learning" : "coding",
#     "age" : 35,
#     "is_adult" : True,
#     "marks": 94.4
# }

# dict ["name"] = "shradha"
# dict ["surname"] = "khapra"
# print (dict)

##Empty dictionary##

# null_dict = {}
# print(null_dict)
# #addition in null dictionary
# null_dict = {}
# null_dict["name"] = "apna college"
# print(null_dict)

##NESTED DICTioNARIES#
#we nest a dictionary in a parent dictionary
# student = {
#     "name" : "RAHul KUMAR",
#     "subject" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" = 98
#     }
# }
# print(student)        
   

#for printing only subjects

# student = {
#     "name" : "RAHul KUMAR",
#     "subject" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }

# print(student["subject"])
# print(student["subject"]["chem"])  #for obtaining marks or value of a particular subject
#nested data se bhi relevant info nikal skta hai

##DICTIONARY METHODS##
#1. KEYS METHOD
# student = {
#     "name" : "RAHul KUMAR",
#     "subject" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }


# print(student.keys())
# print(list(student.keys())) #types casting
# print(len(student)) #total no of keys in the dictionary
# print(len(list(student.keys())))#total no of keys in the dictionary nikalna ka secoond way

#2. VALUES METHOD


# student = {
#     "name" : "RAHul KUMAR",
#     "subject" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }
# print(student.values())
# print(list(student.values()))#for converting it into a list#type casting

#3. ITEMS Method


# student = {
#     "name" : "RAHul KUMAR",
#     "subject" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }

# print(student.items())
# print(list(student.items()))
# pairs = list(student.items())
# print(pairs[0]) #for printing first pair from the list...aur first pair ek tuple hai...list ka hi fiirst pair hai jo isse print hoga 
# print(pairs[1])#for printing second pair from the list and second pair bhi ek tuple hai

#4. GET METHOD#


# student = {
#     "name" : "RAHul KUMAR",
#     "subject" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }

# print(student["name"])
# print(student.get("name"))
#dono me same hi value joki name ka value whi return hoga toh zaroorat kya padi get method key
# print(student["name2"])#ye error return krega kyoki aisa kuch hai hi nhi prrr
# print(student.get("name2")) #ye error nhi dega ye dega--> None


#4. UPDATE METHOD

# student = {
#     "name" : "RAHul KUMAR",
#     "subject" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }
# student.update({"city" : "delhi"})
# print(student)
           #OR#
# new_dict = {"city" : "delhi"}
# student.update(new_dict)
# print(student)
##ham chahe to isme aur bhi key value pairs add kr skte hai in the following way

# new_dict = {"city" : "delhi", "age" : 16}
# student.update(new_dict)
# print(student)

#ham purani key ki value ko overwrite bhi kr ske hai

# new_dict = {"name" : "Akshay Yadav"}
# student.update(new_dict)
# print(student)


####SETS IN PYTHON###

# set = {1, 2, "hello", "world", 4, 4, 4, 2}

# print(set)
# print(type(set))#it ignores duplicate values and type will be recognised as 'set'
# print(len(set))#length also ignores duplicate values

# collec = {} #if we want an empty set and we do this the type will be empty dict bec this syntax is for empty dict
# print(type(collec))

#so for an empty set

# collec = set()
# print(type(collec))

#SET METHODS########

#1.ADD METHOD AND REMOVE METHOD

# collec = set()

# collec.add(1)
# collec.add(2)
# collec.add(3)
# collec.add(3)#dusri bar likhne se koi fayda nhi hoga print ek hi bar hoga
# collec.remove(3)#for removing
# collec.remove(7)#this will give error bec 7 does not exist in the set

# print(collec)

#we can add anything in a set other than a list and dict

# collec = set()

# collec.add(1)
# collec.add(2)
# collec.add("apna college")#string
# collec.add((1, 2, 3))#tuple

# #collec.add([1, 2 , 3])#error dega...unhashable type kyoki ye list hai

# print(collec)

#CLEAR method


# collec = set()

# collec.add(1)
# collec.add(2)
# collec.add("apna college")#string
# collec.add((1, 2, 3))#tuple

# collec.clear()#empties the set

# print(collec)
# print(len(collec))

#pop method- it randomly picks a value from the set and sisplays it

# collec = {"hello","apnacollege","world","coding"}

# print(collec.pop())
# print(collec.pop())
# print(collec.pop()) #ye sb kuch bhi values dega unordered way me..

#SET UNION AND INTERSECTION

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.union(set2))#union of two sets
# print(set1.intersection(set2))#intersection of two sets
# print(set1)
# print(set2)

#######questions##############################

#Q1.#Store  the following word meaning in a python dictionary
  #table : "a piece of furniture", "list of facts & figure"
  #cat: "a small animal"
#answer---
# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figure"]
# }
# print(dictionary)

#Q2.You are given list of subjects. Assume one classroom is required for 1 subject. How many classroom are needed by all students.
#ans-

# subjects = {
#     "pyhton", "java", "c++", "javascript", "java",
#     "pyhton", "java", "c++", "c"
# }

# print(len(subjects))

#Q3.WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
#Ans-
# marks = {}
# marks["maths"] = int(input("Enter marks of maths: "))
# marks["science"] = int(input("Enter marks of science: "))
# marks["english"] = int(input("Enter marks of english: "))
# print(marks)

       #OR#####the method we use now is actually the answer of the question as we are going to use update feature bec in the last answer we did not use that and it was just a answer but not an answer which perfectly answers thre question

# marks = {}
# x = int(input("Enter phy marks:"))
# marks.update({"phy":x})
# y = int(input("Enter chem marks:"))
# marks.update({"chem":y})
# z = int(input("Enter math marks:"))
# marks.update({"math":z})
# print(marks)

#Q4.Figure out a way to store 9 & 9.0 as a separate values in the set...You can take help of a built in data types
#first possible soln
# value = {9, "9.0"} #or value = {"9", 9.0}
# print(value)
#second possible soln we make pairs in the form of tuples in set
# value = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(value)
#third possible soln
# value = {(9,9.0)} #this will be a set of tuples
# print(value)

################################LECTURE 4 OVERRR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
