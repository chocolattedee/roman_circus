# characters  = {1:'Peasant', 2: "Gladiator", 3:"Royal"}
user_id = [] 


def player_id():
    print("1: 'Peasant', 2: 'Gladiator', 3:'Royal'")
    player_choice = input("Choose a Character:\n")
    global user_id
    if player_choice == "1":
        player_choice = "Peasant"
        user_id = player_choice
        print(f"You have chosen the {user_id}")
        return user_id
    elif player_choice == "2":
        player_choice = "Gladiator"
        user_id = player_choice
        print(f"You have chosen the {user_id}")
        return user_id
    elif player_choice == "3":
        player_choice = "Royal"
        user_id = player_choice
        print(f"You have chosen the {user_id}")
        return user_id
    else:
        print("Improper Input Amigo :D")
        return player_id()


#Successfully assigns a character 