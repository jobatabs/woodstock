#
# MAP SCREEN
#


label map_screen:


    scene bg map
    with fade
    menu:
        "Backstage":

            scene black with wiperight

            show text "Backstage" at truecenter with dissolve

            pause 1.0

            hide text with dissolve

            pause 0.3

            $ location = "backstage"

            jump backstage
        "Trailer":

            scene black with wiperight

            show text "Trailer" at truecenter with dissolve

            pause 1.0

            hide text with dissolve

            pause 0.3

            $ location = "trailer"

            jump trailer
        "Town Hall":

            $ location = "townhall"

            jump townhall
        "Toilets" if day > 1:

            scene black with wiperight

            show text "Toilets" at truecenter with dissolve

            pause 1.0

            hide text with dissolve

            pause 0.3

            $ location = "toilets"

            jump toilets
        "Field" if day > 1:

            scene black with wiperight

            show text "Field" at truecenter with dissolve

            pause 1.0

            hide text with dissolve

            pause 0.3

            $ location = "field"

            jump field
