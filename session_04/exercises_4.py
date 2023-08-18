# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.

fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(fruits)

# 2. Add "Grapes" to the list and print the list.

fruits.append("Grapes")
print(fruits)

# 3. Change "Pears" to "Strawberries" and print the list.

fruits[2] = "Strawberries"
print(fruits)

# 4. Remove "Apples" from the list and print the list.

del fruits[0]
print(fruits)

# 5. Print out the current length of the list.

print(len(fruits))

# 6. Order the list alphabetically.

fruits.sort()

# 7. Print out the list again.

print(fruits)


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.

for fruit in fruits:
  print(fruit)

# 2. Print the numbers 1 to 100 (including the number 100).

for number in range(1,101):
  print(number)

# 3. Print all odd numbers from 1 to 100.

for i in range(1,101,2):
  print(i)

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).

not_held = [1916, 1940, 1944, 2020]
for olympics_year in range(1896, 2023, 4):
  if olympics_year not in not_held
  print(olympics_year)

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.

numbers = [3,55,74,89,18,24,30,9,92,43]
even_count = 0
odd_count = 0

for i in numbers:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
         odd_count = odd_count + 1

print("This list has " + str(even_count) + " even numbers and " + str(odd_count) + " odd numbers.")

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.

names = ["Alice", "Bob", "Charlie", "Dave", "Ellen"]
for name in names:
  print("Hello " + name)

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".

word = "supercalifragilisticexpialidocious"
for letter in word:
  print(letter)

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.

numbers = [1,2,3,4,5]
sq_numbers = []
for number in numbers:
  sq_numbers.append(number*number)

print(sq_numbers)

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.

names = ["Alice", "Bob", "Charlie", "Dave", "Ellen"]
dr_names = []
for name in names:
  dr_names.append("Dr. " + name)

print(dr_names)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```

x = range(0,101)
for number in x:
  if (number % 3 == 0) and (number % 5 == 0):
    print("Fizzbuzz")
  elif (number % 3 == 0):
    print("Fizz")
  elif (number % 5 == 0):
    print("Buzz")
  else:
    print(number)