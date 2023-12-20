import characters
import poorend
import happy2
import neutral2 

def neutralscene1():
    print("After shaking off the initial frustration at your situation, you participate out of fear that dejecting the proposal would lead to greater consequence.\nYou arrive just in time to handed some of the last seats at the very back of the circus. Your response to this is...\n ")
    player_choice = input("Happy(H),Neutral(N),Poorly(P): ")
    player_choice2 = player_choice.upper()

    if player_choice2 == "H":
        print("Your enjoyment as a",characters.user_id, "is undisturbed by this news and you proceed to party harder.\n")
        return happy2.happyscene2()
    elif player_choice2 == "N": 
        print("Your hesitancy",characters.user_id," is common, everyone else is quitely upset! After thinking on it you decide to go for a walk around the Circus.\n")
        neutral2.neutralscene2()
    elif player_choice2 == "P":
        print("Your attitude is noticed",characters.user_id,"...")
        poorend.poorscene()
    else:
        print("Invalid Input Friendo :\n")
        return neutralscene1()