#
# FIELD
#

label field:
    scene bg field
    with fade
    if day_one_end == "whisky":
        "You arrive to the landing site that's full of cows grazing."
    jump actionsmenu

label talkfield:
    menu:
        "Try to communicate with the cows":
            p "Moo?"
            "MOO!"
            jump talkfield
        "Ask farmer to move cows" if farmer_awake:
            p "Could you move the cows, Max?"
            "The farmer moves the cows."
            $ day_two_end = "happycows"
            jump day2_ending
        "Back":
            jump actionsmenu

label lookfield:
    if day_one_end == "whisky":
        menu:
            "The cows seem udderly uninterested in you or the socio-political importance of Woodstock."
            "Call for Bessie the cow" if mj_farmer_talk == True:
                "You call for Bessie the cow."
                "She leads you to the farmer, who's sleeping in the toilets."
                $ farmer_found = True
                $ location = "toilets"
                $ talk_to = "farmer"
                jump toilets
            "Carefully try to move the cows":
                "Nothing happens."
                jump lookfield
            "Shout":
                p "Okay, come on cows! Let's move!"
                p "LET'S MOVE!"
                p "SHOO! SHOO!"
                p "Jimi Hendrix is supposed to come here to play!!"
                "The cows don't seem to fully appreciate what you're saying."
                jump lookfield
            "Shove the cows":
                "The cows seem to get visibly angry."
                "Their nostrils flare, as they start to move towards you menacingly."
                "It should be noted that cows are responsible for an average of 22 human deaths in the U.S. each year."
                menu:
                    "Fight the cows":
                        "You decide to challenge the cows in hand-to-hoof combat."
                        "The cows form a ring around you, and you see a big cow make its way towards you."
                        "The rest of the herd starts mooing loudly, and you have hardly any time to react as the big bad cow launches its attack on you."
                        "The last thing you remember before waking up in the hospital is a massive hoof approaching your face."
                        $ day_two_end = "cowfight"
                        jump day2_ending
                    "Leave the cows alone":
                        p "Okay, chill! Don't have a cow..."
                        p "I mean, I've really got no beef with any of you. I mean-"
                        p "Ah, the hell with this."
                        "You ran away from the cows as fast as you can."
                        jump field
            "Back":
                jump actionsmenu

    elif day_one_end == "money":
        if winch_here == False:
            "You see a lonely truck sitting in the middle of a field."
            if town_supervisor_toilettalk == True:
                p "Maybe this was the truck the town supervisor was talking about?"
                "You take a closer look at the truck, and you notice that there is a winch-pulley system attached to it."
                menu:
                    "Get in the truck":
                        "The truck seems to be unlocked."
                        "You get in and find the keys inside the glove compartment."
                        menu:
                            "Drive the truck to the toilet area":
                                if truck_fixed == False:
                                    "You try to start the engine, but nothing happens."
                                    $ truck_started = True
                                    "Someone with some experience with cars might know what's the problem."
                                    "As it stands, you leave the truck alone."
                                    jump field
                                elif truck_fixed == True:
                                    "The engine starts with a cough."
                                    "You drive the truck to the toilet area."
                                    $ location = "toilets"
                                    $ talk_to = "kid in the toilet"
                                    $ winch_here = True
                                    jump toilets
                            "Leave the truck alone":
                                "You put the keys back in to the glove compartment and leave the car alone."
                                jump field
                    "Leave the truck alone":
                        "You let the truck sit idly in the field."
                        jump actionsmenu
            else:
                jump actionsmenu
        else:
            "The field is empty."
            jump actionsmenu
        jump actionsmenu