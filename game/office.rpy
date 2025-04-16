#
# OFFICE
#

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
    $ mayor_first_talk = False
    show chara mayor neutral
    with dissolve
    "As you open the door to the supervisor's office, you see him sitting behind his large desk."
    m "Oh hello [player_name]. I've been trying to reach you all morning."
    "Yes, I'm sorry, I—"
    m "Well it doesn't matter now. You see, I really can't afford for your festival to continue."

    menu:
        "What? Why not?":
            m "My constituents are giving me a lot of trouble."
            m "They're annoyed with all the hippies flooding the town. I have to look out for my people."
            m "Look, I know we promised that you wouldn't need a permit, but unfortunately that's not going to fly anymore."
            menu:
                "Okay, can I get a permit then?":
                    m "Sure you can."
                    m "Come in on Monday and fill out the form A-41-K and Z-53-C and we'll get you sorted in a month or two."
                    "...what?"
                    m "These things take time, you know?"
                    menu:
                        "You're fucking with me, right?":
                            "The supervisor leaps from his chair."
                            show chara mayor angry
                            m "How dare you, [player_name]!"
                            m "To imply that I have any skin in the game!"
                            m "I'm simply looking out for my voters!"
                            m "I mean my constituents!"
                            show chara mayor neutral
                            with dissolve
                            "The supervisor walks back to his desk and sits down."
                            m "I apologise for my outburst."
                            jump townhall_first_dialogue_second_part
                        "Oh... ok then.":
                            m "I truly am sorry, [player_name]."
                            m "It's just, I have to look out for my voters."
                            m "I mean my constituents."
                            jump townhall_first_dialogue_second_part          
                "Sure, we'll pack our stuff and leave town.":
                    show chara mayor laughing with dissolve
                    "The supervisor is visibly pleased that his negotiation tactics have worked so effectively on you."
                    m "Ha! Good! I'll give you and your crew a couple of hours to pack up your things and leave town."
                    m "See Sam? That's how it's done!"
                    show chara assistant neutral
                    with dissolve
                    "The supervisor's assistant does not respond, but he gives a quick glance at you before going back to re-organizing his filing cabinet."
                    "You head for the door, feeling quite defeated."
                    jump townhall
        "Sure, that's alright. We'll start packing everything up.":
            m "Good! I need your guys of here by 8 o'clock today."
            m "I really appreciate your understanding [player_name]."
            "The supervisor gives you one final look."
            "The conversation seems to be over. You head for the door."
            jump townhall


label townhall_first_dialogue_second_part:
    menu:
        "Wait. Your voters?":
            m "Well you got me. As you probably know, it's election season."
            m "I can't do anything to risk my reputation."
            jump mayor_negotiation
        "(Say nothing)":
            m "Well, good."
            m "I need your guys to be packed up by eight o'clock."
            m "Once again, I'm sorry, [player_name]."
            "The supervisor gives you one final look."
            "The conversation seems to be over. You head for the door."
            jump townhall

# Negotiating with the mayor


label mayor_negotiation:


menu:
    "I can donate to your campaign.":
        m "Unfortunately, whatever you can give won't be enough."
        m "It's not money I need, it's my voters' trust."
        m "You need to leave."
        jump townhall
    "I will give you the finest colombian powder if you let us stay." if negotiation_drugs == False:
        "The mayor is not exactly thrilled by this proposition."
        "Before you have a chance to say anything else, you are being escorted out of the town hall by two big men with even bigger shotguns."
        $ negotiation_drugs = True
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
        jump townhall
    "I will join the local church and devote my life to serving the Almighty if you let us stay." if negotiation_faith == False:
        m "What the hell are you trying to pull here, huh? You and your crew better git on out of here before I call the sheriff on your ass!"
        m "You think it's funny to make fun of other people's faith?!"
        m "This meeting is over!"
        "You decide it's best to leave."
        $ negotiation_faith = True
        jump townhall

# Townhall second dialogue


label townhall_second_dialogue:
    "You enter the office. The town supervisor seems surprised to see you again."
    m "Was there something you needed, [player_name]?":
    menu:
        "Your voters, huh?":
            m "Uh?! What do you mean?"
            "You mentioned your voters earlier"
            "The town supervisor falls silent."
            m "Well you got me. As you probably know, it's election season."
            m "I can't do anything to risk my reputation."
            jump mayor_negotiation
        "Sorry, I was just about to leave.":
            jump townhall

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
