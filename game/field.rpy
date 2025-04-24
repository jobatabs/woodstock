#
# FIELD
#

label field:
    "Cows cover the landing area."
    jump actionsmenu

label talkfield:
    menu:
        "Cow":
            "MOO!"
            jump talkfield
        "Ask farmer to move cows" if farmer_awake:
            "The farmer moves the cows."
            $ day_two_ending = "happycows"
            jump day2_ending
        "Back":
            jump actionsmenu

label lookfield:
    menu:
        "There's a bunch of cows here."

        "Carefully try to move the cows":
            "Nothing happens."
            jump lookfield
        "Shout":
            "The cows ignore you."
            jump lookfield
        "Shove the cows":
            "The cows seem visibly angry."
            jump lookfield
        "Fight the cows":
            "The cow fucks you up."
            $ day_two_ending = "cowfight"
            jump day2_ending
        "Back":
            jump actionsmenu