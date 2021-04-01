import random

def main():
    """ Function that runs the game "Camel" """
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_traveled = -20
    drinks_in_canteen = 3
    forward = 0

    # Prints welcome screen
    print('Welcome to Camel!')
    print('You have stolen a camel to make your way across the great Mobi Desert.')
    print('The natives want their camel back and are chasing you down!')
    print('Survive your desert trek and out run the natives.')
    print()

    done = False
    while not done:
        # Prints all the players choices
        print('A. Drink from your canteen.')
        print('B. Ahead moderate speed.')
        print('C. Ahead full speed.')
        print('D. Stop for the night.')
        print('E. Status check.')
        print('Q. Quit.')
        print()

        choice = input('What is your choice? ')
        print()
        
        # Player wants to quit
        if choice.upper() == 'Q':
            done = True
            print('You quit the game! To play again you have to restart the game.')
        
        # Player wants to get status
        elif choice.upper() == 'E':
            print(f'Miles traveled:  {miles_traveled}')
            print(f'Drinks in canteen:  {drinks_in_canteen}')
            print(f'The natives are {miles_traveled - natives_traveled} miles behind you.')
        
        # Player wants to rest for a day
        elif choice.upper() == 'D':
            camel_tiredness = 0
            natives_traveled += random.randint(7, 14)
            print('The camel feels happy and well rested')
        
        # Player wants to move at full speed
        elif choice.upper() == 'C':
            forward = random.randint(10, 20)
            miles_traveled += forward
            thirst += 1
            camel_tiredness += random.randint(1, 3)
            natives_traveled += random.randint(7, 14)
            print(f'You traveled {forward} miles.')
        
        # Player wants to move ahead at moderate speed
        elif choice.upper() == 'B':
            forward = random.randint(5, 12)
            miles_traveled += forward
            thirst += 1
            camel_tiredness += 1
            natives_traveled += random.randint(7, 14)
            print(f'You traveled {forward} miles.')
        
        # Player wants to drink from canteen
        elif choice.upper() == 'A':
            if drinks_in_canteen > 0:
                thirst = 0
                drinks_in_canteen -= 1
                print(f'You drink from the canteen and feel refreshed.')
            else:
                print('No more drinks left!')
        
        # Player gets lucky and find an Oasis
        if done == False and (choice.upper() == 'B' or choice.upper() == 'C'):
            if random.randint(1, 20) == 1:
                thirst = 0
                camel_tiredness = 0
                drinks_in_canteen = 3
                print('You found an oasis!')
                print('Your canteen has been refilled,')
                print('your camel is fully rested,')
                print('and you are no longer thirsty!')
        
        # Checks if player is thirsty or dies of thirst
        if done == False:
            if thirst > 3 and thirst <= 5:
                print('You are thirsty!')
            elif thirst > 5:
                print('You died of thirst!')
                done = True
        
        # Checks if Camel is getting tired or dies of tiredness
        if done == False:
            if camel_tiredness > 4 and camel_tiredness <= 7:
                print('Your camel is getting tired.')
            elif camel_tiredness > 7:
                print('Your camel is dead.')
                done = True

        # Checks is the natives are catching up, or if they catch the player
        if done == False:
            if miles_traveled - natives_traveled <= 0:
                print('The natives have caught up! They catch you and make you their slave!')
                done = True
            elif miles_traveled - natives_traveled < 15:
                print('The natives are getting close!')
        
        # Prints how much the player managed to travel before loosing the game
        if done == True:
            print(f'You managed to travel a total of {miles_traveled}/200 miles.')
        
        # Checks if player wins the game
        if done == False:
            if miles_traveled >= 200:
                print()
                print('You made it across the desert! You won!')
                done = True
        print()


main()