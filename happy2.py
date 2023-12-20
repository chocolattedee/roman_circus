import characters
import poorend
import neutral2
import happyend

def happyscene2():
    print("Its not your first time watching someone get turned into lion kibble; You carry on to your seat before a raffle is called and the reward goes to the numeral next you! Your response is...\n")
    player_choice = input("Happy(H),Neutral(N),Passive(P):")
    player_choice3 = player_choice.upper()
    # print(player_choice3)

    if player_choice3 == "H":
        print("Your enjoyment as a",characters.user_id, "has caught some attention and now its all eyes on the dance floor!\n")
        return happyend.happyendscene()
    elif player_choice3 == "N": 
        print("Your dissappointment",characters.user_id," is expected, but you took it better than some! After some brooding,you decide to get a closer look at the games.\n")
        neutral2.neutralscene2()
    elif player_choice3 == "P":
        print("Your face folds as if having smelled rotted milk, before you have a chance to speak your dissmay you are restrained and carried away...\n")
        poorend.poorscene()
    else:
        print("Invalid Input Friendo :)\n")
        return happyscene2()