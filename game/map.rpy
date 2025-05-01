#
# MAP SCREEN
#


label map_screen:
    play music "empty.mp3" fadein 2.0 fadeout 2.0
    scene bg map
    with fade
    menu:
        "Town Hall":

            $ location = "townhall"
            $ talk_to = "town supervisor"

            jump townhall
        "Backstage":

            scene black with wiperight

            show text "Backstage" at truecenter with dissolve

            pause 1.0

            hide text with dissolve

            pause 0.3

            $ location = "backstage"
            $ talk_to = "Larry"

            jump backstage
        "Trailer":

            scene black with wiperight

            show text "Trailer" at truecenter with dissolve

            pause 1.0

            hide text with dissolve

            pause 0.3

            $ location = "trailer"

            jump trailer
        
        "Toilets" if toilet_area_open == True:

            scene black with wiperight

            show text "Toilets" at truecenter with dissolve

            pause 1.0

            hide text with dissolve

            pause 0.3

            $ location = "toilets"
            if day_one_end == "money":
                $ talk_to = "kid in the toilet"
            elif day_one_end == "whisky":
                $ talk_to = "hippie girl"
            else:
                "Problem with determining who to talk to in the toilet area."
                $ talk_to = "kid in the toilet"

            jump toilets

        "Field" if field_area_open == True:

            scene black with wiperight

            show text "Field" at truecenter with dissolve

            pause 1.0

            hide text with dissolve

            pause 0.3

            $ location = "field"
            $ talk_to = "cows"

            jump field
