#
# OFFICE
#

label office:
    scene black with wiperight

    show text "Town supervisor's office" at truecenter with dissolve

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
    m "Ah, [player_name]! How are you doing?"
    p "I'm good. What's this about a permit?"
    m "Right..."
    m "Well, I'm afraid the situation has changed a bit with the townsfolk."

    menu:
        "Ask how the situation has changed":
            p "Okay? How so?"
            m "Well, the people of Bethel have decided that our community does not want a big hippie festival to happen here."
            menu:
                "Ask about the sudden change in the mood of the townspeople":
                    p "I thought you worked all of this out with them already?"
                    m "I did."
                    m "But now the clergymen of the town have started preaching that your festival will bring a literal hell on earth if this \"Satan's music\" will be played here."
                    p "Great... so what's going to happen now?"
                    p "All of a sudden we're supposed to shut down the whole thing?"
                    m "I'm afraid that's exactly what's going to happen now."
                    p "You can't be serious."
                    m "Sorry, my hands are tied."
                    menu:
                        "COMPLETE SENTENCE OR NOT? Question the town supervisor on his sudden lack of support for the festival":
                            p "How come you've changed your mind so quickly about this?"
                            p "Last night you were giving grand speeches about how the festival will energize the community and bring in a lot of cash for the town?"
                            m "I know, I know..."
                            m "I still think it would have been good for the community if your festival would have happened here."
                            p "Well then how come you're essentially letting them tell you what to do? I thought YOU were the town supervisor, not them!"
                            show chara mayor angry
                            m "Now look here, you can't talk to me like that!"
                            m "I'm very sorry, but there is really nothing I can do!"
                            m "Last night, the townsfolk hurriedly passed a legislation that all festivals need a special I-LV-JC permit to be able to use these fields for events!"
                            menu:
                                "Accept the situation and start packing up the festival":
                                    p "Fine, I guess that's it then."
                                    m "Thank you for understanding!"
                                    "You leave the office."
                                    jump townhall
                                "Ask about getting the \"I-LV-JC\" permit":
                                    p "Let me guess, we're not allowed to get one now?"
                                    show chara mayor neutral
                                    m "No, no... Of course you can apply for one!"
                                    p "Great, how do I do that then?"
                                    m "Just fill this form and you should get a reply within two months."
                                    p "\"Get a reply within two months\"?! The festival is starting TODAY!"
                                    m "Yes yes, I know all that..."
                                    menu:
                                        "Accept the situation and fill out the form":
                                            p "Fine, I'll fill out the form and wait for a reply."
                                            m "Good man! Here you go."
                                            "You fill out the form to apply for the special permit \"I-LV-JC\". After you're done, you head for the door."
                                            m "I'll make sure to let you know as soon as your request has been processed!"
                                            jump townhall
                                        "Tell the town supervisor you are \"SOL\"":
                                            p "So we're basically \"SOL\" then?"
                                            "Sol: - Noun, a former French copper or silver coin, usually worth 12 deniers."
                                            "Sol: - Noun, a poetic word for the sun."
                                            "Sol: - Acronym, colloquial, meaning \"Shit Outta Luck\"."
                                            show chara mayor angry
                                            m "Don't use that kind of language in my office!!"
                                            p "Right, sorry."
                                            p "I meant to say \"So we're basically slightly inconvenienced by this inopportune setback\"."
                                            show chara mayor neutral
                                            m "Sure, something like that..."
                                            jump townhall_first_dialogue_second_part
                                            


                        "Accept the situation and leave":
                            p "Right. Well there's clearly nothing I can do about this!"
                            m "I appreciate your understanding."
                            "You leave the office."
                            jump townhall
                                   
                "Tell the town supervisor that you'll cancel the festival":
                    p "Sure. We'll start packing and leave."
                    show chara mayor laughing with dissolve
                    "The supervisor is visibly pleased that his negotiation tactics have worked so effectively on you."
                    m "Ha! Good! I'll give you and your crew a couple of hours to pack up your things and leave town."
                    "You head for the door, feeling quite defeated."
                    jump townhall
        "Tell the town supervisor that you'll cancel the festival":
            p "Sure, that's alright. We'll start packing everything up."
            m "Good! I need your guys of here by 8 o'clock today."
            m "I really appreciate your understanding [player_name]."
            "The supervisor gives you one final look."
            "The conversation seems to be over. You head for the door."
            jump townhall


label townhall_first_dialogue_second_part:

    menu:
        "Tell the town supervisor that you'll fill out the form for the permit":
            p "Fine, I'll fill out the form and wait for a reply."
            m "Good man! Here you go."
            "You fill out the form to apply for the special permit \"I-LV-JC\". After you're done, you head for the door."
            m "I'll make sure to let you know as soon as your request has been processed!"
            jump townhall
        "Tell the town supervisor he is full of shit":
            p "This is some grade-A bullshit you're telling me here."
            show mayor angry
            m "I TOLD YOU TO NOT CUSS IN MY OFFICE!"
            m "Besides, I've got a re-election campaign to think about here!"
            p "A what campaign now?"
            show mayor neutral
            m "I-"
            m "Well..."
            p "Oh I see now... You don't want to upset the good folk of Bethel because you don't want to lose your precious little office!"
            m "\"Precious?\""
            m "My... precious?"
            "After a moment of staring in to distance, the town supervisor snaps back to reality."
            m "This town would be thrown to shit if I wasn't here!"
            m "You know who had this job before me?"
            m "Bubba Wilkinson, the local tomato farmer!"
            p "I didn't know tomatoes grew here."
            m "They don't!"
            m "Which is exactly why I need to have this office!"
            m "If I'm not here, some idiot that the townspeople randomly choose to elect because \"The Clergy\" told them to -"
            "You've never seen a grown man do the \"finger quotes\" move before."
            "The town supervisor sees you smirking at his gesture and stops himself from continuing with his rant."
            m "Why am I telling you this?! This is none of your business anyway!"
            "The town supervisor seems to calm down a bit."
            jump mayor_negotiation

# Negotiating with the mayor


label mayor_negotiation:
$ mayor_election_concern = True

p "Look, I respect your commitment to the town of Bethel. What if our festival would offer a nice gift to your re-election campaign? To possibly speed the application process as well?"
"The town supervisor thinks for a moment."
m "Hmm... a nice injection of funds to my campaign budget could really turn the tide..."
m "I think that sounds reasonable!"
m "What are you offering me?"

menu:
    "Offer a donation of money":
        p "I'll give a nice donation of money to your campaign."
        m "Sounds good!"
        m "If you can find me a briefcase full of money, I'll make sure you'll get your permit today."
        "It seems like this is the best deal you're going to get today."
        "You decide to go look for a briefcase full of money."
        p "Nice doing business with you."
        m "Likewise!"
        jump townhall
    "Offer whisky" if have_whisky == True:
        p "How about I give you this bottle of whisky?"
        $ mayor_happy = True
        $ day_one_end = "whisky"
        "The mayor is thrilled by this proposition."
        show chara mayor laughing
        m "Thank you, [player_name]! This is quite a gift indeed."
        m "Maybe we can just put this whole mess behind us?"
        m "After all, it's just one weekend."
        "You shake hands with the mayor."
        "Your troubles solved, you leave."
        jump townhall
    "Give the suitcase full of money" if have_chest == True:
        p "Would you be interested in this suitcase full of money by chance?" 
        $ mayor_happy = True
        $ day_one_end = "money"
        "You show your suitcase full of money to the mayor."
        show chara mayor surprised
        m "My golly gee! That sure is a hecking lot of money!"
        show chara mayor laughing
        m "Hey, how about we put this whole thing between us?"
        "The mayor reaches into a drawer and pulls out a slip of paper."
        m "I'll give you this fast-tracked permit for your event."
        m "How does that sound?"
        "You shake hands with the mayor."
        "Your troubles solved, you leave."
        jump townhall
    "Offer to give a gold bar to the town supervisor":
        p "I will find you a gold bar if you let us stay."
        show chara mayor laughing
        with dissolve
        "The mayor bursts in to laughter."
        m "A gold bar? You're going to find me a gold bar from this here field of mud and horse droppings?"
        m "All right, that sounds good to me! You find me a gold bar and I'll let you people stay and do your little festival! Ha ha ha!"
        "With tears in his eyes from laughter, the mayor walks you to the door and bids you farewell."
        m "A gold bar, ha ha ha! Why don't you find me a goose that lays golden eggs while your at it? Ha ha ha!!"
        $ mayor_wants_gold = True
        jump townhall
    "Offer to devote your life to the servitude of the local church" if negotiation_faith == False:
        p "I will join the local church and devote my life to serving the Almighty if you let us stay."
        m "What the hell are you trying to pull here, huh? You and your crew better git on out of here before I call the sheriff on your ass!"
        m "You think it's funny to make fun of other people's faith?!"
        m "This meeting is over!"
        "You decide it's best to leave."
        $ negotiation_faith = True
        jump townhall

# Townhall second dialogue


label townhall_second_dialogue:
    "You enter the office. The town supervisor seems surprised to see you again."
    m "Was there something you needed, [player_name]?"
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
