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

lesson = input("What is the lesson? ")

total = 0
gradeCount = 0

while gradeCount < 3:
    grade = int(input("What is your mark? "))

    if grade < 0 or grade > 100:
        print("It should be a number from 0 to 100")
    else:
      gradeCount += 1
      total += grade
        
    if grade<25:
      print("F") 
    elif 25 <= grade < 45:
      print("E")
    elif 45 <= grade < 50:
      print("D")
    elif 50 <= grade < 60:
      print("C")
    elif 60 <= grade < 80:
      print("B")
    else:
      print("A")

# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name

import random
prize_draw_list = []
user_input = None

while user_input != "":
    user_input = input("Please input your name to be added to the prize draw:\n")
    if user_input != "":
        prize_draw_list.append(user_input)
 
print("Congratulations! " + random.choice(prize_draw_list) + " you are the winner of the prize draw!")

# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games

import random

print("Welcome to Rock, Paper, Scissors")

user_score = 0
computer_score = 0
turns = 0

while turns < 3:
  user_choice = input("What is your move? (rock, paper, scissors) ")
  computer_choice = random.choice(["rock", "paper", "scissors"])
  print("You picked " + user_choice)
  print("The computer picked " + computer_choice)
  turns += 1
  print("This is turn: " + str(turns))
  if user_choice == "rock":
      if computer_choice == "scissors":
          print("You Win")
          user_score += 1
      elif computer_choice == "paper":
          print("You Lose")
          computer_score += 1
      else:
          print("It's a draw")
  elif user_choice == "paper":
      if computer_choice == "rock":
          print("You Win")
          user_score += 1
      elif computer_choice == "scissors":
          print("You Lose")
          computer_score += 1
      else:
          print("It's a draw")
  else:
      if computer_choice == "paper":
          print("You Win")
          user_score += 1
      elif computer_choice == "rock":
          print("You Lose")
          computer_score += 1
      else:
          print("It's a draw")

print("Game Over! Final Score: User Score: " + str(user_score) + "\n Computer Score: " + str(computer_score))