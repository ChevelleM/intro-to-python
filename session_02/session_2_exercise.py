width = 6
height = 5
area = width*height
print("Rectangle of width" + str(width) "and height" + str(height) + "has an area of" + str(area))

print(len("python"))

print("python"[0,2])

name = input("What is your name? ")
print("Hello, " + name)

current_age = int(input("How old are you? "))
age_in_15_years_time = current_age + 15
print("In 15 years time you will be: " + str(age_in_15_years_time))

print("Hello, " + name+ ", you are currently " + str(current_age) + "years old. In 15 years time you will be " + str(age_in_15_years_time))

hometown = input("What is your hometown? ")
print(hometown.upper())

colour = input("What is your favourite colour? ")
print(len(colour))

month = input("The month is ")
weather= input("The weather is ")
print("It is " + month + " and it is " + weather + " today")

month = input("What month is it? ")
temp1 = int(input("What was the temperature on Monday? "))
temp2 = int(input("What was the temperature on Tuesday? "))
temp3 = int(input("What was the temperature on Wednesday? "))
temp4 = int(input("What was the temperature on Thursday? "))
temp5 = int(input("What was the temperature on Friday ? "))
average_temp = (temp1 + temp2 + temp3 + temp4 + temp5)/5
print("It is " + month + " and the average temperature is " + str(average_temperature) + "degrees celsius")

print("It is " + month.upper() + " and the average temperature is " + str(average_temperature) + "degrees celsius")

favourite_animals = "My favourite animals:\n\tCats,\n\tDogs,\n\tTigers"

name = input("What is your name? ")
number = int(input("Pick a number? "))
print(name[number].upper())

str = "WelcometoPython"
print(len(str))
print(str[1:14:2])