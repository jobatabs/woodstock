#
# MAP SCREEN
#


label map_screen:


    scene bg map
    with fade
    menu:
        "Go to the town hall":
            jump townhall
        "Go to the backstage area":
            jump backstage
        "Go to your trailer":
            jump trailer
