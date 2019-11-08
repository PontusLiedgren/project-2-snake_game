# project-2-passwordgenerator
#
# Author: Pontus Liedgren
# https://github.com/PontusLiedgren/project-2-passwordgenerator


# Password generator

import random
print("Välkommen till lösenordsgeneratorn!\n")

name_input = input("Säg ditt namn: ")
birth_input = input("Säg ditt födelsedatum(ååååmmdd): ")
interest_input = input("Säg något intresse: ")
# password_list = [name_input, birth_input, interest_input]

def password(first_name_input, date_of_birth_input, personal_interest_input):
    print(first_name_input[2], first_name_input[0].upper(), str(date_of_birth_input) [1], str(date_of_birth_input) [6], personal_interest_input[1].upper())

password(name_input, birth_input, interest_input)


