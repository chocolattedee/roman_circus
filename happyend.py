import happy2
import title_screen
import characters

def happyendscene():
    print("You made it to the good end! Cue Trumpets!!! Kiss a baby on the head you're a winner!\n")
    print("Wanna go again?\n")
    player_choice = input("Y/N: ")
    player_endchoice = player_choice.upper()

    if player_endchoice == "Y":
        print("Your enjoyment has come to an end but no one will ever forget you",characters.user_id)
        return title_screen.Roman_circus_title()
    elif player_endchoice == "N": 
        print("Your journey",characters.user_id," has concluded, though there is always the next decree to look forward to...")
        return 
    else:
        print("Invalid Input Friendo :)")
        return happyendscene()