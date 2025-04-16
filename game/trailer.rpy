#        
# TRAILER
#

# After the starting set-up, the game properly begins
label trailerstart:

    scene bg trailer
    with fade
    "It is the morning of August 15th, 1969."
    "You wake up hungover in your trailer and look around a bit."
    "Last night's launch party was really quite something..."
    "Quick flashbacks from various scenes of debauchery appear in your mind."
    "You eventually get up from your bed and put on some clothes."
    $ playertip = "I should talk to Larry backstage."
    menu:
        "Okay, let's get out there and get stuff done. (Leave the trailer)":
            "As you make your way towards the door, you notice a note taped to your wall."
            "Someone has left a message for you."
            "\"[player_name]! I need to talk to you ASAP! It looks like we're not going to be able to go forward with the festival after all! Come talk to me backstage as soon as you wake up.\""
            "The note has been signed by \"Larry\"."
            "You have a faint memory of hiring someone named Larry to be the lighting technician for the stage..."
            jump map_screen
        "Wait, who am I?":
            "Your name is [player_name], and you are the producer in charge of putting together the Woodstock Music Festival."
            menu:
                "Oh, okay then. Well, let's get going! (Leave your trailer)":
                    "As you make your way towards the door, you notice a note taped to your wall."
                    "Someone has left a message for you."
                    "\"[player_name]! I need to talk to you ASAP! It looks like we're not going to be able to go forward with the festival after all! Come talk to me backstage as soon as you wake up.\""
                    "The note has been signed by \"Larry\"."
                    "You have a faint memory of hiring someone named Larry to be the lighting technician for the stage..."
                    jump map_screen
                "Huh? What is \"The Woodstock Music Festival\"":
                    "The Woodstock Music and Art Fair, commonly referred to as Woodstock, was a music festival held from August 15 to 18, 1969, on a dairy farm in Bethel, New York, 40 miles (65 km) southwest of the town of Woodstock."
                    "Billed as \"An Aquarian Exposition: 3 Days of Peace & Music\" and alternatively referred to as the Woodstock Rock Festival, it attracted an audience of more than 460,000."
                    "Thirty-two acts performed outdoors despite overcast and sporadic rain. It was one of the largest music festivals in history and became synonymous with the counterculture of the 1960s."
                    "The festival has become widely regarded as a pivotal moment in popular music history, as well as a defining event for the silent and baby boomer generations."
                    menu:
                        "Cool! Well, let's get going. (Leave your trailer)":
                            "As you make your way towards the door, you notice a note taped to your wall."
                            "Someone has left a message for you."
                            "\"[player_name]! I need to talk to you ASAP! It looks like we're not going to be able to go forward with the festival after all! Come talk to me backstage as soon as you wake up.\""
                            "The note has been signed by \"Larry\"."
                            "You have a faint memory of hiring someone named Larry to be the lighting technician for the stage..."
                            jump map_screen


label trailer:
    scene bg trailer
    with fade

    "Your trailer is a mess. You can still smell the booze from last night."

    jump actionsmenu


label looktrailer:
    menu:
        "Note taped to the wall":
            "There is a note taped to your wall."
            "\"[player_name]! I need to talk to you ASAP! It looks like we're not going to be able to go forward with the festival after all! Come talk to me backstage as soon as you wake up.\""
            "The note has been signed by Larry."
            jump looktrailer

        "Under the bed":
            if have_metal_detector == False:
                "Your trusty FEW57ER 9000 Mine Detector lies abandoned under your bed."
                menu:
                    "Take the mine detector":
                        "You take the well-used mine detector with you."
                        $ have_metal_detector = True
                        jump looktrailer
                    "Leave the mine detector":
                        "You leave the mine detector to its fate."
                        jump looktrailer
            else:
                "Apart from a half-eaten hot-dog and an unopened pack of condoms that is past its expiry date, there is not much here."
                jump looktrailer
        
        "Cabinet":
            if have_whisky == False:
                "You find a bottle of whisky in the cabinet."
                menu:
                    "Take it":
                        "You take the bottle."
                        $ have_whisky = True
                        jump looktrailer
                        
                    "Leave it.":
                        "There's no time to get drunk now."
                        jump looktrailer
            else:
                "The cabinet is empty, and dirty. Geez, when did you clean here?"
                jump looktrailer

        "Bed":
            "Your bed calls to you, promising comfort beyond belief..."
            menu:
                "Rest a bit":
                    "You lay down and relax for a moment."
                    "Time passes."
                    "You feel rested."
                    menu:
                        "Keep resting":
                            "You keep relaxing for a bit more."
                            "Time passes."
                            "You feel more rested."
                            menu:
                                "Try to fall asleep.":
                                    "(Don't you have a festival to save?)"
                                    "You try to fall asleep."
                                    "Time passes."
                                    "You succesfully stare at the ceiling for some time."
                                    if mystical_stone==True:
                                        if monster_dead==False:
                                            menu:
                                                "Try to fall asleep one more time.":
                                                    "You fall in to a deep, mystic slumber."
                                                    jump monster_battle
                                                "Get up":
                                                    "With a sigh, you wrench yourself up."
                                                    jump looktrailer
                                        else:
                                            menu:
                                                "Get up":
                                                    "With a sigh, you wrench yourself up."
                                                    jump looktrailer
                                    else:
                                        menu:
                                            "Get up":
                                                "With a sigh, you wrench yourself up."
                                                jump looktrailer
                                "Get up":
                                    "With a sigh, you wrench yourself up."
                                    jump looktrailer
                        "Get up":
                            "With a sigh, you wrench yourself up."
                            jump looktrailer
                "Stay up":
                    "It's not time to rest now."
                    jump looktrailer


        "Back":
            jump actionsmenu