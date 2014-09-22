# Intro to Python Mini Project 1
# This project simulates a game of Rock Spock Paper Lizard Scissors (RSPLS)


from random import randrange

def name_to_number(name):
# Convert rspls name to a number
# Input = name, output = the corresponding numeric code.
# The only valid values for name are in the set:
# {'rock', 'Spock', 'paper', 'lizard', 'scissors'}

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
# Convert a number to a rspls name
# Input = number, output = name
# The only valid values are [0,4]
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
        message = "That is not a valid choice.  Valid choices are integers in the range [0, 4]."
        print message

    return name


def rspls(player_choice):
# Main function for the application.  Calls helper 
# functions name_to_number and number_to_name.
# Input = player_choice, output = None

    print "" # create a line of white
    print "Player chooses " + player_choice + "."
    
    player_num = name_to_number(player_choice)
    
    comp_number = randrange(0, 5, 1)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice + "."

    # Compute the winner.  If the value of difference
    # is a 1 or a 2, then the player wins.  If the value of
    # difference is 3 or 4, then the computer wins.  If the
    # value of difference equals 0, then it's a tie.
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

    
# Sample output.
rspls('rock')
rspls('Spock')
rspls('paper')
rspls('lizard')
rspls('scissors')
