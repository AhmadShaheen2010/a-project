import time
import random

charactersNames=["an Evil fairy","a Pirate","an Evil robot","a Serial killer"
                 ,"The devil","Cinderblock","Slade"]
#a character list which we will use later to add the random factor to the game

class player():
    stop = False
#sets the stop variable to a false bolean value which we will use later to
# determine if the player want to replay the game or not
    took_the_wand=False
#the same with the stop variable
    score=0
#the score which should be set to 0 for now so that we can change it later
    Start_time=time.time()
#we will use this later to determine the elapsed time

def print_sleep_repeat(text,text1=""):
    #a function which prints the given text and wait 2 seconds
    # i also added two arguements instead of 1 to make it so that i can cut the
    # lines of the Print_Sleep_Repeat statments and i did set a default value
    # to the text1 arguement so that it's not required and i made that default
    # value nothing so that it doesn't print something that i don't want but at
    # the same time when it's used it's done
    print(text,text1)
    time.sleep(2)

def win():
    #a function for winning , it had to be above the house function as the win
    # is there,this win function is triggered when u win and it prints the
    # score then asks if u want to play again and if u say yes it resets the
    # variables to make everything start again like usual
    def replay_or_not():
        print_sleep_repeat(f"Your score: {player.score}")
        elapsed_time = time.time() - player.Start_time
        #this subtracts the current time from the start time to tell u the
        # elapsed time which will be printed in the line after it
        print_sleep_repeat(f"Elapsed time :  {elapsed_time} seconds")
        user_input5 = input("play again? (Y/N): ")
        if user_input5.lower() == "y":
            player.score = 0
            player.took_the_wand = False
            player.Start_time=time.time()
        elif user_input5.lower() == "n":
            print("Goodbye then.")
            player.stop = True
        else:
            # this part is used to ask the question again if the input wasn't
            # 1 or 2
            print_sleep_repeat("Invalid input. Please enter y or n")
            replay_or_not()

    replay_or_not()

def cave():
    # in this function it checks if u have the wand as if u have it will be
    # kicked out of it and if  don't have it ,it will ask u wether to take it
    # or not while
    if player.took_the_wand== True:
        print_sleep_repeat("u left the cave bc it's empty")
    else:
        print_sleep_repeat("You entered the cave.")
        print_sleep_repeat("it's dark and u see nothing but a bright wand")
        print_sleep_repeat("press 1 to take it and 2 to not take it")

        def cave_wand_taking_choice():
            # this fuction is one of the functions which take the input and
            # does something based on it
            user_input2 = input("Please enter 1 or 2: ")
            if user_input2 == "1":
                player.took_the_wand = True
                print("u took the wand and left the cave and ur score has",
                      "increased by 1")
                player.score += 1
            elif user_input2 == "2":
                print("u left the cave and ur score is the same")
            else:
                # this part is used to ask the question again if the input
                # wasn't 1 or 2
                print("Invalid input. Please enter 1 or 2.")
                cave_wand_taking_choice()
        cave_wand_taking_choice()

def house():
    # in this function if u enter the house with the magic wantd which u found
    # in the cave u will be able to use it against the enemy and win and get
    # one more score point but if u run from the house u will lose 1  score
    # point and if u didn't get the wand from the cave u will have ur normal
    # weak wand and if u use it u will lose and the score will be set to 0
    character=random.choice(charactersNames)
    if player.took_the_wand == False:
        print_sleep_repeat(f"You entered the house.u see {character} which",
                           "wants to kill u")
        print_sleep_repeat("1 to use ur weak wand or 2 to run away")
        def house_weak_wand_using_choice():
            # this fuction is one of the functions which take the input and
            # does something based on it
            user_input3 = input("Please enter 1 or 2: ")
            if user_input3 == "1":
                print("ur wand didn't work and u lost so your score has been",
                      "set to 0")
                player.score = 0
            elif user_input3 == "2":
                print("u ran away and u lost 1 score point")
                player.score -=1
            else:
                # this part is used to ask the question again if the input
                # wasn't 1 or 2
                print("Invalid input. Please enter 1 or 2.")
                house_weak_wand_using_choice()
        house_weak_wand_using_choice()
    else:
        print_sleep_repeat(f"You entered the house.u see {character} which",
                           "wants to kill u")
        print_sleep_repeat("1 to use ur powerful wand or 2 to run away")
        def house_powerful_wand_using_choice():
            # this fuction is one of the functions which take the input and
            # does something based on it
            user_input4 = input("Please enter 1 or 2: ")
            if user_input4 == "1":
                print("ur wand worked and u won ")
                player.score += 1
                win()
            elif user_input4 == "2":
                print("u ran away and lost one score point")
                player.score -= 1
            else:
                # this part is used to ask the question again if the input
                # wasn't 1 or 2
                print("Invalid input. Please enter 1 or 2.")
                house_powerful_wand_using_choice()
        house_powerful_wand_using_choice()

def house_or_cave_choice():
    #it directs u to either the cave or the house based on the ur input
    user_input1 = input("Please enter 1 or 2: ")
    if user_input1 == "1":
        house()
    elif user_input1 == "2":
        cave()
    else:
        #this part is used to ask the question again if the input wasn't 1 or 2
        print("Invalid input. Please enter 1 or 2.")
        house_or_cave_choice()

while player.stop == False :
    #this is the main loop which keeps everything happening again and again ...
    print_sleep_repeat("u find ur self in a forest near a cave and a house and"
                       ,"u have a weak wand")
    print_sleep_repeat("rumors are that the cave has secret powers in it and",
                       "the house contains EVIL Creatures")
    print_sleep_repeat("Press 1 to enter the house.......")
    print_sleep_repeat("press 2 to enter the cave............")
    house_or_cave_choice()
