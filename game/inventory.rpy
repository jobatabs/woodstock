init python:
    def update_inventory():
        drew = False
        if have_metal_detector:
            drew = True
            renpy.show("metal detector", at_list=[metal_detector_transform], zorder=2)
        else:
            renpy.hide("metal detector")
        if have_whisky:
            drew = True
            renpy.show("whisky", at_list=[whisky_transform], zorder=3)
        else:
            renpy.hide("whisky")
        if have_axe:
            drew = True
            renpy.show("axe", at_list=[axe_transform], zorder=2)
        else:
            renpy.hide("axe")
        if have_batteries:
            drew = True
            renpy.show("batteries", at_list=[battery_transform], zorder=2)
        else:
            renpy.hide("batteries")
        if have_chest:
            drew = True
            renpy.show("chest", at_list=[chest_transform], zorder=2)
        else:
            renpy.hide("chest")
        if have_paper:
            drew = True
            renpy.show("paper", at_list=[paper_transform], zorder=2)
        else:
            renpy.hide("paper")
        if cents > 0:
            drew = True
            if cents == 5:
                renpy.show("cents5", at_list=[gold_transform], zorder=2)
            elif cents == 10:
                renpy.show("cents10", at_list=[gold_transform], zorder=2)
            elif cents == 15:
                renpy.show("cents15", at_list=[gold_transform], zorder=2)
            elif cents == 20:
                renpy.show("cents20", at_list=[gold_transform], zorder=2)
        else:
            renpy.hide("cents5")
            renpy.hide("cents10")
            renpy.hide("cents15")
            renpy.hide("cents20")
        if punched_machine == True:
            drew = True
            renpy.show("hotcoin", at_list=[stone_transform], zorder=2)
        else:
            renpy.hide("hotcoin")
        if drew:
            renpy.show("inventory bg", what=Solid("#4b4b4b93"), at_list=[inventory_bg], zorder=1)

transform metal_detector_transform:
    offset (810, 360)
    pos (0, 0)
    zoom 0.15

transform whisky_transform:
    offset (810, 360)
    pos (100, 0)
    zoom 0.15

transform axe_transform:
    offset (810, 360)
    pos (300, 100)
    zoom 0.15

transform battery_transform:
    offset (810, 360)
    pos (0, 100)
    zoom 0.15

transform chest_transform:
    offset (810, 360)
    pos (100, 100)
    zoom 0.15

transform gold_transform:
    offset (810, 360)
    pos (200, 0)
    zoom 0.15

transform paper_transform:
    offset (810, 360)
    pos (200, 100)
    zoom 0.15

transform stone_transform:
    offset (810, 360)
    pos (300, 0)
    zoom 0.15

transform inventory_bg:
    pos (800, 350)
    size (450, 250)