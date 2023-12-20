import random
import poorend
import characters
import happy_1
import neutral1

decree1 = "Provide me money and I shall put on a Circus!"
decree2 = "Provide me food and I shall put on a Circus!"
decree3 = "Provide me drink and I shall put on a Circus!"

decrees = [decree1, decree2, decree3]

def intro_scene():
    #print("If this is visible the import worked.")
    game_intro = random.choice(decrees)
    print(f"The Emperor has decreed: {game_intro}")
    player_choice = input("This news causes you to respond: Happily(H), Neutrally(N), Poorly(P): ")
    player_choice1 = player_choice.upper()
    


#Conditional check for player input 

    if player_choice1 == "H":
        print("Your eagerness to serve ",characters.user_id, "has been noted, you partake in merrymaking after paying your dues.")
        happy_1.happyscene1()
    elif player_choice1 == "N": 
        print("Your hesitancy ",characters.user_id," is waved off as common confusion, lucky you! After collecting your dues, you are then formally invited to the Circus!")
        neutral1.neutralscene1()
    elif player_choice1 == "P":
        print("Your face folds as if having smelled rotted milk, before you have a chance to speak your dissmay you are restrained and carried away...")
        poorend.poorscene()
    else:
        print("Invalid Input Friendo :)")
        return intro_scene()




#Plan for this scene: 
#Take one of three possible 'decrees' and print it to the terminal for the player to respond Happily/Poorly/Neutrally to. 
#Take the player input and based on the three responses, route the user accordingly. 
#One of the player inputs should send the user to the termination scene before ending the game.
#Planning for two more scenes for the Happily / Neutrally paths 
# Considering Intro - happy1,happy2,happy_end / Intro -- poorend // Intro --neutral1,neutral2,neutralend