import title_screen
import characters

def poorscene():
    print("The",characters.user_id,"groggily awakens to the dusty floor of the arenas dungeon.\n")
    print("""
        You had been a proud Roman in the Roman for years.
        But today, as you prepared to fight a lion in front of the baying crowd, your heart sinks. 
        The Emperor's new decree had filled them with a sense of dread, and they knew that they would not live through with this fight.\n
    """)
    print("Want to go on another adventure?")
    player_choice = input("Y/N: \n")
    user_choice = player_choice.upper()

    if user_choice == "Y/N:": 
        return poorscene()
    elif user_choice == "Y":
        return title_screen.Roman_circus_title()
    elif user_choice == "N":
        print("Better luck next time Adventurer!\n")
    else:
        print("Invalid Input Friendmigo\n")
