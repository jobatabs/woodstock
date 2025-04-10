#
# TOWN HALL
#

label townhall:
    scene black with wiperight

    show text "Town Hall" at truecenter with dissolve

    pause 1.0

    hide text with dissolve

    pause 0.3

    scene bg townhall
    with fade
    if townhall_first_visit==True:
        $ townhall_first_visit = False
        "The townhall is dusty and silent. You hear noises coming from the mayor's office."
    jump actionsmenu

label office:
    scene black with wiperight

    show text "Mayor's office" at truecenter with dissolve

    pause 1.0

    hide text with dissolve

    pause 0.3

    scene bg office
    with fade
    if mayor_first_talk==True:
        jump townhall_first_dialogue
    elif mayor_happy==False:
        jump townhall_second_dialogue
    else:
        jump townhall_third_dialogue

# Townhall first dialogue


label townhall_first_dialogue:
    show chara mayor neutral
    with dissolve
    "As you open the door to the mayor's office, you see the mayor himself sitting behind his large desk."
    "He seems to be in the middle of a rather heated rant about something."
    m "Yes, that no-good bunch of draft-dodgers! They'll be thrown out of here as soon as Douglas and his boys come back from..."
    "The mayor stops himself mid-sentence as you enter the room."
    show chara mayor angry
    with dissolve
    m "[player_name]!"
    m "You ever heard of knocking before entering?!"
    m "You think it's any of your business what I talk about with my assistant?!"
    "You see another man in the room, sitting behind a much smaller desk."
    show chara assistant neutral
    with dissolve
    "A bespectacled man quietly gazes at you. After a moment, he turns away and starts to sort through a pile of papers on his desk."
    show chara mayor angry
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
                            show chara mayor neutral
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
                                    show chara mayor furious
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
                                    show chara assistant neutral
                                    with dissolve
                                    "The mayor's assistant does not react in any way, nor does he return his boss' glance."
                                    show chara mayor neutral
                                    with dissolve
                                    m "Erm... what exactly do you suggest?"
                                    jump mayor_negotiation             
                "Sure, we'll pack our stuff and leave town.":
                    show chara mayor laughing with dissolve
                    "The mayor is visibly pleased that his negotiation tactics have worked so effectively on you."
                    m "Ha! Good! I'll give you and your crew a couple of hours to pack up your things and leave town."
                    "The mayor walks back to his desk and triumphantly sits down on his chair."
                    m "See Sam? That's how it's done!"
                    show chara assistant neutral
                    with dissolve
                    "The mayor's assistant does not respond, but he gives a quick glance at you before going back to re-organizing his filing cabinet."
                    "You head for the door, feeling quite defeated."
                    hide chara
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
        show chara mayor laughing
        with dissolve
        "The mayor bursts in to laughter."
        m "A gold bar? You're going to find me a gold bar from this here field of mud and horse droppings?"
        m "You hear that, Sam? He's going to find us a gold bar! Ha ha ha ha!!"
        show chara assistant neutral
        with dissolve
        "You see the mayors assistant continue his work, expressionless."
        show chara mayor laughing
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
    "You enter the office. Immediately the mayor's eyes are on you."
    if mayor_wants_gold==False:
        show chara mayor angry
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
        show chara mayor laughing
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
    show chara mayor surprised
    with dissolve
    "The mayors eyes widen and his expression goes blank."
    m "What is THAT?!"
    menu:
        "Here's a bar of gold for you.":
            m "Are you... what?!"
            m "Where did you find this?!"
            menu:
                "It doesn't really matter. Here, it's yours. (Give the bar of gold)":
                    show chara mayor laughing
                    with dissolve
                    m "YOU ACTUALLY FOUND A BAR OF GOLD?!"
                    m "Ha ha ha! I can't belive it!"
                    m "I'M RICH! I'M RICH, YOU HEAR ME?!"
                    hide chara
                    with dissolve
                    "The mayor runs out of his office with the gold bar in his hands."
                    "Outside, you hear a car starting. A rumble of an engine is heard as the mayor drives far away in to the distance."
                    "Seems like the mayor won't be giving you any more trouble."
                    "As you make your way toward the door, you hear a light shuffle of footsteps behind you."
                    show chara assistant neutral
                    with dissolve
                    a "Looks like you managed to finally get rid of him. Congratulations."
                    a "You can have your festival. But make sure all of your guests and crew have left town by Monday afternoon."
                    a "Our little town has... important business to attend to, and we do not like to be interfered with."
                    a "Goodbye."
                    hide chara
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
                    show chara mayor gollum
                    with dissolve
                    m "My precious..."
                    hide chara
                    with dissolve
                    "The mayor runs out of his office with the gold bar in his hands."
                    "Outside, you hear a car starting. A rumble of an engine is heard as the mayor drives far away in to the distance."
                    "Seems like the mayor won't be giving you any more trouble."
                    "As you make your way toward the door, you hear a light shuffle of footsteps behind you."
                    show chara assistant neutral
                    with dissolve
                    a "Looks like you managed to finally get rid of him. Congratulations."
                    a "You can have your festival. But make sure all of your guests and crew have left town by Monday afternoon."
                    a "Our little town has... very important business to attend to, and we do not like to be interfered with."
                    a "Goodbye."
                    hide chara
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
    "The office is empty."

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
        "Leave the office":
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


label looktownhall:


    if have_batteries==False:
        "The corridors of the town hall don't seem to contain much more than a single vending machine. The only item left for sale is a pack of batteries."
        jump vending_machine
    else:
        "The corridors of the town hall don't seem to contain much more than a single vending machine, which is now empty."
        jump actionsmenu

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
                        jump actionsmenu
                "Walk away from the vending machine":
                    jump actionsmenu
        "Punch the machine" if punched_machine==False:
            "You punch the machine, and a single coin drops from the coin-return slot."
            "You pick up the coin."
            "One one side of the coin, it says \"ONE CAR WASH\"."
            "On the other side, there is a logo of a car on fire and underneath a text, \"Texas Pete's Flaming Hot Car Wash\"."
            "Although you aren't sure what you'll do with it, you take the car wash token with you."
            $ punched_machine = True
            jump vending_machine
        "Walk away from the machine":
            jump actionsmenu
