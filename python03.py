##LIST DATA TYPES IN PYTHON
# marks1 = 94.4
# marks2 = 90.4
# marks3 = 88.4
# marks4 = 92.4

# aise krne me bohot time lagega toh ham list data type ka use krte hai  

# marks = [94.4, 90.4, 88.4, 92.4]
# print(marks)
# print(type(marks))
# print(marks[0]) 
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(len(marks))

# In python list me different data types ke elements ho skte hai

# student = ["karan", 95.4, 17, "Delhi"]
# print(student)

# #IMP-->Pyhton me strings immutable hote hai but list mutable hote hai matlab list ke elements ko change kr skte hai

# str = "hello"
# print(str[0])
# str[0] = "H"    #ye error dega kyuki string immutable hai
#                   but list mutable hote hai toh list ke elements ko change kr skte hai

# student = ["karan", 95.4, 17, "Delhi"]
# print(student)
# student[0] = "Arjum"
# print(student)

# Indexing me values access honge jo list me exist krte hai wrna out of range show krega

# ###LIST SLICING IN PYTHON#####

# marks = [94.4, 90.4, 88.4, 92.4]
# print(marks[0:2])  #0 se 2 tak print hoga but...last element print nhi hoga
# print(marks[1:])   #1 se last tak print hoga
# print(marks[:3])   #0 se 3 tak print hoga but...last element print nhi hoga

# #NEGATIVE INDEXING OF LISTS IN PYTHON

# print(marks[-3:-1])

# ##LIST METHODS IN PYTHON##3

# 1.>List Appending

# list1 = [1, 2, 3, 4, 5]
# list1.append(6)  #append method se last me element add hoga
# print(list1)

# 2.>List Sorting
#     It is of two types ... ascending and descending

# list2 = [5, 2, 9, 1, 7]
# list2.sort()  #ascending order me sort hoga
# print(list2)

# list2 = [5, 2, 9, 1, 7]
# print(list2.append(4))
# print(list2.sort())  #ascending order me sort hoga
# print(list2)

# list2 = [5, 2, 9, 1, 7]
# list2.sort(reverse=True)  #descending order me sort hoga
# print(list2)

#    string sorting--alphabetically sorting hoga isme

# for ascending order

# list3 = ["banana", "apple", "cherry", "date"]
# list3.sort()
# print(list3)

# now for descending order

# list3 = ["banana", "apple", "cherry", "date"]
# list3.sort(reverse=True)
# print(list3)

# 3.>List Reversing

# list4 = [1, 2, 3, 4, 5]
# list4.reverse()  #ye list ke elements ko reverse order me print krega
# print(list4)

# 4.>List Inserting

# list5 = [1, 2, 3, 4, 5]
# list5.insert(2, 10)  #ye list ke 2nd index pr
# print(list5)

# 5>>List Removing

# list6 = [1, 2, 3, 4, 5]
# list6.remove(3)  #ye list ke 3rd element ko remove krega
# print(list6)

# 6.>List Popping

# list7 = [1, 2, 3, 4, 5]
# list7.pop(3)  #ye list ke 3rd index pr situated element ko remove krega
# print(list7)






# #####TUPLES IN PYTHON#####

# tuple1 = (1, 2, 3, 4, 5)
# print(tuple1)
# print(type(tuple1))
# print(tuple1[0])
# print(tuple1[1])

# tuple1[0] = 10  #ye error dega kyuki tuple immutable hote hai

# tup = () #empty tuple
# print(tup)
# print(type(tup))

# tup = (1) #ye tuple nhi hoga ye int hoga
# print(tup)
# print(type(tup))  #class int print hua

# tup = (1,) #ye tuple hoga
# print(tup)
# print(type(tup))  #class tuple print hoga
# string ho ya float ho ya int ho...tuple me different data types ke elements ho skte hai and single walo me last me comma zaroor dalna
# non singulars me last me comma dalna optional hai

# ###SLICING IN TUPLES####
# tup = (1, 2, 3, 4, 5)
# print(tup[1:4])  #ye 1 se 4 tak print krega but last element print nhi hoga
# print(tup[2:]) 

# #METHODS IN TUPLES

# 1.>Index Method

# tup1 = (1, 2, 3, 4, 5)
# print(tup1.index(3))  #ye 3 ka index print krega joki 2 hai

# 2.>Count Method

# tup2 = (1, 2, 3, 4, 5, 3, 3)
# print(tup2.count(3))  #ye 3 kitni baar tuple me hai

# ##QUESTIONS#######

# Q1.WAP to ask the user to enter names of their three favourite movies and store them in lists

# a = input("Enter the name of your first favourite movie:")
# b = input("Enter the name of your second favourite movie:")
# c = input("Enter the name of your third favourite movie:")

# list1 = [a, b, c]
# print("Your favourite movies are:", list1)

#         OR#

# movies = []
# movies.append(input("Enter 1st movie: "))
# movies.append(input("Enter 2nd movie: "))
# movies.append(input("Enter 3rd movie: "))

# print("Your favourite movies are:", movies)

# Q2. WAP to check if the list contains a palindrome of elements.

# list1 = [1,2,1]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")

# else:
#     print("NOT palindrome")   

#             ####ex-2####### 

# list1 = [1,2,3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")

# else:
#     print("NOT palindrome") 

# Q3> i.>WAP to count the no of students with the grade "A" in the following tuple.
#       ("C","D","A","A","B","B","A")
# SOln.
# tup = ("C","D","A","A","B","B","A")
# print(tup.count("A"))

#      ii.>Store the above values in a list and store them from "A" to "D"

# list=["C","D","A","A","B","B","A"]
# list.sort()
# print(list)

# ################################################LECTURE 3 OVERRRRRRRRRRRRR#################################################
