#
# TOWN HALL
#

label townhall:
    play music "townhall.mp3" fadein 2.0 fadeout 2.0
    scene black with wiperight

    show text "Town Hall" at truecenter with dissolve

    pause 1.0

    hide text with dissolve

    pause 0.3

    scene bg townhall
    with fade
    if townhall_first_visit==True:
        $ townhall_first_visit = False
        "The townhall is dusty and silent. You hear noises coming from the town supervisor's office."
    else:
        "The townhall is silent as ever."
    jump actionsmenu

# Town hall searching for items


label looktownhall:
    if have_axe==False:
        "The corridors of the town hall don't seem to contain much more than a single vending machine. There is a case with a fire axe in it."
    else:
        "The corridors of the town hall don't seem to contain much more than a single vending machine. The fire axe case lies empty."
    menu:
        
        "Vending machine":
            scene bg vending_machine
            with dissolve
            jump vending_machine
        
        "Fire axe case" if have_axe==False:
            "You see a fire axe in the unlocked case."
            menu:
                "Take the axe":
                    if day == 1:
                        p "Hmm... maybe I should try negotiating first..."
                        jump looktownhall
                    else:
                        "You take the axe."
                        $ have_axe = True
                        $ update_inventory()
                    jump looktownhall
                
                "Leave":
                    "You leave the axe to its fate."
                    jump looktownhall
        "Back":
            jump actionsmenu

# Town hall vending machine


label vending_machine:
    
    $ have_seen_vending_machine = True
    if have_batteries==False:
        "The only item left for sale is a pack of batteries."
    else:
        "The vending machine is empty."
        jump looktownhall
    menu:
        "Press the button for the batteries":
            "The display of the vending machine flashes \"20 cents\"."
            menu:
                "Insert 20 cents in to the machine":
                    if cents<20:
                        "You only have [cents] cents."
                        jump vending_machine
                    elif cents>=20:
                        "You insert 20 cents in to the machine."
                        "The machine spits out the pack of batteries, and you pick them up."
                        $ cents -= 20
                        $ have_batteries = True
                        $ update_inventory()
                        jump actionsmenu
                "Walk away from the vending machine":
                    scene bg townhall
                    with dissolve
                    jump looktownhall
        "Punch the machine" if punched_machine==False:
            "You punch the machine, and a single coin drops from the coin-return slot."
            "You pick up the coin."
            "One one side of the coin, it says \"ONE CAR WASH\"."
            "On the other side, there is a logo of a car on fire and underneath a text, \"Texas Pete's Flaming Hot Car Wash\"."
            $ punched_machine = True
            $ update_inventory()
            "Although you aren't sure what you'll do with it, you take the car wash token with you."
            jump vending_machine
        "Walk away from the machine":
            scene bg townhall
            with dissolve
            jump looktownhall
