#        
# TRAILER
#

# Is the player starting the game? (Determines if the intro text is displayed in the starting area)
default first_play = True

# Has the player picked up the metal detector from the trailer? (Determines if it's possible to find items in the backstage area)
default have_metal_detector = False

# Determines how many times the player has clicked the different options in the starting "fourth-wall breaking joke"
default exit_fight_dialogue_points = 0

# After the starting set-up, the game properly begins
label starting_screen:


    if first_play==True:
        scene bg trailer
        with fade
        "It is the morning of August 15th, 1969."
        "You wake up hungover in your trailer and look around a bit."
        "Last night's launch party was really quite something..."
        "Quick flashbacks from various scenes of debauchery appear in your mind."
        "You eventually get up from your bed and put on some clothes."
        $ first_play = False
    menu:
        "Look around":
            "As you make your way towards the door, you notice a note taped to your wall."
            "Someone has left a message for you."
            "\"[player_name]! I need to talk to you ASAP! It looks like we're not going to be able to go forward with the festival after all! Come talk to me backstage as soon as you wake up.\""
            "The note has been signed by \"Larry\"."
            "You have a faint memory of hiring someone named Larry to be the lighting technician for the stage..."
            jump starting_screen
        "Okay, let's get out there and get stuff done. (Leave the trailer)":
            jump map_screen
        "Wait, who am I?":
            "Your name is [player_name], and you are the producer in charge of putting together the Woodstock Music Festival."
            menu:
                "Look around":
                    "As you make your way towards the door, you notice a note taped to your wall."
                    "Someone has left a message for you."
                    "\"[player_name]! I need to talk to you ASAP! It looks like we're not going to be able to go forward with the festival after all! Come talk to me backstage as soon as you wake up.\""
                    "The note has been signed by \"Larry\"."
                    jump starting_screen
                "Oh, okay then. Well, let's get going! (Leave your trailer)":
                    jump map_screen
                "Huh? What is \"The Woodstock Music Festival\"":
                    "The Woodstock Music and Art Fair, commonly referred to as Woodstock, was a music festival held from August 15 to 18, 1969, on a dairy farm in Bethel, New York, 40 miles (65 km) southwest of the town of Woodstock."
                    "Billed as \"An Aquarian Exposition: 3 Days of Peace & Music\" and alternatively referred to as the Woodstock Rock Festival, it attracted an audience of more than 460,000."
                    "Thirty-two acts performed outdoors despite overcast and sporadic rain. It was one of the largest music festivals in history and became synonymous with the counterculture of the 1960s."
                    "The festival has become widely regarded as a pivotal moment in popular music history, as well as a defining event for the silent and baby boomer generations."
                    menu:
                        "Look around":
                            "As you make your way towards the door, you notice a note taped to your wall."
                            "Someone has left a message for you."
                            "\"[player_name]! I need to talk to you ASAP! It looks like we're not going to be able to go forward with the festival after all! Come talk to me backstage as soon as you wake up.\""
                            "The note has been signed by \"Larry\"."
                            jump starting_screen
                        "Cool! Well, let's get going. (Leave your trailer)":
                            jump map_screen
                        "This game seems dumb. I don't think I'm interested in playing this anymore.":
                            "..."
                            "Um, okay..."
                            "You just started."
                            jump exit_fight_dialogue

# Fourth wall breaking joke


label exit_fight_dialogue:


    "Are you saying you want to quit the game now?"
    menu:
        "Yeah, this bird is baked. Let me out.":
            "Sorry, I couldn't quite hear you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "Yeah man, I'm one toke over the line. Let me off this trip.":
            "Sorry, I couldn't quite hear you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "I'm afraid my prefrontal cortex has had quite enough now. Leave me be, thank you.":
            "Sorry, I couldn't quite hear you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "En jaksa enää. Haluan poistua juomaan viinaa. Nyt.":
            "Sorry, I couldn't quite understand you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "Ja, jag skulle vilja gå av den här resan nu, tack.":
            "Sorry, I couldn't quite understand you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "Ja, ich möchte diese Reise jetzt beenden, danke.":
            "Sorry, I couldn't quite understand you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "What I actually meant was that I'd like to keep playing this remarkable work of art that you so foolishly insist on referring to simply as \"the game\"." if exit_fight_dialogue_points>=1:
            "Really?! Oh that's so great to hear that you like the game!"
            "Of course, we'll let you get on with the game now!"
            "Have fun!"
            jump map_screen


label trailer:


    scene bg trailer
    with fade
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
                                            jump trailer
                                else:
                                    menu:
                                        "Get up":
                                            jump trailer
                            else:
                                menu:
                                    "Get up":
                                        jump trailer
                        "Get up":
                            jump trailer
                "Get up":
                    jump trailer
        "Look around":
            if have_metal_detector==False:
                "Your trusty metal detector lies abandoned under your bed."
                menu:
                    "Take the metal detector":
                        "You take the well-used metal detector with you."
                        $ have_metal_detector = True
                        jump trailer
                    "Leave the metal detector":
                        "You leave the metal detector to its fate."
                        jump trailer
            else:            
                "Apart from a half-eaten hot-dog and an unopened pack of condoms that is past its expiry date, there is nothing here."
                jump trailer
        "Leave":
            jump map_screen