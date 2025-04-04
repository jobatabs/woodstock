#
# DEFINING PARAMETERS
#

# Characters
define p = Character("[player_name]")
default player_name = "Player"

#
# GAME STARTS HERE
#

# First, we ask the player their name.


label start:


    "Hello and thank you for trying out our prototype!"
    "What is your name?"
    menu:
        "My name is Derek.":
            $ player_name = "Derek"
        "My name is Eliza.":
            $ player_name = "Eliza"
        "My name is Jonatan.":
            $ player_name = "Jonatan"
        "My name is Juha.":
            $ player_name = "Juha"
        "My name is Tuukka.":
            $ player_name = "Tuukka"
        "Just call me \"Player\".":
            $ player_name = "Player"
        "My name is... (choose your own name)":
            $ player_name = renpy.input("My name is...")
            $ player_name = player_name.strip()
            if player_name=="":
                "Don't want to give a name after all, eh?"
                "Fine. You shall be called..."
                "\"Generic_gender-neutral_name_01!\""
                $ player_name="generic_name_01"
        "My name is none of your business.":
            $ player_name = "Mr. Poopybutts"
            "...!"
            "Very well, have it your way."
            "For the duration of this game, you shall be called..."
            "Mr. Poopybutts."
    "Pleasure to make your acquaintance, [player_name]!"
    "You shall now be released in to the world and allowed to start the game."
    "We hope that you will enjoy your time with..."
    "\"Woodstock Game Prototype 1.0\"!"
    "(Try to imagine a mind-blowing intro sequence here)."
    jump title

# The player is given a chance to change their name before starting the game (unless their name is "Mr. Poopybutts")


label title:


    if player_name=="Mr. Poopybutts":
        menu:
            "My name is Mr. Poopybutts. Let's start the game. (Start the game)":
                jump starting_screen
    else:
        menu:
            "Let's start the game! (Start the game)":
                jump starting_screen
            "Actually, I think I made a mistake choosing my name. Let me go back. (Choose your name again)":
                jump start
