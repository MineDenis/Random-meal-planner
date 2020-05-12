#!/usr/bin/python3

import sys
import requests
import json

# This program will use an Existing api to recieve a random meal, I will extract the name and the instructions to the dish
# I originally wanted to make this in alexa, I then decided to do it in python, understand json and requests better,
# and then redo it as an alexa skill.

def main():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    meal = response.json()

    # This sets the name of the dish and the instructions to a variable.
    meal, instr= meal['meals'][0]['strMeal'], meal['meals'][0]['strInstructions'];
    
    # I print the dish name firstly followed by a question.
    print(meal)
    
    print('Would you like to learn how to make this meal ? Y/N')
    
    # The user responds with either yes or no, or anything else.
    answer = input()
    
    #To prevent mixture in caps, I decided to make the input upper.
    if answer.upper() == 'Y':
        print(instr)
    #If it enters the if statement it will output the instructions if not, nothing will happen.

if __name__ == '__main__':
    main()
