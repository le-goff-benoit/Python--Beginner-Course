# coding: utf-8

# Simple variables attributions
character_name = "Benoit \nLe Goff"
character_age = 25

# Data type for strings in Python
print(character_name)

# Classic str manipulation
city_name = "oslo"
city_name.capitalize()
print(city_name.capitalize())

# Classic list manipulation
city_people = ['Benoit', 'Cosette', 'Albert']
print(city_people)
print(city_people[0])

# For loop to display the list
for i in range(len(city_people)):
    print('Person ' + str(i + 1) + ': ' + city_people[i])

# Create a function to display a list
def displayList(list):
    for i in range(len(list)):
        print('Item: ' + str(i + 1) + ': ' + list[i])


displayList(city_people)

# Fundamental Data Structure in Python
tel_person = {'Benoit': '077 269 00 48', 'Cosette': '077 269 18 10', 'Albert': '058 200 25 00'}
print(tel_person['Benoit'])

for tel in tel_person:
    print(tel_person[tel])