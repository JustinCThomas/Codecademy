"""
This program generates passages that are generated in mad-lib format
Author: JCT (start-off code comes from Codecademy) 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print ("Mad Libs has officially STARTED!!!")


name = raw_input("Enter a name: ")
adjective_1 = raw_input("Enter adjective 1 please: ")
adjective_2 = raw_input("Enter adjective 2 please: ")
adjective_3 = raw_input("Enter adjective 3 please: ")

verb = raw_input("Please enter a verb: ")
noun_1 = raw_input("Please enter noun 1: ")
noun_2 = raw_input("Please enter noun 2: ")

animal = raw_input("Enter a name of an animal please: ")
food = raw_input("Enter a name of a food please: ")
fruit = raw_input("Enter a name of a fruit please: ")
superhero = raw_input("Enter a name of a superhero please: ")
country = raw_input("Enter a name of a country please: ")
dessert = raw_input("Enter a name of a dessert please: ")
year = raw_input("Enter a year please: ")


print(STORY) % (name, adjective_1, adjective_2, animal, food, verb, noun_1, fruit, adjective_3, name, superhero, name, country, name, dessert, name, year, noun_2)
















