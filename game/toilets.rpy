#
# TOILETS
#

label toilets:
    "It's toilet time."
    jump actionsmenu

label talktoilets:
    menu:
        "Marty":
            "Talking to Marty."
            jump talktoilets
        "Back":
            jump actionsmenu

label looktoilets:
    menu:
        "Toilet":
            "There's a kid stuck in the toilet."
            jump looktoilets
        "Back":
            jump actionsmenu