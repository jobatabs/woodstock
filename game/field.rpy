#
# FIELD
#

label field:
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
            $ day_two_ending = "happycows"
            jump day2_ending
        "Back":
            jump actionsmenu

label lookfield:
    menu:
        "The cows seem udderly uninterested in you or the socio-political importance of Woodstock."

        "Carefully try to move the cows":
            "Nothing happens."
            jump lookfield
        "Shout":
            p "Okay, come on cows! Let's move!"
            "LET'S MOVE!"
            "SHOO! SHOO!"
            "Jimi Hendrix is supposed to come here to play!!"
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
                    $ day_two_ending = "cowfight"
                    jump day2_ending
                "Leave the cows alone":
                    p "Okay, chill! Don't have a cow..."
                    p "I mean, I've really got no beef with any of you. I mean-"
                    p "Ah, the hell with this."
                    "You ran away from the cows as fast as you can."
                    jump lookfield
        "Back":
            jump actionsmenu