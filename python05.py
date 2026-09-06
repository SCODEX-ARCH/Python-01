count = 1      #iterator
# while count <= 5:
#     print ("hello")
#     count += 1

# print(count)

# i = 1
# while i <= 5:  #yaha 100 1000000 kitna bhhi value daalkr printkarwa skte hai
#     print("apnacollege")
#     i+=1

# for printing the count or the nos alongside every string we do a slight tchange and print i tooo 

# i = 1
# while i <= 5:  #yaha 100 1000000 kitna bhhi value daalkr printkarwa skte hai
#     print("apnacollege",i)
#     i+=1  

# for printing integers rather than strings
# i = 1
# while i <= 5:  
#     print(i)
#     i+=1 
# print("loopended")       

# #For backward output
# i=5
# while i >=1:
#     print(i)
#     i-=1
# print("Loop Ended")   

# Questions on loop#-----------

# Q1. Print numbers from 1 t 100

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# Q2. Print numbers from 100 to 1

# i = 100
# while i >= 1:
#     print(i)
#     i -=1

# Q3. Print the multiplicaton table of a number n.

# i = 1
# while i <= 10:
#     print(3*i)
#     i += 1
#      ###OR#####
# i = 3
# while i <= 30:
#     print(i)
#     i += 3
# for doing the same(obtaining table) for any other number while taking input from the user...just do the following

# n = int(input("enter number: "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# Q4.Print the elements of the following list using a loop:
# i.[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Ans-
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(nums[0])#ye bar bar likhne ke bajay ham loop banaenge
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1
# ii.
# heroes = ["ironman", "thor", "batman", "superman"]

# i = 0
# while idx < len(heroes):
#     print(heroes[i])
#     i += 1
# ###iss tarike se list ya tuple ke ek ek item ke upr jana is known as traversing(traverse)

# Q5. Search for a number x in this tuple using loop.
#     (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# Ans-



# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36

# i=0
# while i < len(nums):
#      if(nums[i] == x):
#         print("FOUND at idx", i)
        
#      i += 1
#      #OR###we can do this also
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# x = 36
# i=0
# while i < len(nums):
#      if(nums[i] == x):
#         print("FOUND at idx", i)
#      else:
#          print("FINDING")   
#      i += 1

# ###some more imp keywords in while loop
# BREAK AND CONTINUE 
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# print("end of loop")

# ####OR####we can use it here also
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# x = 36
# i=0
# while i < len(nums):
#      if(nums[i] == x):
#         print("FOUND at idx", i)
#         break
#      else:
#          print("FINDING")   
#      i += 1

# IInd Keyword--Continue-it is used to skip

# i = 0
# while i <= 5:
#      if(i == 3):
#         i += 1
#         continue #skip
#      print(i)
#      i += 1
# Q. For printing only odd nos.

# i = 0
# while i <= 10:
#      if(i % 2 == 0):
#         i += 1
#         continue #skip
#      print(i)
#      i += 1

# #FOR LOOPS-- It is used for sequential traversing
# nums = [1, 2, 3, 4, 5]

# for val in nums:
#     print(val)

# veggies = ["brinjal", "ladyfinger", "cauliflower", "potato"]

# for val in veggies:
#     print(val)

# tup = (1, 2, 4, 3, 5)   

# for val in tup:
#     print(val) 

# toh generLLY agr hame kisi iterator ke upr kaam krna hai yani hamare pas koi variable hai jiski value ko ham update kr rhe hai ya fir hamare pas koi stopping condition hai toh wo sare kam ham while loop se krenge
# aur agr hame kisi data type ke upr traverse krna hai jaise tuple ho gya koi list hogyi koi string ho gyi toh uske ;iye ham for loop ka istemal krenge 

# str ka ek ex-
# str = "apnacollege"

# for char in str:
#     print(char)
# else:
#     print("loop ended") 
#     ##ye same loop ended ham log directly bhi print("loop ended") se print krwa skte the prrr else ka kya kam....else ka kam ye hai ki agr loop normal terminate ho gya toh else execute hoga aur agr loop break se terminate ho gya toh else execute nhi hoga

# str = "apnacollege"

# for char in str:
#      if(char == "o"):
#           print("o found")
#           break
#      print(char)
# else:
#      print("loop ended") 

# ###QUESTIONS related to for loop

# Q1.Print the elementss of the following list using a loop:
#   [1,4,9,16,25,36,49,64,81,100]
# Ans-
# nums = [1,4,9,16,25,36,49,64,81,100]
# for val in nums:
#      print(val) 

# Q2.Search for a number x in the tuple using for loop.
# [1,4,9,16,25,36,49,64,81,100]
# Ans--TAKE IN NOTICE THAT THIS METHOD OF SEARCHING FOR A VALUE IS CALLED "LINEAR SEARCH" IN PROGRAMMING

# nums = (1,4,9,16,25,36,49,64,81,100,36)
# x = 36

# idx = 0
# for val in nums:
#     if(val == x):
#         print("FOUND AT IDX",idx)
#         break
#     idx += 1

# ##>RANGE() FUNCTION- It is used to return a sequence of nos...starting from 0 by default and increments by 1 by default, and stops before a specified number.

# seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])

# print(range(5))

# isi seq ke upr loop chalane ke liye
# seq = range(10)

# for i in seq:
#      print(i)
#      #OR##

# for i in range(10):
#      print(i)

# START STOP & STEP in range function...start and step is optional while stop is compulsory

# for i in range(10):  #range(stop)
#      print(i)

# for i in range(2, 10):  #range(start, stop)
#      print(i)


# for i in range(2, 10, 2):  #range(start, stop, step)--isme start 2 se hoga and end 10 pe hoga prr stepside value 2 hone ke wajah se values 2 se increase kregi
#      print(i)  


# Q-Print all even nos from 1 to 100 using range and for loop method
# Ans-
# for i in range(2, 101, 2):
#     print(i)

# ######QUESTIONS######
# Q1. Print numbers from 1 to 100.

# for i in range(1, 101):
#     print(i)

# Q2. Print nos from 100 to 1.

# for i in range(100, 0, -1):
#     print(i)  

# Q3. Print the multiplication of a number n.
# Let the no n be 4

# for i in range(4, 41, 4):
#     print(i) 
#     OR- we can do it by taking input from the user

# n = int(input("enter number:"))

# for i in range(1, 11):
#     print(n * i)

# #PASS Statement

# for i in range(5):
#     #empty

# print("some useful work")  #this will give error because under the loop no command is given...so we will do this instead

# for i in range(5):
#     pass

# print("some useful work")

# also we can use pass statemnt in if statement

# if i > 5:
#     pass   
 
# Questions..............
# 1. WAP to find the sum of first n numbers. (using while)

# n = 7

# sum = 0
# for i in range(1, n+1):
#     sum += i
#     print(i)

# print("Total sum is equal to", sum)

#       Using while loop

# n = 7
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1 

# print("Total sum =", sum) 

# Q2. WAP to find the factorial of first n numbers.

# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1 

# print("Factorial =", fact)  

#    ##For doing the same job from for loop- 

# n = 5
# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print("Factorial=", fact)   

# ######THE END OF LECTURE############
