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
    p "I'm good. What's this I hear about a problem with some permit?"
    m "Right..."
    m "Well, I'm afraid the situation has changed a bit with the townsfolk."

    menu:
        "Give the briefcase full of money" if have_chest == True:
            p "Here's a briefcase full of money for you."
            $ have_chest = False
            $ mayor_happy = True
            $ day_one_end = "money"
            m "Oh wow!"
            m "I see you are speedrunning through the game!"
            m "That's alright with me! The problem with the permit is all sorted now!"
            "You leave the office."
            $ playertip = "The problem with the permit has been sorted. Time to start the festival."
            jump townhall
        "Ask for more information":
            p "Okay? How so?"
            m "Well, the people of Bethel have decided that our community does not want a big hippie festival to happen here."
            menu:
                "Ask why the townsfolk have suddenly changed their mind":
                    p "I thought you worked all of this out with them already?"
                    m "I did."
                    m "But now the clergymen of the town have started preaching that your festival will bring a literal hell on earth if this \"Satan's music\" will be played here."
                    p "Great... so what's going to happen now?"
                    p "All of a sudden we're supposed to shut down the whole thing?"
                    m "I'm afraid that's exactly what's going to happen now."
                    p "You can't be serious."
                    m "Sorry, my hands are tied."
                    menu:
                        "Question the town supervisor about his lack of support":
                            p "How come you've changed your mind so quickly about this?"
                            p "Last night you were giving grand speeches about how the festival will energize the community and bring in a lot of cash for the town?"
                            m "I know, I know..."
                            m "I still think it would have been good for the community if your festival would have happened here."
                            p "Well then how come you're essentially letting them tell you what to do? I thought YOU were the town supervisor, not them!"
                            show chara mayor angry
                            m "Now look here, you can't talk to me like that!"
                            m "I'm very sorry, but there is really nothing I can do!"
                            m "Last night, the townsfolk hurriedly passed a legislation that all festivals need a special I-LV-JC permit to be able to use these fields for any events!"
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
            $ mayor_election_concern = True
            p "Oh I see now... You don't want to upset the good folk of Bethel because you don't want to lose your precious little office!"
            m "This town would be thrown to shit if I wasn't here!"
            m "You know who had this job before me?"
            m "Bubba Wilkinson, the local tomato farmer!"
            p "I didn't know tomatoes grew here."
            m "They don't!"
            m "Which is exactly why I need to have this office!"
            m "If I'm not here, some idiot that the townspeople randomly choose to elect because \"The Clergy\" told them to -"
            "You've never seen a grown man do \"finger quotes\" before."
            "The town supervisor sees you smirking and stops himself from continuing with his rant."
            m "Why am I telling you this?! This is none of your business anyway!"
            "The town supervisor seems to calm down a bit."
            menu:
                "Tell the town supervisor he's a spineless politician":
                    p "You really are a spineless politician who only cares about his self-interests."
                    "It does not take long for the town supervisor to leap over his desk and perform some kind of a judo move on you, throwing you out of his office."
                    jump townhall
                "Offer to help with the re-election campaign":
                    jump mayor_negotiation

# Negotiating with the mayor


label mayor_negotiation:

p "Look, I respect your commitment to the town of Bethel. What if our festival would offer a nice gift to your re-election campaign? To possibly speed the application process as well?"
"The town supervisor thinks for a moment."
m "Hmm... a nice injection of funds to my campaign budget could really turn the tide..."
m "I think that sounds reasonable!"
m "What are you offering me?"

menu:
    "Offer a donation of money":
        $ mayor_wants_chest = True
        p "I'll give a nice donation of money to your campaign."
        m "Well, that's a very nice offer!"
        $ playertip = "I need to find a briefcase full of money for the town supervisor."
        m "But I'm afraid the amount would need to be quite substantial."
        m "After all, I would be directly going against the will of the townsfolk in this business with the permit."
        m "If you can find me a briefcase full of money, I'll make sure you'll get your permit today."
        menu:
            "Tell the town supervisor that you don't have that kind of money":
                p "I don't really have a briefcase full of money just laying around..."
                p "Could a little less be OK?"
                m "Sorry, but I'm putting my neck on the line here."
                m "It's going to be a briefcase full of money, or nothing."
                "It seems like this is the best deal you're going to get today."
                "You decide to go look for a briefcase full of money."
                p "Nice doing business with you."
                m "Likewise!"
                jump townhall
            "Tell the town supervisor that he'll get his money soon":
                p "Alrighty then, one briefcase full of money, coming right up."
                m "Excellent! I'll see you soon!"
                "You leave the office and go look for a briefcase full of money."
                jump townhall
    "Offer the town supervisor a gift of whisky" if have_whisky == True:
        p "How about I give you this bottle of whisky?"
        $ have_whisky = False
        $ mayor_happy = True
        $ day_one_end = "whisky"
        "The town supervisor is thrilled by this proposition."
        show chara mayor laughing
        m "Oh wow!"
        m "Thank you, [player_name]! This is a pretty fancy bottle I must say!"
        "The town supervisor seems enchanted by the bottle of whisky."
        m "Well then! Let's just put this whole mess behind us, shall we?"
        m "I'll give you a fast-tracked permit! You'll have no more trouble from the townsfolk!"
        "The mayor reaches into his desk drawer and pulls out a small slip of paper."
        m "Here you go! One fast-tracked permit!"
        m "Pleasure doing business with you! And good luck to your beautiful festival!"
        "You and the town supervisor shake hands, and you head for the door."
        "As you reach for the door handle, you hear the town supervisor mutter to himself behind you."
        m "Ahh yes, that's the good stuff... I'm going to enjoy this!"
        "You leave the town supervisor alone with his bottle."
        $ playertip = "The problem with the permit has been sorted. Time to start the festival."
        jump townhall
    "Give the briefcase full of money" if have_chest == True:
        if mayor_election_concern == False:
            p "Would you be interested in this briefcase full of money by chance?" 
            $ mayor_happy = True
            $ day_one_end = "money"
            "You show your briefcase full of money to the town supervisor."
            show chara mayor surprised
            m "Oh wow! You're offering this to me?"
            p "Yep, it's yours. The only thing I need from you is that our problem with the permit is solved immediately."
            show chara mayor laughing
            m "Ha ha! Of course, of course! I'll give you a fast-tracked permit right away!"
            "The town supervisor reaches into his desk drawer and pulls out a small slip of paper."
            m "Here you go! One fast-tracked permit!"
            "The town supervisor hands you a fast-tracked permit. It looks like the trouble with the permit is all sorted now."
            m "Pleasure doing business with you! And good luck to your beautiful festival!"
            "You and the town supervisor shake hands, and you head for the door."
            $ playertip = "The problem with the permit has been sorted. Time to start the festival."
            jump townhall
        elif mayor_election_concern == True:
            p "Here's your briefcase full of money."
            "You give the briefcase full of money to the town supervisor."
            $ have_chest = False
            $ mayor_happy = True
            $ day_one_end = "money"
            m "Oh wow! You actually managed to pull it off!"
            m "I must say, I was a bit sceptical at first at your proposition!"
            p "So the problem with the permit is all sorted now, yeah?"
            m "Yes, yes of course! Here, I'll give you a fast-tracked permit right away!"
            "The town supervisor reaches into his desk drawer and pulls out a small slip of paper."
            m "Here you go! One fast-tracked permit!"
            "The town supervisor hands you a fast-tracked permit. It looks like the trouble with the permit is all sorted now."
            m "Pleasure doing business with you! And good luck to your beautiful festival!"
            "You and the town supervisor shake hands, and you head for the door."
            $ playertip = "The problem with the permit has been sorted. Time to start the festival."
            jump townhall
    "Offer to give a gold bar to the town supervisor" if mayor_wants_gold == False:
        p "I will find you a gold bar if you let us stay."
        show chara mayor laughing
        with dissolve
        "The town supervisor bursts in to laughter."
        m "A gold bar? You're going to find me a gold bar from this here field of mud and horse droppings?"
        m "All right, that sounds good to me! You find me a gold bar and I'll let you people stay and do your little festival! Ha ha ha!"
        "With tears in his eyes from laughter, the mayor walks you to the door and bids you farewell."
        m "A gold bar, ha ha ha! Why don't you find me a goose that lays golden eggs while your at it? Ha ha ha!!"
        "You leave the town supervisor's office to go look for gold."
        $ playertip = "I need to go find a bar of gold for the town supervisor."
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
    if mayor_wants_chest == True:
        m "Ah, it's you!"
        m "Do you have the money?"
        menu:
            "Offer whisky to the town supervisor" if have_whisky == True:
                p "How about I give you this bottle of whisky?"
                $ have_whisky = False
                $ mayor_happy = True
                $ day_one_end = "whisky"
                "The town supervisor is thrilled by this proposition."
                show chara mayor laughing
                m "Oh wow!"
                m "Thank you, [player_name]! This is a pretty fancy bottle I must say!"
                "The town supervisor seems enchanted by the bottle of whisky."
                m "Well then! Let's just put this whole mess behind us, shall we?"
                m "I'll give you a fast-tracked permit! You'll have no more trouble from the townsfolk!"
                "The mayor reaches into his desk drawer and pulls out a small slip of paper."
                m "Here you go! One fast-tracked permit!"
                m "Pleasure doing business with you! And good luck to your beautiful festival!"
                "You and the town supervisor shake hands, and you head for the door."
                "As you reach for the door handle, you hear the town supervisor mutter to himself behind you."
                m "Ahh yes, that's the good stuff... I'm going to enjoy this!"
                "You leave the town supervisor alone with his bottle."
                $ playertip = "The problem with the permit has been sorted. Time to tell Larry to start the festival."
                jump townhall
            "Give the town supervisor the briefcase full of money" if have_chest == True:
                if mayor_wants_chest == True:
                    p "Here's your briefcase full of money."
                    "You give the briefcase full of money to the town supervisor."
                    $ have_chest = False
                    $ mayor_happy = True
                    $ day_one_end = "money"
                    m "Oh wow! You actually managed to pull it off!"
                    m "I must say, I was a bit sceptical at first at your proposition!"
                elif mayor_wants_chest == False:
                    p "Here's a briefcase full of money, just for you!"
                    m "Oh, wow! All of this is for me??"
                    p "Yep, it's all yours. But only if you make our little problem go away..."
                    m "Sure, sure! Anything you say!"
                p "So the problem with the permit is all sorted now, yeah?"
                m "Yes, yes of course! Here, I'll give you a fast-tracked permit right away!"
                "The town supervisor reaches into his desk drawer and pulls out a small slip of paper."
                m "Here you go! One fast-tracked permit!"
                "The town supervisor hands you a fast-tracked permit. It looks like the trouble with the permit is all sorted now."
                m "Pleasure doing business with you! And good luck to your beautiful festival!"
                "You and the town supervisor shake hands, and you head for the door."
                $ playertip = "The problem with the permit has been sorted. Time to tell Larry to start the festival."
                jump townhall
            "Say you need more time to get the money":
                p "I don't have the money yet. I need a little more time."
                m "No problem, I'll be here."
                "You leave the office."
                jump townhall

    "You enter the office. The town supervisor seems surprised to see you again."
    m "Oh, it's you again. What can I do for you, [player_name]?"
    menu:
        "Offer to help with the re-election campaign" if mayor_election_concern == True:
            jump mayor_negotiation
        "Try to make a deal with the town supervisor" if mayor_election_concern == False:
            p "I think you and me should make some sort of a deal."
            m "What do you mean?"
            p "I think it's too late for us to start packing up the festival. The whole thing is supposed to kick off today."
            m "*sigh*"
            m "We've already talked about this. There's nothing I can do."
            p "Surely there's something I could offer you? So that the festival could continue?"
            m "You don't give up, do you?"
            m "I'm very sorry, but my hands are tied."
            m "Have a good day."
            menu:
                "Keep pushing for a deal":
                    p "I really think we should make some sort of a deal here!"
                    m "And *I* think the best thing for everyone would be that you pack up and leave town."
                    m "This meeting is over. Good day to you."
                    "It seems you have failed to negotiate with the town supervisor."
                    "You are escorted out of the office."
                    jump townhall
                "Tell the town supervisor he is full of shit":
                    p "This is some grade-A bullshit you're telling me here."
                    show mayor angry
                    m "YOU WILL NOT CURSE IN MY OFFICE!"
                    m "Who the hell do you think you are, using that kind of language?"
                    m "You just waltz in and think you can do or say anything you want!"
                    m "Why don't you leave me alone?!"
                    m "I've got a re-election campaign to think about here!"
                    p "A what campaign now?"
                    show mayor neutral
                    m "I-"
                    m "Well..."
                    $ mayor_election_concern = True
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
                    "You've never seen a grown man do \"finger quotes\" before."
                    "The town supervisor sees you smirking at his gesture and stops himself from continuing with his rant."
                    m "Why am I telling you this?! This is none of your business anyway!"
                    "The town supervisor seems to calm down a bit."
                    menu:
                        "Tell the town supervisor he's a spineless politician":
                            p "You really are a spineless politician who only cares about his self-interests."
                            "It does not take long for the town supervisor to leap over his desk and perform some kind of a judo move on you, throwing you out of his office."
                            jump townhall
                        "Offer to help with the re-election campaign":
                            jump mayor_negotiation

        "Leave the office":
            p "Actually, never mind."
            m "I see..."
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
