#
# DEFINING PARAMETERS
#

# Characters
define p = Character("[player_name]")
define m = Character("Mayor of Bethel", color="#cf112b")
define t = Character("Larry the Technician", color="#9c341e")
define a = Character("Mayor's Assistant", color="#a6a6a6")
define c = Character("Cosmic Being", color="#4a1ea2")
default player_name = "Player"

# Is the player starting the game? (Determines if the intro text is displayed in the starting area)
default first_play = True

# Has the player talked to the technician? (Determines if the technician explains the situation when first talking to him)
default technician_first_talk = True

# Has the player talked to the mayor? (Determines if the mayor gives his angry rant)
default mayor_first_talk = True

# Has the player mentioned gold to the mayor, making him happy to see the player? (No gameplay effect, just changes the tone when visiting the mayor's office a second time)
default mayor_wants_gold = False

# Has the player picked up the metal detector from the trailer? (Determines if it's possible to find items in the backstage area)
default have_metal_detector = False

# Has the player found 4 coins in the backstage area? (The player needs to pick up 4 coins before the battery runs out)
default have_coin = False
default have_coin2 = False
default have_coin3 = False
default have_old_coin = False

# Has the player seen the vending machine? (Determines if it's possible to ask Larry for money)
default have_seen_vending_machine = False

# Has the player gotten a coin from Larry? (Determines if it's possible to get the batteries from the vending machine)
default have_larry_coin = False

# The amount of money player has to buy the batteries and if they have bought them (Batteries needed to get gold bar from backstage area)
default cents = 0
default have_batteries = False

# Has the player found the chest in the backstage area? (Needed to be done before it's possible to find gold)
default have_chest = False

# Has the player found the gold bar? (Needs to be given to the mayor to make him happy)
default have_gold = False

# Has the player given the gold bar to the mayor? (Unlocking the neutral ending)
default mayor_happy = False

# Has the player solved "the mayor problem", causing Larry to be happy (No gameplay change except unlocking the neutral ending)
default technician_happy = False

# Has the player talked to Larry to get his piece of paper? (Needed to unlock safe)
default have_paper = False

# Has the player found the stone in the safe? (Needed to travel to the dreamworld)
default mystical_stone = False

# Has the player killed the monster in the dreamworld? (Unlocks the best ending)
default monster_dead = False

# Determines how many times the player has clicked the different options in the starting "fourth-wall breaking joke"
default exit_fight_dialogue_points = 0

# Determines if the safe is empty (so that nothing more can be found in the mayor's office)
default safe_empty = False

# After 10 tries of finding nothing in the backyard area, an easter egg is found
default egg_counter = 0

# Has the player punched the vending machine?
default punched_machine = False

# Which dialogue options the player has already chosen during the mayor negotiation?
default negotiation_drugs = False
default negotiation_faith = False

#
# GAME STARTS HERE
#

# First, we ask the player their name.


label start:


    "Hello and thank you for trying out our prototype!"
    "What is your name?"
    menu:
        "My name is Derek.":
            $ player_name = "Derek"
        "My name is Eliza.":
            $ player_name = "Eliza"
        "My name is Jonatan.":
            $ player_name = "Jonatan"
        "My name is Juha.":
            $ player_name = "Juha"
        "My name is Tuukka.":
            $ player_name = "Tuukka"
        "Just call me \"Player\".":
            $ player_name = "Player"
        "My name is... (choose your own name)":
            $ player_name = renpy.input("My name is...")
            $ player_name = player_name.strip()
            if player_name=="":
                "Don't want to give a name after all, eh?"
                "Fine. You shall be called..."
                "\"Generic_gender-neutral_name_01!\""
                $ player_name="generic_name_01"
        "My name is none of your business.":
            $ player_name = "Mr. Poopybutts"
            "...!"
            "Very well, have it your way."
            "For the duration of this game, you shall be called..."
            "Mr. Poopybutts."
    "Pleasure to make your acquaintance, [player_name]!"
    "You shall now be released in to the world and allowed to start the game."
    "We hope that you will enjoy your time with..."
    "\"Woodstock Game Prototype 1.0\"!"
    "(Try to imagine a mind-blowing intro sequence here)."
    jump title

# The player is given a chance to change their name before starting the game (unless their name is "Mr. Poopybutts")


label title:


    if player_name=="Mr. Poopybutts":
        menu:
            "My name is Mr. Poopybutts. Let's start the game. (Start the game)":
                jump starting_screen
    else:
        menu:
            "Let's start the game! (Start the game)":
                jump starting_screen
            "Actually, I think I made a mistake choosing my name. Let me go back. (Choose your name again)":
                jump start

# After the starting set-up, the game properly begins


label starting_screen:


    if first_play==True:
        scene bg trailer
        with fade
        "It is the morning of August 15th, 1969."
        "You wake up hungover in your trailer and look around a bit."
        "Last night's launch party was really quite something..."
        "Quick flashbacks from various scenes of debauchery appear in your mind."
        "You eventually get up from your bed and put on some clothes."
        $ first_play = False
    menu:
        "Look around":
            "As you make your way towards the door, you notice a note taped to your wall."
            "Someone has left a message for you."
            "\"[player_name]! I need to talk to you ASAP! It looks like we're not going to be able to go forward with the festival after all! Come talk to me backstage as soon as you wake up.\""
            "The note has been signed by \"Larry\"."
            "You have a faint memory of hiring someone named Larry to be the lighting technician for the stage..."
            jump starting_screen
        "Okay, let's get out there and get stuff done. (Leave the trailer)":
            jump map_screen
        "Wait, who am I?":
            "Your name is [player_name], and you are the producer in charge of putting together the Woodstock Music Festival."
            menu:
                "Look around":
                    "As you make your way towards the door, you notice a note taped to your wall."
                    "Someone has left a message for you."
                    "\"[player_name]! I need to talk to you ASAP! It looks like we're not going to be able to go forward with the festival after all! Come talk to me backstage as soon as you wake up.\""
                    "The note has been signed by \"Larry\"."
                    jump starting_screen
                "Oh, okay then. Well, let's get going! (Leave your trailer)":
                    jump map_screen
                "Huh? What is \"The Woodstock Music Festival\"":
                    "The Woodstock Music and Art Fair, commonly referred to as Woodstock, was a music festival held from August 15 to 18, 1969, on a dairy farm in Bethel, New York, 40 miles (65 km) southwest of the town of Woodstock."
                    "Billed as \"An Aquarian Exposition: 3 Days of Peace & Music\" and alternatively referred to as the Woodstock Rock Festival, it attracted an audience of more than 460,000."
                    "Thirty-two acts performed outdoors despite overcast and sporadic rain. It was one of the largest music festivals in history and became synonymous with the counterculture of the 1960s."
                    "The festival has become widely regarded as a pivotal moment in popular music history, as well as a defining event for the silent and baby boomer generations."
                    menu:
                        "Look around":
                            "As you make your way towards the door, you notice a note taped to your wall."
                            "Someone has left a message for you."
                            "\"[player_name]! I need to talk to you ASAP! It looks like we're not going to be able to go forward with the festival after all! Come talk to me backstage as soon as you wake up.\""
                            "The note has been signed by \"Larry\"."
                            jump starting_screen
                        "Cool! Well, let's get going. (Leave your trailer)":
                            jump map_screen
                        "This game seems dumb. I don't think I'm interested in playing this anymore.":
                            "..."
                            "Um, okay..."
                            "You just started."
                            jump exit_fight_dialogue

# Fourth wall breaking joke


label exit_fight_dialogue:


    "Are you saying you want to quit the game now?"
    menu:
        "Yeah, this bird is baked. Let me out.":
            "Sorry, I couldn't quite hear you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "Yeah man, I'm one toke over the line. Let me off this trip.":
            "Sorry, I couldn't quite hear you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "I'm afraid my prefrontal cortex has had quite enough now. Leave me be, thank you.":
            "Sorry, I couldn't quite hear you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "En jaksa enää. Haluan poistua juomaan viinaa. Nyt.":
            "Sorry, I couldn't quite understand you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "Ja, jag skulle vilja gå av den här resan nu, tack.":
            "Sorry, I couldn't quite understand you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "Ja, ich möchte diese Reise jetzt beenden, danke.":
            "Sorry, I couldn't quite understand you. Could you repeat that, please?"
            $ exit_fight_dialogue_points += 1
            jump exit_fight_dialogue
        "What I actually meant was that I'd like to keep playing this remarkable work of art that you so foolishly insist on referring to simply as \"the game\"." if exit_fight_dialogue_points>=5:
            "Really?! Oh that's so great to hear that you like the game!"
            "Of course, we'll let you get on with the game now!"
            "Have fun!"
            jump map_screen

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

#
# TOWN HALL
#


label townhall:


    scene bg townhall
    with fade
    menu:
        "Go to the mayor's office":
            if mayor_first_talk==True:
                jump townhall_first_dialogue
            elif mayor_happy==False:
                jump townhall_second_dialogue
            else:
                jump townhall_third_dialogue     
        "Look around":
            jump townhall_items
        "Leave":
            jump map_screen

# Townhall first dialogue


label townhall_first_dialogue:


    scene bg office
    with fade
    show mayor neutral
    with dissolve
    "As you open the door to the mayor's office, you see the mayor himself sitting behind his large desk."
    "He seems to be in the middle of a rather heated rant about something."
    m "Yes, that no-good bunch of draft-dodgers! They'll be thrown out of here as soon as Douglas and his boys come back from..."
    "The mayor stops himself mid-sentence as you enter the room."
    show mayor angry
    with dissolve
    m "[player_name]!"
    m "You ever heard of knocking before entering?!"
    m "You think it's any of your business what I talk about with my assistant?!"
    "You see another man in the room, sitting behind a much smaller desk."
    hide mayor angry
    with dissolve
    show assistant neutral
    with dissolve
    "A bespectacled man quietly gazes at you. After a moment, he turns away and starts to sort through a pile of papers on his desk."
    hide assistant neutral
    with dissolve
    show mayor angry
    with dissolve
    "The mayor gets up from his chair and walks over to you, visibly angry."
    m "You and me have a problem!"
    m "I don't want your festival here!"
    m "I want you and your ragged crew of hippies to pack up your stuff and leave!"
    menu:
        "What's the problem?":
            m "I... WE do not accept you coming here with your loud music and your drugs and your free love to destroy our beautiful town!"
            m "I want you people out of here by 8 o'clock today!"
            menu:
                "Who's \"we\"?":
                    m "Me! ...and the townsfolk!"
                    m "It's all of us! Together!"
                    m "We don't want you here, you hear me?!"
                    menu:
                        "Yeah yeah, I hear you. You don't want us here.":
                            m "That's right! And you better hear it well!"
                            show mayor neutral
                            with dissolve
                            "The mayor walks back to his desk and sits down."
                            m "Well then, it's good that we have a mutual understanding. Now if you'll excuse me, I have other things to attend to!"
                            "You see the mayor put up his feet to his desk and open up a magazine called \"Livestock Quarterly\"."
                            "There doesn't seem to be no more use in trying to talk to the mayor, so you head for the door."
                            $ mayor_first_talk = False
                            jump townhall
                        "To me, it sounds like this is more of a personal problem.":
                            m "A personal problem? What the hell are you talking about?!"
                            menu:
                                "I'm thinking that it's just you who has a problem with us.":
                                    show mayor furious
                                    with dissolve
                                    "The mayor suddenly goes red in the face."
                                    m "Now you listen to me you little shit! I am the mayor of this here fine town, and I'm telling you to get your stuff and LEAVE!!"
                                    m "I'm giving you one hour to pack up your stuff and after that one hour is done, I'm calling in the sheriff and you KNOW him and his boys are long overdue for some fine hootin' and tootin' action!"
                                    m "THIS MEETING IS OVER!"
                                    "Before you know it, you are being pushed out of the office. The mayor slams the door shut behind you."
                                    $ mayor_first_talk = False
                                    jump townhall
                                "Maybe we can find a solution that would prove to be beneficial for both parties? Especially for the... townsfolk?":
                                    "The mayor stares at you blankly for a second or two before giving a sideways glance to his assistant."
                                    hide mayor
                                    with dissolve
                                    show assistant neutral
                                    with dissolve
                                    "The mayor's assistant does not react in any way, nor does he return his boss' glance."
                                    hide assistant neutral
                                    with dissolve
                                    show mayor neutral
                                    with dissolve
                                    m "Erm... what exactly do you suggest?"
                                    jump mayor_negotiation             
                "Sure, we'll pack our stuff and leave town.":
                    show mayor laughing with dissolve
                    "The mayor is visibly pleased that his negotiation tactics have worked so effectively on you."
                    m "Ha! Good! I'll give you and your crew a couple of hours to pack up your things and leave town."
                    "The mayor walks back to his desk and triumphantly sits down on his chair."
                    m "See Sam? That's how it's done!"
                    hide mayor
                    with dissolve
                    show assistant neutral
                    with dissolve
                    "The mayor's assistant does not respond, but he gives a quick glance at you before going back to re-organizing his filing cabinet."
                    "You head for the door, feeling quite defeated."
                    hide assistant
                    with dissolve
                    $ mayor_first_talk = False
                    jump townhall
        "Sure, that's alright. We'll start packing everything up.":
            m "Good! I want you out of here by 8 o'clock today!"
            "The mayor gives you one final nasty look and goes back to his desk."
            "The conversation seems to be over. You head for the door."
            $ mayor_first_talk = False
            jump townhall

# Negotiating with the mayor


label mayor_negotiation:


menu:
    "I will give you the finest colombian powder if you let us stay." if negotiation_drugs == False:
        "The mayor is not exactly thrilled by this proposition."
        "Before you have a chance to say anything else, you are being escorted out of the town hall by two big men with even bigger shotguns."
        $ negotiation_drugs = True
        $ mayor_first_talk = False
        jump map_screen
    "I will find you a gold bar if you let us stay.":
        show mayor laughing
        with dissolve
        "The mayor bursts in to laughter."
        m "A gold bar? You're going to find me a gold bar from this here field of mud and horse droppings?"
        m "You hear that, Sam? He's going to find us a gold bar! Ha ha ha ha!!"
        hide mayor
        with dissolve
        show assistant neutral
        with dissolve
        "You see the mayors assistant continue his work, expressionless."
        hide assistant neutral
        with dissolve
        show mayor laughing
        with dissolve
        m "All right, that sounds good to me! You find me a gold bar and I'll let you people stay and do your little festival! Ha ha ha!"
        "With tears in his eyes from laughter, the mayor walks you to the door and bids you farewell."
        m "A gold bar, ha ha ha! Why don't you find me a goose that lays golden eggs while your at it? Ha ha ha!!"
        $ mayor_wants_gold = True
        $ mayor_first_talk = False
        jump townhall
    "I will join the local church and devote my life to serving the Almighty if you let us stay." if negotiation_faith == False:
        m "What the hell are you trying to pull here, huh? You and your crew better git on out of here before I call the sheriff on your ass!"
        m "You think it's funny to make fun of other people's faith?!"
        m "This meeting is over!"
        "You decide it's best to leave."
        $ negotiation_faith = True
        $ mayor_first_talk = False
        jump townhall
    "I will let you have a night with some of the more \"fair\" members of our crew if you let us stay.":
        m "Dear lord..." 
        m "I knew you were a drug-using satanist but I didn't think you were THIS deranged!"
        m "This is how your little crew operates huh? You pimp out your crew members to get what you want?!"
        m "I'm calling the sheriff right now. We're going to put you behind bars and make sure you never get out!"
        "The mayor procures a shiny revolver from his desk drawer."
        "It seems you have made a slight error in judgement."
        jump jail_ending

# Townhall second dialogue


label townhall_second_dialogue:


    scene bg office
    with fade
    "You enter the office. Immediately the mayor's eyes are on you."
    if mayor_wants_gold==False:
        show mayor angry
        with dissolve
        "He doesn't seem happy to see you."
        m "What the hell are you doing back here?! I thought I told you to leave!"
        m "GET OUT!"
        menu:
            "Wait! Maybe we can work something out!":
                m "Huh?! You better start talking, fast!"
                jump mayor_negotiation
            "Sorry, I was just about to leave.":
                jump townhall
    else:
        show mayor laughing
        with dissolve
        "The mayor starts laughing heartily."
        m "Ah, look who it is! My little golden retriever!"
        m "Well, any luck in finding a bar of gold in our little field?"
        menu:
            "Sorry, no luck yet.":
                m "Yes, well I'm not very surprised!"
                m "Keep digging, maybe one day you'll find an old coin you can pawn! Ha ha ha!"
                "You leave the mayor's office."
                jump townhall
            "Here's your bar of gold" if have_gold==True:
                jump gold_dialogue

# Talking about the bar of gold with the mayor


label gold_dialogue:
    "You show the mayor your bar of gold."
    show mayor surprised
    with dissolve
    "The mayors eyes widen and his expression goes blank."
    m "What is THAT?!"
    menu:
        "Here's a bar of gold for you.":
            m "Are you... what?!"
            m "Where did you find this?!"
            menu:
                "It doesn't really matter. Here, it's yours. (Give the bar of gold)":
                    show mayor laughing
                    with dissolve
                    m "YOU ACTUALLY FOUND A BAR OF GOLD?!"
                    m "Ha ha ha! I can't belive it!"
                    m "I'M RICH! I'M RICH, YOU HEAR ME?!"
                    hide mayor
                    with dissolve
                    "The mayor runs out of his office with the gold bar in his hands."
                    "Outside, you hear a car starting. A rumble of an engine is heard as the mayor drives far away in to the distance."
                    "Seems like the mayor won't be giving you any more trouble."
                    "As you make your way toward the door, you hear a light shuffle of footsteps behind you."
                    show assistant neutral
                    with dissolve
                    a "Looks like you managed to finally get rid of him. Congratulations."
                    a "You can have your festival. But make sure all of your guests and crew have left town by Monday afternoon."
                    a "Our little town has... important business to attend to, and we do not like to be interfered with."
                    a "Goodbye."
                    hide assistant neutral
                    with dissolve
                    "The mayor's assistant leaves the office."
                    "You follow him in to the hallway but he is nowhere to be seen."
                    "You wonder about the assistant for a moment, but then decide to make your way outside."
                    $ mayor_happy = True
                    $ have_gold = False
                    jump map_screen
                "I found it in your mother's bed. And you know what? I'm not going to give you this.":
                    m "No! It is mine!"
                    "Before you know it, the mayor has snatched the bar of gold from your hand."
                    m "It is..."
                    show mayor gollum
                    with dissolve
                    m "My precious..."
                    hide mayor
                    with dissolve
                    "The mayor runs out of his office with the gold bar in his hands."
                    "Outside, you hear a car starting. A rumble of an engine is heard as the mayor drives far away in to the distance."
                    "Seems like the mayor won't be giving you any more trouble."
                    "As you make your way toward the door, you hear a light shuffle of footsteps behind you."
                    show assistant neutral
                    with dissolve
                    a "Looks like you managed to finally get rid of him. Congratulations."
                    a "You can have your festival. But make sure all of your guests and crew have left town by Monday afternoon."
                    a "Our little town has... very important business to attend to, and we do not like to be interfered with."
                    a "Goodbye."
                    hide assistant neutral
                    with dissolve
                    "The mayor's assistant leaves the office."
                    "You follow him in to the hallway but he is nowhere to be seen."
                    "You wonder about the assistant for a moment, but then decide to make your way outside."
                    $ mayor_happy = True
                    $ have_gold = False
                    jump map_screen
        "Oops, actually it's nothing. Never mind.":
            "You hide the bar of gold from the mayor's view and decide to quickly make your way towards the door."
            jump townhall        

# Town hall empty room with safe


label townhall_third_dialogue:


    scene bg office
    with fade
    menu:
        "Look around":
            if safe_empty==False:
                "You find a small safe hidden behind one of the filing cabinets."
                menu:
                    "Try to enter a code for the lock.":
                        jump safe
                    "Leave the safe alone.":
                        jump townhall_third_dialogue
            else:
                "As you have emptied the safe, there is nothing more of interest in the room."
                jump townhall_third_dialogue
        "Leave":
            jump townhall

# Safe mechanics


label safe:


    scene bg safe
    with fade
    menu:
        "Enter \"1967\"":
            "Nothing happens."
            jump safe
        "Enter \"1968\"":
            "Nothing happens."
            jump safe
        "Enter \"1969\"" if have_paper==True:
            "The safe clicks and opens."
            "Inside, you find a small glowing stone."
            "As you grab the stone a dark, dangerous feeling comes over you."
            "For some reason, you start to feel quite sleepy."
            $ mystical_stone = True
            "You close the door of the safe and leave."
            $ safe_empty = True
            jump townhall 
        "Enter \"1970\"":
            "Nothing happens."
            jump safe
        "Leave the safe alone":
            jump townhall_third_dialogue

# Town hall searching for items


label townhall_items:


    if have_batteries==False:
        "The corridors of the town hall don't seem to contain much more than a single vending machine. The only item left for sale is a pack of batteries."
        jump vending_machine
    else:
        "The corridors of the town hall don't seem to contain much more than a single vending machine, which is now empty."
        jump townhall

# Town hall vending machine


label vending_machine:


    $ have_seen_vending_machine = True
    menu:
        "Press the button for the batteries":
            "The display of the vending machine flashes \"50 cents\"."
            menu:
                "Insert 50 cents in to the machine":
                    if cents<50:
                        "You only have [cents] cents."
                        jump vending_machine
                    elif cents==50:
                        "You insert 50 cents in to the machine."
                        "The machine spits out the pack of batteries, and you pick them up."
                        $ have_batteries = True
                        jump townhall
                "Leave":
                    jump townhall
        "Punch the machine" if punched_machine==False:
            "You punch the machine, and a single coin drops from the coin-return slot."
            "You pick up the coin."
            "One one side of the coin, it says \"ONE CAR WASH\"."
            "On the other side, there is a logo of a car on fire and underneath a text, \"Texas Pete's Flaming Hot Car Wash\"."
            "Although you aren't sure what you'll do with it, you take the car wash token with you."
            $ punched_machine = True
            jump vending_machine
        "Leave":
            jump townhall

#
# BACKSTAGE
#


label backstage:


    scene bg backstage
    with fade
    menu:
        "Talk to Larry the Technician":
            if technician_first_talk==True:
                jump backstage_dialogue
            else:
                jump backstage_dialogue_second
        "Look around":
            jump backstage_items
        "Leave":
            jump map_screen

# Backstage first dialogue


label backstage_dialogue:


    $ technician_first_talk = False
    if technician_happy==False:
        show technician frightened
        with dissolve
        t "[player_name]! You finally woke up!"
        t "We have a huge problem!"
        t "The mayor came by this morning and was yelling at everyone, looking for you."
        t "He's saying that he won't allow the festival to go on!"
        t "And even worse..."
        t "I'M OUT OF BEER!"
        t "What are we going to do?!"
    elif technician_happy==True:
        show technician happy 
        with dissolve
        t "Hey [player_name]! Are you ready to start the festival?"
        menu:
            "Yep, let's get this show started! (End the day)":
                jump ending
            "Not just yet. Let me check on a couple of things first. (Leave)":
                jump backstage
    menu:
        "I'll go talk to the mayor. I'm sure we'll figure something out." if mayor_happy==False:
            t "Alright, that sounds like a good plan. Good luck!"
            jump backstage
        "Screw the mayor. We'll continue forward with the festival." if mayor_happy==False:
            "Larry looks shocked."
            t "Are you sure?! He said he's going to come in here with the sheriff and shut everything down by force if we don't leave by 8 o'clock!"
            menu:
                "Yes I'm sure. C'mon, let's get this show started! (End the day)":
                    jump ending
                "Hmm... maybe it's better to go talk to him first.":
                    t "Yes, I think that's a good idea! Good luck!"
                    "You leave Larry alone as he lights up a cigarette with shaking hands."
                    jump backstage 
        "The mayor won't be a problem for us anymore." if mayor_happy==True:
            $ technician_happy = True
            show technician happy  
            with dissolve
            t "Really? That's great news!"
            t "So, do you want to start the festival then?"
            menu:
                "Yeah, let's get this show started! (End the day)":
                    jump ending
                "Nah, let me actually make sure everything is in order before we start.":
                    t "Okay, sounds good. Let me know when you're ready to start the festival!"
                    jump backstage

# Backstage second dialogue


label backstage_dialogue_second:


    if technician_happy==False:
        show technician frightened
        with dissolve
        t "[player_name]! Did you go talk to the mayor yet?"
    elif technician_happy==True:
        show technician happy 
        with dissolve
        if have_paper==False:
            t "Hey [player_name]! Thanks for taking care of that business with the mayor!"
            t "I have a gift for you as a thank you!"
            "Larry hands you a folded piece of paper."
            "You unfold the paper and see that \"1969\" is written on it."
            $ have_paper = True
            menu:
                "Why are you giving me a piece of paper that has the current year written on it?":
                    t "Time is relative, man! This will help you remember what year it is in case you forget!"
                    t "Alright, I have to go check that the ungrounded stage cables aren't submerged in puddles again."
                    t "Later, man!"
                    jump backstage
                "This is just what I needed, thanks!":
                    t "No problemo, man!"
                    jump backstage
        else:
            t "Hey [player_name]! Are you ready to start the festival?"
            menu:
                "Yep, let's get this show started! (End the day)":
                    jump ending
                "Not just yet. Let me check on a couple of things first. (Leave)":
                    jump backstage
    menu:
        "Not yet. I'll go do that now." if mayor_first_talk==True:
            t "Alright, good luck!"
            jump backstage
        "Screw the mayor. We'll continue forward with the festival." if mayor_happy==False:
            "The stage manager looks frightened."
            t "Are you sure?! He said he's going to come in here with the sheriff and shut everything down by force if we don't leave by 8 o'clock!"
            menu:
                "Yes I'm sure. C'mon, let's get this show started! (End the day)":
                    jump ending
                "Hmm... maybe it's better to go talk to him first.":
                    t "Yes, I think that's a good idea! Good luck!"
                    "You leave the stage manager as he lights up a cigarette with shaking hands."
                    jump backstage
        "Hey Larry do you want this bar of gold?" if have_gold==True:
            t "Nah I'm good, man."
            t "Thanks anyway."
            jump backstage
        "Do you happen to have some extra change on you?" if have_seen_vending_machine==True:
            if have_larry_coin==False:
                t "Uh... I don't really believe in money, man..."
                t "But here, I found this in the pocket of these sweet pants!"
                "Larry hands you a coin worth ten cents."
                $ have_larry_coin = True
                $ cents += 10
                menu:
                    "Thanks!":
                        t "No problem, man!"
                        jump backstage
                    "...are those not your pants?":
                        t "Whoa man!"
                        t "That's kind of a capitalist mentality if you ask me!"
                        t "I mean do we really ever \"own\" anything??"
                        menu:
                            "You're totally right. Nobody really \"owns\" anything. Especially when it comes to copyrighted music some students might want to use for their video game course project.":
                                t "Right on, man!"
                                jump backstage
                            "I guess that means you don't need to get paid for this gig.":
                                "You decide there are more important matters than a lengthy discussion about the nature of ownership to focus on right now. You thank Larry for the coin and leave."
                                jump backstage
            else:
                t "Nah, I have no more coins on me, man."
                t "I thought you were supposed to be good with money? How come you're totally broke?"
                menu:
                    "I'm not \"totally broke\"!":
                        t "I think you are if you're asking me for change..."
                        "You decide it's better to immediately end the conversation and leave."
                        jump backstage
                    "I made some bad investments.":
                        t "Yeah man, it happens!"
                        t "My brother and I went to the casino last year..."
                        t "I don't really know how the whole thing works, but my brother told me that if the ball lands on the red square two times in a row, the next time it'll land on the black one for sure!"
                        t "So, we eventually lost our mom's house..."
                        "You decide it's better to not continue this conversation any longer."
                        jump backstage
        "Yes, I talked to him. Don't worry, I'll get it sorted." if mayor_first_talk==False:
            t "O-okay! Let me know if anything changes!"
            jump backstage    
        "The mayor won't be a problem for us anymore." if mayor_happy==True:
            $ technician_happy = True
            show technician happy  
            with dissolve
            t "Really? That's great news!"
            t "So, do you want to start the festival then?"
            menu:
                "Yeah, let's get this show started! (End the day)":
                    jump ending
                "Nah, let me actually make sure everything is in order before we start.":
                    t "Okay, sounds good. Let me know when you're ready to start the festival!"  
                    jump backstage

# Backstage search


label backstage_items:
    
    
    if have_metal_detector==False:
        "You look around the discarded cardboard boxes and other pieces of garbage that permeate the backstage area."
        "There doesn't seem to be anything of interest here."
        jump backstage
    else:
        menu:
            "Use your metal detector":
                if egg_counter >= 11:
                    "You have walked through the whole backstage area with your metal detector. There doesn't seem to be anything more to find."
                    jump backstage_items
                elif have_old_coin==True:
                    if have_batteries==False:
                        "Your metal detector seems to have run out of batteries."
                        jump backstage_items
                    elif have_batteries==True:
                        if have_chest==False:
                            "You change the batteries of your metal detector for new ones. Suddenly the machine seems to beep with newfound vigour."
                            "Something heavy hides beneath the mud of the backstage area."
                            "You plunge your hands in to the mud, using your fingers to find the edges of the object." 
                            "Finally your hands find something that you can grab on to firmly."
                            "You pull with all your strength, and you manage to get the object out of the mud."
                            "It is an old chest."
                            "It has been waiting for decades for someone to finally unearth it."
                            "As you break the lock, visions of vast riches fill your mind."
                            "What could be inside?"
                            "What will you buy with all of the riches that are contained within?"
                            "Finally, you will be free from this eternal hell of organizing music festivals for a pittance!"
                            "You'll be able to achieve all your dreams!"
                            "You'll be able to go back home to your parents and declare \"Yes, I have returned! And I have come back to you a success!\""
                            "You open up the chest."
                            "Inside, you see..."
                            "(To accesss this content, you need to purchase the \"Motherlode Add-On Content Pack\")"
                            "(Only $29.99)"
                            "(Restrictions apply)"
                            $ have_chest =  True
                            jump backstage
                        if have_gold==False:
                            "You dig around and find a bar of gold!"
                            $ have_gold = True
                            $ egg_counter += 1
                            jump backstage_items
                        elif egg_counter==10:
                            "You dig around and find an easter egg!"
                            "Doesn't seem like you can do anything with it though..."
                            $ egg_counter += 1
                            jump backstage_items
                        elif egg_counter>0:
                            "You dig around but find nothing."
                            $ egg_counter += 1
                            jump backstage_items   
                else:
                    "You walk around the backstage area until your metal detector beeps."
                    if have_coin==False:
                        "You dig around and find a small coin!"
                        "This one is worth 25 cents."
                        $ cents += 25
                        $ have_coin = True
                        jump backstage_items
                    elif have_coin2==False:
                        "You dig around and find a small coin!"
                        "This one is worth five cents."
                        $ cents += 5
                        $ have_coin2 = True
                        jump backstage_items
                    elif have_coin3==False:
                        "You dig around and find a small coin!"
                        "This one is worth ten cents."
                        $ cents += 10
                        $ have_coin3 = True
                        jump backstage_items
                    elif have_old_coin==False:
                        "You dig around and find a small coin!"
                        "This one seems to be late Anglo-Saxon, from the first half of the eleventh century."
                        "It is quite obvious that it is from the reign of Cnut the Great (c. 990 - 1035) instead of Aethelred I of Wessex (c. 845 - 871), since it has been minted in Cambridge around the year 1000 AD."
                        "Of course, another obvious sign that it is from the reign of Cnut is that the obverse of the coin depicts a \"pointed helmet\" style of portrait, a trademark of Cnut's."
                        "But since you aren't particulary interested in old coins, you throw it away."
                        $ have_old_coin = True
                        jump backstage_items   
            "Leave the area":
                jump backstage

#        
# TRAILER
#


label trailer:


    scene bg trailer
    with fade
    menu:
        "Rest a bit":
            "You lay down and relax for a moment."
            "Time passes."
            "You feel rested."
            menu:
                "Keep resting":
                    "You keep relaxing for a bit more."
                    "Time passes."
                    "You feel more rested."
                    menu:
                        "Try to fall asleep.":
                            "(Don't you have a festival to save?)"
                            "You try to fall asleep."
                            "Time passes."
                            "You succesfully stare at the ceiling for some time."
                            if mystical_stone==True:
                                if monster_dead==False:
                                    menu:
                                        "Try to fall asleep one more time.":
                                            "You fall in to a deep, eternal slumber."
                                            jump monster_battle
                                        "Get up":
                                            jump trailer
                                else:
                                    menu:
                                        "Get up":
                                            jump trailer
                            else:
                                menu:
                                    "Get up":
                                        jump trailer
                        "Get up":
                            jump trailer
                "Get up":
                    jump trailer
        "Look around":
            if have_metal_detector==False:
                "Your trusty metal detector lies abandoned under your bed."
                menu:
                    "Take the metal detector":
                        "You take the well-used metal detector with you."
                        $ have_metal_detector = True
                        jump trailer
                    "Leave the metal detector":
                        "You leave the metal detector to its fate."
                        jump trailer
            else:            
                "Apart from a half-eaten hot-dog and an unopened pack of condoms that is past its expiry date, there is nothing here."
                jump trailer
        "Leave":
            jump map_screen

#
# DREAMWORLD MONSTER BATTLE
#


label monster_battle:


    scene bg monsterlair
    with fade
    "You wake up in some sort of alternative dimension."
    "Suddenly, you hear a voice in the distance."
    show monster
    with dissolve
    "A large entity that cannot be described by words appears before you."
    "You feel your lifeforce being sapped away by this unimaginable being as you try to find the right words."
    c "Y'ai 'ng'ngah, Yog-Sothoth h'ee - l'geb f'ai throdog uaaah."
    menu:
        "You are my master, and I give my life to thee.":
            "Slowly, the creature feeds on your spirit. You slip in to an endless darkness."
            "You are dead."
            jump death
        "What are you, some kind of stupid man-squid?":
            "You hear a voice that seems to be coming from inside your head."
            c "Insolent fool. You wish to challenge my power? I have lived since the beginning, before your kind even had developed ears or eyes."
            c "You will bow before my power. I shall feed on your kind for an eternity."
            menu:
                "Please don't kill me.":
                    "Slowly, the creature feeds on your spirit. You slip in to an endless darkness."
                    "You are dead."
                    jump death
                "I think you look kind of dumb.":
                    c "How dare you. You are an insignificant speck of matter. I will never stop feasting on you. You will suffer for a thousand generations."
                    menu:
                        "I didn't mean it. Don't kill me. Please.":
                            "Slowly, the creature feeds on your spirit. You slip in to an endless darkness."
                            "You are dead."
                            jump death
                        "You fight like a dairy farmer!":
                            c "How appropriate. You fight like a cow!"
                            "The creature's fierce comeback causes the flesh from your bones to evaporate instantly."
                            "You are dead."
                            jump death

                        "u r dumb lol":
                            "The creature in front of you recoils in horror at this insult. You start to feel your lifeforce returning to you."
                            "Over in the infinite distance, the creature seems to scream in anger."
                            "White flames envelop the creature as it makes a sound that seems to continue to echo forever."
                            hide monster
                            with dissolve
                            "Soon, nothing of the creature remains but a blob of dark matter."
                            $ monster_dead = True
                            "With the creature gone, you feel your consciousness shift back in to your corporeal body."
                            jump trailer

#
# DETERMINING WHICH ENDING HAPPENS
#


label ending:


    if mayor_happy==False:
        jump bad_ending
    elif monster_dead==False:
        jump neutral_ending
    else:
        jump good_ending


label bad_ending:


    scene bg bad_ending
    with fade
    "The festival is started."
    "However, before the gates are even opened, the sheriff and his boys arrive in their pick-up trucks."
    "They start rounding up and beating on the festival guests."
    "The festival is shut down and your reputation as a festival organizer is destroyed."
    "You end up paying for various legal and medical fees for the rest of your life."
    "If you had insurance, it would have covered all damages."
    "As it stands, Woodstock Music Festival disappears in to the waves of history."
    "56 years from now, no-one remembers what happened on that weekend of August 15th to 18th, 1969."
    "Game Over. (Ending C)"
    return


label neutral_ending:


    scene neutral_ending
    with fade
    "The festival is started."
    "Everything goes according to plan and the festival is a great success."
    "More than 460,000 people visit the festival over the weekend."
    "The music and the political message of the festival attains a mythical status as a symbol of the 1960's counter-culture movement."
    "You are known as the person who made it all happen, and you spend the rest of your days organizing various successful music events."
    "In 2019, a podcast series gains popularity all over the world."
    "The series describes the history of Woodstock Music Festival and its cultural impact." 
    "The final episode of the series focuses on the mysterious disappearance of all the townspeople of Bethel following the festival weekend."
    "No rational reason is found as to how an entire town of 3,959 people can suddenly disappear between Monday 18th and Tuesday 19th of August, 1969."
    "Game Over. (Ending B)"
    return


label good_ending:


    scene good_ending
    with fade
    "The festival is started."
    "Everything goes according to plan and the festival is a great success."
    "More than 460,000 people visit the festival over the weekend."
    "The music and the political message of the festival reach a mythical status as a symbol of the 60's counter-culture movement."
    "You are known as the person who made it all happen, and you spend the rest of your days organizing various successful music events."
    "In 2019, a podcast series gains popularity all over the world."
    "The series describes the history of Woodstock Music Festival and its cultural impact." 
    "The final episode of the series describes how world peace was achieved following the festival weekend."
    "In interviews, numerous world leaders from the 1960's describe how they felt like \"a great malice\" had been removed from the world during Woodstock Music Festival."
    "Mankind has enjoyed a golden era of peace and prosperity for a thousand years now."
    "Game Over. (Ending A)"
    return


label jail_ending:


    scene bg jail
    with fade
    "You spend the rest of your days in jail."
    "(Seriously, what is wrong with you?)"
    "(Do you really think we would add this sort of stuff to our game?)"
    "(Shame on you!)"
    "(I'm sorry, but we have no choice but to make this a game over for you.)"
    "Game Over. (Ending D)"
    menu:
        "Try again":
            if mayor_first_talk==True:
                jump townhall_first_dialogue
            elif mayor_first_talk==False:
                jump townhall_second_dialogue
        "Exit game":
            return


label death:


    scene bg death
    with fade
    "Game Over. (Ending E)"
    menu:
        "Try again":
            jump monster_battle
        "Exit game":
            return