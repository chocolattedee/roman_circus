import characters
import poorend
import happyend
import neutralend 

def neutralscene2():
    print("There is a strong breeze that comes through the top of the arena and knocks your jug of wine all over your toes! Your response is:")
    player_choice = input("Happy(H),Neutral(N),Poor(P): ")
    player_choice2 = player_choice.upper()

    if player_choice2 == "H":
        print("Your enjoyment as a",characters.user_id, "is undisturbed by this news and you proceed to party harder.")
        return happyend.happyendscene()
    elif player_choice2 == "N": 
        print("Your hesitancy",characters.user_id," is not uncommon, everyone else is perturbed as well! After thinking on it you decide to get some 'cheap' refreshments.")
        neutralend.neutralend_scene()
    elif player_choice2 == "P":
        print("Your dissappointment is immeasurable, and your day is surely about to be ruined...")
        poorend.poorscene()
    else:
        print("Invalid Input Friendo :)\n")
        return neutralscene2()