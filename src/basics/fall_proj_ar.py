from math import *
from random import *
from time import *


# define a dictionary of choices
# [USER OPTION] = PROGRAM RESULT
options = {'1) Dice Roll': "diceroll",
           '2) Coin Flips': "coinflips",
           '3) Lottery': "lottery",
           '4) Slot Machine': "slotmachine",
           '5) Player Game': "playergame",
           '6) Riddle': "riddle",
           '7) Peppermint Jar Game': "pprmntjargame",
           '8) Exit': "exit"}


# Let user select an exercise
option = select_from_dict(options, 'option')

def select_from_dict(choices, name):
    index = 0
    index_valid_list = []
    print('Welcome to the Random Number Game')

    for optionName in choices:
        index = index + 1
        index_valid_list.extend([choices[optionName]])
        print(str(index) + ') ' + optionName)
    input_valid = False
    while not input_valid:
        input_raw = input(name + ': ')
        input_no = int(input_raw) - 1
        if input_no > -1 and input_no < len(index_valid_list):
            selected = index_valid_list[input_no]
            print('Selected ' +  name + ': ' + str(selected))
            if "diceroll" == selected:
                try_dice_roll()
            elif "coinflips" == selected:
                try_coin_flips()
            elif "lottery" == selected:
                try_lottery()
            elif "slotmachine" == selected:
                try_slot_machine()
            elif "playergame" == selected:
                try_player_game()
            elif "pprmntjargame" == selected:
                try_exercise06()
            elif "exit" == selected:
                try_exercise07()
            else:
                print("we dont have this problem ready yet")

            # here call appropriate exercise-function
            retry = input("want to retry any problems? y/n: ").lower()
            if "y" == retry:
                input_valid = False
            else:
                input_valid = True
                break
        else:
            print('Please select a valid ' + name + ' number')
    return selected

def try_dice_roll():
    print('You have a Dice with 6 sides.')
    print('Type roll to make the dice roll. ')
    you = eval(input('Enter what you think is the number shown on the dice: '))

    comp = randint(1, 6)
    if comp == you:
        print('Great job! You guessed it correctly!!\n')
    else:
        print('Sorry mate, the answer was', comp, '.\n')
    pass

def try_coin_flips():
    print('You have a coin with two sides, heads and tails. You flip it.')
    coin = input('Now guess. Is the coin showing a head or tail? Type 1 for head, 2 for tail: ')
    print()
    comp = randint(1, 2)
    if coin == comp:
        print('Great job! You are now a president with a tail!\n')
    else:
        print('Whoops, the answer was', comp, '.\n')
    pass

# Menu
choice = 0
    # Enter choice
    choice = eval(input('Enter a choice from 1 to 8: '))
    # Test choice
    if choice == 1:
        # Dice Roll
    if choice == 2:
        # Coin Flips
    if choice == 3:
        # Lottery
        print(
            'You have entered THE LOTTERY. You have a various numbers to choose from. Your goal is to LITERALLY gues the right number.')
        print()
        ticket = input('Enter a number from 1 to 10: ')
        from random import *

        lottery = randint(1, 10)
        if ticket == lottery:
            print('You won the lottery!! WE THE BEST!')
            print()
        else:
            print('Better luck next time...  ;(')
            print()

    if choice == 4:
        # Slot Machine
        print(
            'Let us play the slot machine today! The range of numbers to guess from will be, 1 through 4. You have 3 guesses in which all three should match.')
        from random import *

        number1 = randint(1, 4)
        number2 = randint(1, 4)
        number3 = randint(1, 4)
        user_value = input('Press enter to generate values: ')
        print(number1, '', number2, '', number3)
        if number1 == number2 and number2 == number3:
            print('Great Job!! You won the game!')
            print()
            break
        else:
            print('You lost this round. Sorry mate...')
            print()
        break
    if choice == 5:
        # Slot Machine
        print('You have selected the Athlete Game.')
        print(
            'Your choice and the computers choice should be the same. There are 5 rounds. The following players are listed: ')
        for i in range(5):
            print('1. Lawrence Taylor ')
            print('2. Ian Thorpe')
            print('3. Roger Federer')
            print('4. Nick Kyrgios')
            print('5. Sachin Tendulkar')
            print('6. Thomas Bryant')
            print('7. Stephen Curry')
            print('8. Kobe Bryant')
            print('9. Giannis Antetokuonmpo')
            print('10. Jerry Rice')
            user = input('Choose one out of the ten: ')
            print()
            from random import *
            import time

            timepast = 10
            start = time.time()
            while timepast <= 20 and timepast >= 10:
                comp3 = randint(6, 10)
                user2 = print('The computer chose', comp3, '.')
                decision = print('Would', user, 'win a basketball game, or', user2, '?')
                if user == user2:
                    print('Thats right!')
                    print()
                else:
                    print('Try again.')
                    print()

                print('Remember, you chose', user, '.')
                comp4 = randint(3, 5)
                user3 = print('Choose between', user, 'and', comp4,
                              '. Which one do you think will win a baseball game? ')
                if user3 == randint(3, 5):
                    print('Break a leg! YOU GOT IT!!')
                    print()
                else:
                    print('Try again!')
                    print()
                print('Remember, you chose', user, '.')
                comp5 = randint(1, 10)
                user4 = print('Choose between', user, 'and', comp5, '. Which one do you think will win a 100m dash? ')
                if user4 == randint(1, 10):
                    print('You finished the race!')
                    print()
                else:
                    print('Great attempt!')
                    print()
                    break
            timepast = time.time() - start
    if choice == 6:
        # Riddle
        print('You have selected Riddle. There are two rounds.')
        for i in range(2):
            riddle = input('Choose Riddles 1, 2, 3, 4, 5, or 6: ')
            if riddle == '1':
                rid1 = input('What goes up but never goes down? ')
                print()
                if rid1 == 'age':
                    print('You got it!')
                    print()
                else:
                    print('Try again..')
                    print()
            if riddle == '2':
                rid2 = input('I go on red, but I stop on green. What am I doing? ')
                if rid2 == 'Eating a watermelon':
                    print('Great!!')
                    print()
                else:
                    print('No, it is eating a watermelon.')
                    print()
            if riddle == '3':
                rid3 = input(
                    'I can fly but have no wings. I can cry but I have no eyes. Wherever I go, darkness follows me. What am I? ')
                if rid3 == 'Clouds':
                    print('Got it!')
                    print()
                else:
                    print('Nope..')
                    print()
            if riddle == '4':
                rid4 = input('What letter of the alphabet has the most water? ')
                if rid4 == 'The letter c':
                    print('You got it!')
                else:
                    print('Just keep swimming!')
            if riddle == '5':
                rid5 = input('I break but never fall. And I fall but never break. What am I? ')
                if rid5 == 'Day and night':
                    print('Great job!')
                else:
                    print('Its hard, but still keep trying!')
            if riddle == '6':
                print('Haha, got you! There is no riddle 6!!')
                print()
        break
    if choice == 7:
        # Peppermint Jar Game
        print(
            'You have decided to play the Peppermint Jar Game. In this game, it is your job to guess the number of peppermints in the given jar. Know that you can use a calculator')
        print('Good Luck!!!!!')
        from math import *
        from random import *

        jar_radius = randint(10, 14)
        jar_height = randint(18, 28)
        candy_length = randint(2, 3)
        candy_width = randint(2, 3)
        candy_height = randint(2, 3)
        jar_volume = pi * ((jar_radius) ** 2) * jar_height
        candy_volume = candy_length * candy_width * candy_height
        print()
        print('The jar has a volume of', jar_volume,
              'centimeters cubed, and the peppermint candy has a volume of about', candy_volume,
              'centimeters cubed. Calculate using the full values given, including the ones after the decimal.')
        print()
        candy_number = jar_volume / candy_volume
        user_choice = eval(input('How many peppermint candies would fit into this jar? '))
        print()
        if user_choice == candy_number and candy_number - 1:
            print('GREAT!!!!! You cracked it!!')
            print()
        else:
            print('You minted it!! The answer was', candy_number, 'candies.')
            print()

    if choice == 8:
        # Exit
        import time

        timepast = 3
        start = time.time()
        while timepast <= 2:
            print('Good Bye, and farewell! I hope for you to join again soon!')
            print('You are going to exit the Game Menu.')
        timepast = time.time() - start
