import characters
import poorend
import happy2
import neutral2

def happyscene1():
    print("The Circus stadium is packed to the brim, Romans are spilling over one another to get the best seats. Drinking in the sights you take note of the non-believers in a life or death battle with lions. This causes you to react...")
    player_choice = input("Happy(H),Neutral(N),Poorly(P): ")
    player_choice2 = player_choice.upper()

    if player_choice2 == "H":
        print("Your enjoyment as a ",characters.user_id, " is undisturbed by this news and you proceed to party harder.")
        return happy2.happyscene2()
    elif player_choice2 == "N": 
        print("Your hesitancy ",characters.user_id," is not uncommon, everyone else is perturbed as well! After thinking on it you decide to get some 'cheap' refreshments.")
        neutral2.neutralscene2()
    elif player_choice2 == "P":
        print("Your face folds as if having smelled rotted milk, before you have a chance to speak your dissmay you are restrained and carried away...")
        poorend.poorscene()
    else:
        print("Invalid Input Friendo :)")
        return happyscene1()