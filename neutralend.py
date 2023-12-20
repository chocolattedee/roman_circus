import happy2
import title_screen
import characters
import neutral2

def neutralend_scene():
    print("You wander to the edge of the ring just in time to watch your favorite Gladiator take the win rather viscerally! The victory signals the end of the Circus and all Romans start to file off the field.\n")
    print("Wanna go again?\n")
    player_choice = input("Y/N: ")
    player_endchoice = player_choice.upper()

    if player_endchoice == "Y":
        print("Your enjoyment has come to an end but no one will ever forget you",characters.user_id)
        return title_screen.Roman_circus_title()
    elif player_endchoice == "N": 
        print("Your hesitancy",characters.user_id,"was consistent if not extremely boring!!!\n")
        return title_screen.Roman_circus_title()
    else:
        print("Invalid Input Friendo :)\n")
        return neutralend_scene()