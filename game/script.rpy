#
# CHARACTERS
#

define p = Character("[player_name]", color="#ffffff")

define t = Character("Larry the Technician", color="#926a61ff")

define m = Character("Town Supervisor", color="#fa787e")

define k = Character("Kid in the Toilet", color="#f8fa88")

define mj = Character("Hippie Girl", color="#6eff75")

define f = Character("Farmer", color="#6d594b")

define c = Character("Bessie", color="#c774ca")

define j = Character("Monster", color="#62e489", what_color="#62e489")

#
# PARAMETERS
#

# How did day one end?
default day_one_end = ""

# How did day two end?
default day_two_end = ""

# Who to talk to?
default talk_to = "Larry"

# Have you tried to start the truck?
default truck_started = False

# Has Larry fixed the truck?
default truck_fixed = False

# Is the winch at the toilet area?
default winch_here = False

# Is the winch hooked on the door?
default winch_hooked = False

# Does the player have the bottle of whisky?
default have_whisky = False

# Does the player have the axe?
default have_axe = False

# Has the player realised that the mayor is worried about re-election?
default mayor_election_concern = False

# Has the player seen the vending machine? (Determines if it's possible to ask Larry for money)
default have_seen_vending_machine = False

# The amount of money player has to buy the batteries and if they have bought them (Batteries needed to get gold bar from backstage area)
default cents = 0
default have_batteries = False

# Determines if the safe is empty (so that nothing more can be found in the mayor's office)
default safe_empty = False

# Has the player talked to the mayor? (Determines if the mayor gives his angry rant)
default mayor_first_talk = True

# Has the player mentioned gold to the mayor, making him happy to see the player? (No gameplay effect, just changes the tone when visiting the mayor's office a second time)
default mayor_wants_gold = False

# Has the player found the stone in the safe? (Needed to travel to the dreamworld)
default mystical_stone = False

# Has the player punched the vending machine?
default punched_machine = False

# Which dialogue options the player has already chosen during the mayor negotiation?
default negotiation_drugs = False
default negotiation_faith = False

# Has the player given the gold bar to the mayor? (Unlocking the neutral ending)
default mayor_happy = False

# Has the player been to the townhall before?
default townhall_first_visit = True

# Player's name
default player_name = "Player"

# Talkable location
default talkable = ["toilets", "backstage"]

# Location the player is in
default location = "trailer"

# Text that is shown at the action menu
default playertip = "If you are reading this, something has gone wrong."

# Day (either 1 or 2)
default day = 1

# Has the player talked to the technician? (Determines if the technician explains the situation when first talking to him)
default technician_first_talk = True

# Has the player gotten a coin from Larry? (Determines if it's possible to get the batteries from the vending machine)
default have_larry_coin = False

# Has the player found 3 coins in the backstage area? (The player needs to pick up 3 coins before the battery runs out)
default have_coin = False
default have_coin2 = False
default have_old_coin = False

# Has the player offered the briefcase full of money to the town supervisor?
default mayor_wants_chest = False

# Has the player found the chest in the backstage area? (Needed to be done before it's possible to find gold)
default have_chest = False

# Has the player found the gold bar? (Needs to be given to the mayor to make him happy)
default have_gold = False

# Has the player solved "the mayor problem", causing Larry to be happy (No gameplay change except unlocking the neutral ending)
default technician_happy = False

# Has the player talked to Larry to get his piece of paper? (Needed to unlock safe)
default have_paper = False

# After 10 tries of finding nothing in the backyard area, an easter egg is found
default egg_counter = 0

# Has the player picked up the metal detector from the trailer? (Determines if it's possible to find items in the backstage area)
default have_metal_detector = False

# Is the toilet area open?
default toilet_area_open = False

# Is the landing site area open?
default field_area_open = False

# Has the town supervisor told you about the winch?
default town_supervisor_toilettalk = False

# Have you talked to the kid in the toilet?
default talked_to_kid = False

# Have you talked to MJ?
default have_talked_mj = False

# Have you talked to the town supervisor about the cows?
default supervisor_cow_talk = False

# Have you asked Larry where the farmer is?
default larry_farmer_talk = False

# Have you talked to MJ about the farmer?
default mj_farmer_talk = False

# Has Bessie the cow found the farmer?
default farmer_found = False

#
# IMAGES
#

image black = "#000000"

image chara technician frightened = "technician frightened.png"
image chara technician happy = "technician happy.png"

image chara mayor angry = "mayor neutral.png"
image chara mayor neutral = "mayor neutral.png"
image chara mayor furious = "mayor neutral.png"
image chara mayor laughing = "mayor neutral.png"
image chara mayor surprised = "mayor neutral.png"
image chara mayor gollum = "mayor neutral.png"
image chara kid neutral = "kid neutral.png"
image chara bessie neutral = "bessie neutral.png"

image chara girl neutral = "girl neutral.png"
image chara farmer neutral = "farmer neutral.png"

image whisky = "whisky.png"
image metal detector = "mine_detector.png"
image axe = "axe.png"
image batteries = "battery.png"
image chest = "briefcase.png"
image cents5 = "cents5.png"
image cents10 = "cents10.png"
image cents15 = "cents15.png"
image cents20 = "cents20.png"
image paper = "paper.png"
image hotcoin = "hotcoin.png"

image chara monster = "monster.png"

#
# GAME STARTS HERE
#

# First, we ask the player their name.
label start:

    scene bg intro1
    with fade
    "Hello and thank you for trying out our prototype! (click to move forward)"
    "What is your name?"
    menu:
        "My name is Derek.":
            $ player_name = "Derek"
        "My name is John.":
            $ player_name = "John"
        "My name is Samantha.":
            $ player_name = "Samantha"
        "My name is Shawn.":
            $ player_name = "Shawn"
        "My name is Lauryn.":
            $ player_name = "Lauryn"
        "Just call me \"Player\".":
            $ player_name = "Player"
        "My name is... (choose your own name)":
            $ player_name = renpy.input("My name is...")
            $ player_name = player_name.strip()
            if player_name=="":
                "Don't want to give a name after all, eh?"
                "Fine. You shall be called..."
                "\"Generic_name_01!\""
                $ player_name="generic_name_01"
        "My name is none of your business.":
            $ player_name = "Mr. Poopybutts"
            "...!"
            "Very well, have it your way."
            "For the duration of this game, you shall be called..."
            "Mr. Poopybutts."
    "Pleasure to make your acquaintance, [player_name]!"
    "Let's get started..."
    "On Aug 15th 1969, a group of really mellow dudes were organizing a music festival that was about to become the most famous festival ever."
    "The following is inspired by their stories."
    "Welcome to..."
    scene bg intro3
    with dissolve
    pause 6.0
    
    jump title

# The player is given a chance to change their name before starting the game
label title:


    if player_name=="Mr. Poopybutts":
        menu:
            "My name is Mr. Poopybutts. Let's start the game. (Start the game)":
                jump trailerstart
            "Actually, I think I made a mistake choosing my name. Let me go back. (Choose your name again)":
                jump start
    else:
        menu:
            "Let's start the game! (Start the game)":
                jump trailerstart
            "Actually, I think I made a mistake choosing my name. Let me go back. (Choose your name again)":
                jump start
