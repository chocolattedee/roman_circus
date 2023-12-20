import intro
import characters


def Roman_circus_title(): 
    print("---------------------------------------- The Roman Circus ----------------------------------------")
    print("Rome,Italy: 5th Century\n") #Creating the location
    print("""The sun beats down on the streets of Rome as crowds gather in the Forum, their faces etched with worry and anger. The people of Rome have heard rumors of a new decree from the Emperor, \nand they fear the worst. Tension is high as they wait for the announcement, the air thick with anticipation and dread.

At last, the Emperor emerges from the palace, flanked by his guards. His face is stern and unyielding as he surveys the throngs of people before him. The crowds fall silent, waiting for him to speak.

"My fellow Romans," he begins, his voice echoing across the Forum. "I have passed a new decree, one that I believe is necessary for the prosperity of our great empire. But I know that it will be \n unpopular with some of you."

A murmur ripples through the crowd, and the Emperor raises his hand to silence them.

"I understand your concerns, but I assure you that this is for the greater good. It is time for us to make some sacrifices, to tighten our belts and work together to ensure a bright future for Rome."

The people of Rome exchange uneasy glances, unsure of what this decree might mean for them. They know that when the Emperor speaks, they must listen,n\nbut they cannot help but wonder what the future holds. As they disperse from the Forum, the murmurs turn to whispers, and the whispers to fearful silence. It seems that once again, the fate of Rome is in the hands of its rulers.
    
    """ )   #Behind the scenes
    print("Waiting with baited breath...")
    print("Will you answer the call to Adventure?")
    start_game = input("Y/N:\n")
    play_game = start_game.upper()
 
    if play_game == "Y/N:":
        Roman_circus_title()
        return
    elif play_game == "Y":
        characters.player_id()
        intro.intro_scene()
        return
    elif play_game == "N":
        print("Have a good one!\n")

    else:
        print("Incorrect input friend.\n")
        return Roman_circus_title()
    
