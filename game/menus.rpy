label actionsmenu:
    $ update_inventory()
    menu:
        "[playertip]"

        "Go to the town supervisor's office" if location == "townhall":
            if supervisor_cow_talk == True:
                "The door to the office is locked."
                jump actionsmenu
            jump office
        "Talk to [talk_to]" if location in talkable:
            jump talkmenu
        "Look around":
            jump lookmenu
        "Leave":
            jump map_screen

label talkmenu:

    if location == "backstage":

        jump talkbackstage

    elif location == "toilets":

        jump talktoilets

    elif location == "field":

        jump talkfield

label lookmenu:

    if location == "backstage":

        jump lookbackstage

    elif location == "trailer":

        jump looktrailer

    elif location == "townhall":
        jump looktownhall

    elif location == "toilets":

        jump looktoilets

    elif location == "field":

        jump lookfield
