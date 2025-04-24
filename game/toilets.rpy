#
# TOILETS
#

label toilets:
    "The toilet area is surprisingly clean. You hear shouting and banging coming from one of the stalls"
    jump actionsmenu

label talktoilets:
    k "Help me!"
    menu:
        "Is there a problem?":
            k "What do you think?!"
            k "I'm stuck in here!"
            k "It's sweltering!"
            jump talktoilets
        "Can you unlock the door?":
            k "Do you think I haven't tried?!"
            jump talktoilets
        "Ask Mary Jane to start up the winch" if winch_hooked:
            "The kid is free."
            k "Thank you so much! Even my camera's fine!"
            $ day_two_ending = "winch"
            jump day2_ending
        "Leave":
            k "Hey, don't leave me here!"
            jump actionsmenu

label looktoilets:
    menu:
        "There's a kid stuck in the toilet."

        "Break down the door with the axe" if have_axe:
            "You break down the door. The kid is free."
            k "Thank you so much!"
            k "But my camera broke..."
            $ day_two_ending = "axe"
            jump day2_ending
        "Pull on the door":
            "The door holds firm."
            jump looktoilets
        "Attach the winch to the toilet door" if winch_here:
            "You hook up the winch to the door of the stall."
            $ winch_hooked = True
            jump actionsmenu
        "Back":
            jump actionsmenu