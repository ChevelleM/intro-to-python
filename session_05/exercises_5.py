# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.

import random
for i in range(1,10):
  print(random.randint(1,100))

# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .

guess = None
while guess != 7:
  guess = int(input("Enter a number "))
print("Wow lucky number 7!")

#guess = None
#while guess != random.randint(1,10):
  #guess = int(input("Enter a number "))
#print("Wow lucky number!")

# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.

width = int(input("Enter a width "))
height = int(input("Enter a height "))
area = width*height
print(str(width) + "cm x " + str(height) + "cm = " + str(area) +"cm2 = " + str(round(area/10000)) + "m2")

# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".

password_input = input("What is your password? ")
password = "qwerty123"

guesses = 0 
while guesses<2:
  if password_input == password:
    print("You have successfully logged in")
    break
  else: 
    print("Password failure")
    password_input = input("What is your password? ")
    guesses += 1

if guesses == 2:
  print("System Locked!")

# 5. Add up all the numbers from 1 to 500 and print the answer.

total = 0 
for x in range(1,501):
  total += x
print(total)

# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.

print("Pick 10 numbers, one of those numbers must be 99")

list = []
for i in range(1,10):
  numbers = int(input("Pick a number: "))
  list.append(numbers)

print(list.index(99))
  
# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36

for x in range(1,16):
  print(str(x) + " x 18 = " + str(x*18))

# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.

x=1
while x<=100:
  print(x, end=' ')
  x += 1
  
# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.



# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name



# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games
