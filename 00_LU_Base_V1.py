import random

# Function go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes/no")


def instructions():
    statement_generator("How To Play", "*")
    print()
    print("Pick a number between 1 and 10")
    print()
    return""


def num_check(question, low, high):
    error = " Please enter an whole number between 1 and 10\n "

    valid = False
    while not valid:
        try:
            #   ask the question
            response = int(input(question))

            # if the amount is too low ? too high give
            if low < response <= high:
                return response

# output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here....
played_before = yes_no("Have you played the game before? ")

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

if played_before == "no":
    instructions()

# Ask user how much they want to play with...
how_much = num_check("How much would you"
                     " like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # id between 1 and 5
    # user gets a unicorn (add $4 to balance
    if 1 <= chosen_num <= 3:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4
        # if the random # is between 6 and 36
        # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1
        # The token is either a horse or zebra ....
        # in both cases, subtract $0.50 from the balance
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"
            # otherwise set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5
    outcome = "You got a {}. Your balance is " \
              "${:.2f}".format(chosen, balance)
    statement_generator(outcome, prize_decoration)

    if balance < 1:
        # If balance is to low, exit the game and
        # output a suitable message
            play_again = "xxx"
            print("Sorry you have run out of money ")
    else:
        play_again = input("Press enter to pay again or 'xxx' to quit")

    print()
print("Final balance is  ${:.2f}".format(balance))

