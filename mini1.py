# Intro to Python Mini Project 1

from random import randrange

def name_to_number(name):
# Convert name to a number
    if(name == 'rock'):
        choice = 0
    elif(name == 'Spock'):
        choice = 1
    elif(name == 'paper'):
        choice = 2
    elif(name == 'lizard'):
        choice = 3
    elif(name == 'scissors'):
        choice = 4
    else:
        message = "That is not a valid choice.  Valid choices are {'rock', 'Spock', 'paper', 'lizard', 'scissors'}."
        print message

    return choice



def number_to_name(number):
# Convert a number to a name
    if(number == 0):
        name = 'rock'
    elif(number == 1):
        name = 'Spock'
    elif(number == 2):
        name = 'paper'
    elif(number == 3):
        name = 'lizard'
    elif(number == 4):
        name = 'scissors'
    else:
        message = "That is not a valid choice.  Valid choices are integers in the range {0-4}."
        print message

    return name


def rspls(player_choice):
# Main function for the application.  Calls helper functions name_to_number and number_to_name.
    print "\n"
    print "Player chooses " + player_choice + "."
    
    player_num = name_to_number(player_choice)
    
    #comp_number = random.randrange(0, 5, 1)
    comp_number = randrange(0, 5, 1)
    print comp_number
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice + "."

    difference = (player_num - comp_number) % 5

    if(difference == 0):
        message = "It's a tie!"
    elif(difference == 1 or difference == 2):
        message = "Player wins!"
    elif(difference == 3 or difference == 4):
        message = "Computer wins!"
    else:
        message = "That's an error!"

    print message
