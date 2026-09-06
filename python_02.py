# str1 = "This is a string"
# str2 = 'Apnacollege'
# str3 = """This is a string"""
#use of commas^

#escape sequence characters 

# str1 = "This is a string. we are creating it in python."
# print(str1)

# str1 = "This is a string.\n we are creating it in python."
# print(str1)
# #\n is used to change line

# str1 = "This is a string.\t we are creating it in python."
# print(str1)
# #\t is used to give tab space

#operations on strings
#1. Concatenation-adding two strings

# str1 = "Apna"
# str2 = "College"

# print(str1+str2)

#2nd way
# str1 = "Apna"
# str2 = "College"
# finalstr = str1+str2
# print(finalstr)

#2. Lenght of str-len(str)

# str1 = "Apna"
# len1 = len(str1)
# print(len1)

# str2 = "College"
# len2 = len(str2)
# print(len2)

# finalstr = str1 + " " + str2 
# print(finalstr)
# print(len(finalstr))

#3.INDEXING IN PYHTON

#str = "apna College"

# print(str[0])
# print(str[1])
# print(str[3])
# print(str[6])
# print(str[4])

#indexing me chracter ko access kr skte hai 
# pr unhe manipulate nhi kr skte

#4. SLICING

# str = "apna College"
# print(str[1:4])
# print(str[0:4])
# print(str[5:12])
# print(str[1:len(str)])
# print(str[1:]) #[1:len(str)]
# print(str[:4]) #[0:4]
# print(str[5:len(str)])


    # NEGATIVE INDEX SLICING
       #Last ltter is -1...we start back indexing from -1

# str = "apple"
# print(str[-5:-1])
# print(str[-5:-2])
# print(str[-5:-3])
# print(str[-5:-4])

#OTHER STRING FUNTIONS 
 #1.ENDS WITH FUNCTION

# str= "I am studying python from ApnaCollege"
# print(str.endswith("ege"))
# print(str.endswith("app"))

  #2.CAPITALIZE FUNCTIONS

# str= "i am studying python from ApnaCollege"
# print(str.capitalize())
# print(str)
#purane wali string ko capitalize nhi krta


#to capitalize old string tooo we do the following
# str= "I am studying python from ApnaCollege"
# str = str.capitalize()
# print(str)

#3. REPLACE FUNCTION

# str = "I am studying python from ApnaCollege"
# print(str.replace("o", "a"))

# str = "I am studying python from ApnaCollege"
# print(str.replace("python", "javascript"))

  #4.FIND FUNNCTION
  #returns 1st index of 1st occurence
  
# str = "I am studying python from ApnaCollege"
# print(str.find("o"))
# print(str.find("from"))
# print(str.find("Q"))

  #COUNT FUNCTION

# str = "I am from studying python from ApnaCollege"
# print(str.count("from"))
# print(str.count("o"))
#from do bar hai toh 2 value aaega

##########QUESTIONS PRACTICE#########

#Q1 WAP to input user's first name and print its length
#SOL:
# a = (input("Fisrst Name:"))
# print("lenght of your name:", len(a))

#Q2 WAP tp find the occurence of '$' in string
#SOl:
# str = "He earn in $ in American $"
# print(str.count("$"))

####CONDITIONAL STATEMENTS In PYTHON###

# age = 16

# if(age>=18):
#     print("can vote & apply for license")
# else:print("not eligible")

# age = 24

# if(age>=18):
#     print("can vote & apply for license")
# else:print("not eligible")

# age = 34

# if(age>=18):
#     print("can vote")
#     print("can drive")
# else:print("not eligible")


# age = 16

# if(True):
#     print("can vote & apply for license")
# else:print("not eligible")

###ELIF OR ELSE IF CONDITIONS##

# light = "green"

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("wait")
# elif(light == "green"):
#     print("go")

# print("end of code")

# num = 5

# if(num > 2):
#     print("greater than 2")

# if(num > 3):
#     print("greater than 3")

#if me dono check krta hai dono true hai toh dono pr execute hoga 
 
# num = 5 

# if(num > 2):
#     print("greater than 2")

# elif(num > 3):
#     print("greater than 3")

# is bar if true hogya first me hi toh elif pr check nhi hua...age if false hota toh elif pr check hota

###use of else statement

# light = "blue"

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("wait")
# elif(light == "green"):
#     print("go")
# else:
#     print('light is broken")')

#another example of elsse sstatement

# age = 14

# if(age >= 18):
#     print("can vote")
# else:
#     print("CANNOT vote")


# marks = 74

# if(marks >= 90):
#     grade = "A"
# elif(marks >=80 and marks < 90):
#     grade = "B"
# elif(marks >=70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of the student-->", grade)

#now to take marks as input from the user

# marks = int(input("Enter the marks of the student: "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >=80 and marks < 90):
#     grade = "B"
# elif(marks >=70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of the student-->", grade)

###NESTING####

# age = 95
# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")

# else:
#     print("cannot drive")   


####PRACTICE QUESTIONS####

#Q1.-->WAP to check if a number entered by the user is odd or even.

# num = int(input("enter number: "))

# rem = num % 2

# if (rem == 0):
#     print("EVEN")
# else:
#     print("ODD")

          ####OR####

# num = int(input("enter number: "))

# if (num % 2 == 0):
#     print("EVEN")
# else:
#     print("ODD")

#Q2. WAP to find the greatest of three numbers enterd by the user.
#SOLn-->
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))

# if (a >= b) and (a >= c):
#     print("greatest number is:", a)
# elif (b >= a) and (b >= c):
#     print("greatest number is:", b)
# else:
#     print("greatest number is:", c)
    

# Q3. WAP to check if a no. is a multiple of 7 or not.

# x = int(input("enter number: "))

# if (x % 7 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")

##################################################LECTURE 2 OVER################################################








    




