label actionsmenu:

    menu:
        "[playertip]"

        "Go to the town supervisor's office" if location == "townhall":
            jump office
        "Talk" if location in talkable:
            jump talkmenu
        "Look":
            jump lookmenu
        "Go somewhere" if location != "townhall":
            jump map_screen
        "Leave" if location == "townhall":
            jump map_screen

label talkmenu:

    if location == "backstage":

        jump talkbackstage

    elif location == "toilets":

        jump talktoilets

    elif location == "field":

        jump talkfield

label lookmenu:

    hide chara with dissolve

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
