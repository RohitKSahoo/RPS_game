import random
import pyttsx3

engine = pyttsx3.init()

emojis = {'r':'🪨', 'p':'📃', 's':'✂️'} # made a dict. where the choices are assigned as emojis
choices = ('r', 'p', 's') # used the tuple cuz it is read only, but list isnt.

def get_user_choices():
    while True:
        you = input("Rock, Paper, Scissor? (r/p/s): ").lower()
        if you in choices:  # checked if the input is present in the choices list or not.
            return you # as it is present, returned the same
        else:
            print("Invalid choice")

def display_choice(you, comp):
    print(f'You chose: {emojis[you]}')
    print(f'Computer chose: {emojis[comp]}')

def determine_winner(you, comp):
    if you == comp:
        print("Draw")
    elif (you == 'r' and comp == 's') or (you == 'p' and comp == 'r') or (you == 's' and comp == 'p'):
        print("You win")
    else:
        print("You lose")

def play_game():
    while True:
        you = get_user_choices()
        comp = random.choice(choices) #comp stored a choice made randomly

        display_choice(you, comp)
        determine_winner(you, comp)

        cont = input("Continue? (y/n): ").lower()
        if cont == 'n':
            engine.say('Thank you for playing')
            engine.runAndWait()
            print("Thank you for playing")
            break

play_game()