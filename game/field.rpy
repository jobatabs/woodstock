#
# FIELD
#

label field:
    "It's field time."
    jump actionsmenu

label talkfield:
    menu:
        "Cow":
            "MOO!"
            jump talkfield
        "Back":
            jump actionsmenu

label lookfield:
    menu:
        "Cows":
            "There's a bunch of cows here."
            jump lookfield
        "Back":
            jump actionsmenu