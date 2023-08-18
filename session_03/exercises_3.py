# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".

name = input("What is your name? ")
if name == "Bob":
  print("Welcome Bob!")

# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".

name = input("What is your name? ")
if not name == "Alice":
  print("You're not Alice!")

# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".

password = input("What is your password? ")
if password == "querty123":
  print("You have successfully logged in")
else: 
  print("Password failure")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".

number = int(input("Enter a number? "))
if number % 2 == 0:
  print(str(number) + "is Even")
else: 
  print(str(number) + "is Odd")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"

number_1 = int(input("Enter a number? "))
number_2 = int(input("Enter a number? "))

if number_1 + number_2 > 21:
  print("Bust")
else:
  print("Safe")

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.

length = int(input("Enter a length "))
width = int(input("Enter a width "))

if length == width:
  print("It is a square")
else:
  print("It is not a square")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

salary = int(input("What is your current salary? "))
years_of_service = int(input("What is your current years of service? "))

if years_of_service > 3:
  print(str(salary) + str(salary*0.1))
else:
  print("No bonus")  

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
x = int(input("Enter a number "))
if x > 0:
  print(x ** 3)
else:
  print(x/2)


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".

name = input("What is your name? ")

if name == "Alice":
  print("Hello, Alice")
elif name == "Bob":
  print("You're not Bob! I'm Bob")
else: 
  print("You must be Charlie")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

age = int(input("What is your age? "))

if age == 0:
  print("You're not born yet!")
elif age < 11:
  print("You're too young to go to this school") 
elif 11<age<16:
  print("You can can come to this school")
elif age>16:
  print("You're too old for school")
else: 
  print("You're not born yet")

# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".

month = input("Enter a month ")

if month == "March" or "April" or "May":
  print(month + " is in Spring")
else: 
  print("I don't know")

if month == "June" or "July" or "August":
  print(month + " is in Summer")
else: 
  print("I don't know")

if month == "September" or "October" or "November":
  print(month + " is in Autumn")
else: 
  print("I don't know")

if month == "December" or "January" or "February":
  print(month + " is in Winter")
else: 
  print("I don't know")

# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

number_1 = int(input("Enter a number "))
number_2 = int(input("Enter a number "))

if number_1 % 2 == 0 and number_2 % 2 == 0:
  print("Even")
elif number_1 % 2 != 0 and number_2 % 2 != 0:
  print("Odd")
else:
  print(str(number_1*number_2))

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.

number_1 = int(input("Enter a number "))
number_2 = int(input("Enter a number "))

if number_1>number_2:
  print(number_1)
else:
  print(number_2)

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

salary = int(input("What is your current salary? "))
years_of_service = int(input("What is your current years of service? "))

if years_of_service > 5:
  print(str(salary) + str(salary*0.15))
elif 3 < years_of_service >= 5:
  print(str(salary) + str(salary*0.10)))
else:
  print("No bonus")

# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.

age_1 = int(input("What is your age? "))
age_2 = int(input("What is your age? "))
age_3 = int(input("What is your age? "))
name_1 = input("What is your name? ")
name_2 = input("What is your name? ")
name_3 = input("What is your name? ")

if age_1>age_2>age_3:
  print(name_1 + " is the oldest and " + name_3 + "is the youngest")
elif age_1>age_3>age_2:
  print(name_1 + " is the oldest and " + name_2 + "is the youngest")
elif age_2>age_1>age_3:
print(name_2 + " is the oldest and " + name_3 + "is the youngest")
elif age_2>age_3>age_1:
print(name_2 + " is the oldest and " + name_1 + "is the youngest")
elif age_3>age_1>age_2:
print(name_3 + " is the oldest and " + name_2 + "is the youngest")
elif age_3>age_2>age_1:
print(name_3 + " is the oldest and " + name_1 + "is the youngest")
else age_3 == age_2 == age_1:
print("All three ages are the same")

# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lesson = input("What is the lesson? ")
mark_1 = int(input("What is your mark? "))
mark_2 = int(input("What is your mark? "))
mark_3 = int(input("What is your mark? "))

if mark_1<25:
  print("F")
elif 25 <= mark_1 < 45:
  print("E")
elif 45 <= mark_1 < 50:
  print("D")
elif 50 <= mark_1 < 60:
  print("C")  
elif 60 <= mark_1 < 80:
  print("B")
else:
  print("A")

if mark_2<25:
  print("F")
elif 25 <= mark_2 < 45:
  print("E")
elif 45 <= mark_2 < 50:
  print("D")
elif 50 <= mark_2 < 60:
  print("C")  
elif 60 <= mark_2 < 80:
  print("B")
else:
  print("A")

if mark_3<25:
  print("F")
elif 25 <= mark_3 < 45:
  print("E")
elif 45 <= mark_3 < 50:
  print("D")
elif 50 <= mark_3 < 60:
  print("C")  
elif 60 <= mark_3 < 80:
  print("B")
else:
  print("A")