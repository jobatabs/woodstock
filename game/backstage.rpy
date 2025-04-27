#
# BACKSTAGE
#

label backstage:


    scene bg backstage
    with fade
    if technician_first_talk==True:
        show chara technician frightened
        with dissolve
        t "[player_name]! You finally woke up!"
        t "Some party, huh?"
        t "Listen, we have a huge problem!"
        t "The town supervisor came by this morning and he was telling everyone that the festival is cancelled!"
        t "He was saying that we need some kind of a permit!"
        t "And there's another, even bigger problem as well!"
        t "I'M OUT OF BEER!"
        t "What are we going to do?!"
        $ playertip = "I should go talk to the town supervisor."
        jump talklarry
    else:
        "Backstage is full of activity, people running around, technicians unloading cases, and artists preparing for their shows."
    jump actionsmenu

label talkbackstage:
    jump backstage_dialogue_second

# Backstage first dialogue

label talklarry:
    menu:
        "Ask about the town supervisor" if mayor_happy==False:
            p "I thought all of this stuff with the town supervisor was already sorted?"
            t "That's what you told me as well last night!"
            t "But now they're shutting us down!"
            t "What are we going to do?!"
            jump talklarry
        "Tell Larry you'll talk to the town supervisor" if mayor_happy==False:
            p "Just keep working, I'll go talk to the town supervisor."
            t "Alright, that sounds good."
            t "I'll go check if the stage cables are still shooting sparks all over the wooden flooring."
            jump actionsmenu
        "Ignore the town supervisor and start the festival" if mayor_happy==False:
            p "Screw the town supervisor. We'll continue forward with the festival."
            "Larry looks shocked."
            t "Are you sure?! He said he's going to come in here with the sheriff and shut everything down by force if we don't leave by 8 o'clock!"
            menu:
                "Ignore Larry's concerns and start the festival (End the day)":
                    p "Yes I'm sure. C'mon, let's get this show started!"
                    t "Okay, if you say so..."
                    jump ending
                "Go talk to the town supervisor":
                    p "Hmm... maybe it's better to go talk to him first?"
                    t "Yes, I think that's a good idea! Good luck!"
                    "You leave Larry alone as he lights up a cigarette with shaking hands."
                    jump actionsmenu
        "Tell Larry you've solved the problem with the permits" if mayor_happy==True:
            p "The town supervisor won't be a problem for us anymore."
            $ technician_happy = True
            show chara technician happy  
            with dissolve
            t "Wow, you sorted it out already? That's great news!"
            t "So, do you want to start the festival then?"
            menu:
                "Start the festival (End the day)":
                    p "Yeah, let's get this show started! (End the day)"
                    t "Alright! Rock'n'roll, man!"
                    jump ending
                "Don't start the festival yet":
                    p "Nah, let me actually make sure everything is in order before we start."
                    t "Okay, sounds good. Let me know when you're ready to start the festival!"
                    jump actionsmenu

# Backstage second dialogue


label backstage_dialogue_second:


    if technician_happy==False:
        show chara technician frightened
        with dissolve
        t "[player_name]! Did you go talk to the town supervisor yet?"
    elif technician_happy==True:
        show chara technician happy 
        with dissolve
        if have_paper==False:
            t "Hey [player_name]! Thanks for taking care of that business with the town supervisor!"
            t "I have a gift for you as a thank you!"
            "Larry hands you a folded piece of paper."
            "You unfold the paper and see that \"1969\" is written on it."
            $ have_paper = True
            menu:
                "Why are you giving me a piece of paper that has the current year written on it?":
                    t "Time is relative, man! This will help you remember what year it is in case you forget!"
                    t "Alright, I have to go check that the ungrounded stage cables aren't submerged in puddles again."
                    t "Later, man!"
                    jump actionsmenu
                "This is just what I needed, thanks!":
                    t "No problemo, man!"
                    jump actionsmenu
        else:
            t "Hey [player_name]! Are you ready to start the festival?"
            menu:
                "Yep, let's get this show started! (End the day)":
                    jump ending
                "Not just yet. Let me check on a couple of things first. (Leave)":
                    jump actionsmenu
    menu:
        "Not yet. I'll go do that now." if mayor_first_talk==True:
            t "Alright, good luck!"
            jump actionsmenu
        "Screw the town supervisor. We'll continue forward with the festival." if mayor_happy==False:
            "Larry looks frightened."
            t "Are you sure?! He said he's going to come in here with the sheriff and shut everything down by force if we don't leave by 8 o'clock!"
            menu:
                "Yes I'm sure. C'mon, let's get this show started! (End the day)":
                    jump ending
                "Hmm... maybe it's better to go talk to him first.":
                    t "Yes, I think that's a good idea! Good luck!"
                    "You leave the stage manager as he lights up a cigarette with shaking hands."
                    jump actionsmenu
        "Hey Larry do you want this bottle of whisky" if have_whisky==True:
            show chara technician angry
            with dissolve
            "Larry gets visibly angry."
            t "I said beer goddamnit!"
            show chara technician happy
            with dissolve
            "Although you have never seen Larry this angry, he calms down just as quick."
            t "Sorry."
            jump actionsmenu
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
                        jump actionsmenu
                    "...are those not your pants?":
                        t "Whoa man!"
                        t "That's kind of a capitalist mentality if you ask me!"
                        t "I mean do we really ever \"own\" anything??"
                        menu:
                            "You're totally right. Nobody really \"owns\" anything. Especially when it comes to copyrighted music some students might want to use for their video game course project.":
                                t "Right on, man!"
                                jump actionsmenu
                            "I guess that means you don't need to get paid for this gig.":
                                "You decide there are more important matters than a lengthy discussion about the nature of ownership to focus on right now. You thank Larry for the coin and leave."
                                jump actionsmenu
            else:
                t "Nah, I have no more coins on me, man."
                t "I thought you were supposed to be good with money? How come you're totally broke?"
                menu:
                    "I'm not \"totally broke\"!":
                        t "I think you are if you're asking me for change..."
                        "You decide it's better to immediately end the conversation and leave."
                        jump actionsmenu
                    "I made some bad investments.":
                        t "Yeah man, it happens!"
                        t "My brother and I went to the casino last year..."
                        t "I don't really know how the whole thing works, but my brother told me that if the ball lands on the red square two times in a row, the next time it'll land on the black one for sure!"
                        t "So, we eventually lost our mom's house..."
                        "You decide it's better to not continue this conversation any longer."
                        jump actionsmenu
        "Yes, I talked to him, but he won't budge." if mayor_first_talk==False:
            t "Hmm. I hear he loves whisky. Maybe you could give some to him?"
            $ playertip = "I could give whisky to the town supervisor."
            jump actionsmenu
        "The mayor's worried about his re-election." if mayor_election_concern==True:
            t "I know! We could give him some campaign money from our emergency funds!"
            "What emergency funds?"
            t "Don't you remember? The suitcase full of emergency money?"
            "Oh! Where is it?"
            t "We buried it! Like you told us, remember?"
            "Well, where did you bury it?"
            t "No idea, dude."
            t "But maybe you could just give some whisky to the town supervisor? I hear he loves whisky."
            $ playertip = "Emergency money, huh..."
        "The mayor won't be a problem for us anymore." if mayor_happy==True:
            $ technician_happy = True
            show chara technician happy  
            with dissolve
            t "Really? That's great news!"
            t "So, do you want to start the festival then?"
            menu:
                "Yeah, let's get this show started! (End the day)":
                    jump ending
                "Nah, let me actually make sure everything is in order before we start.":
                    t "Okay, sounds good. Let me know when you're ready to start the festival!"  
                    jump actionsmenu

# Backstage search


label lookbackstage:
    
    
    if have_metal_detector==False:
        "You look around the discarded cardboard boxes and other pieces of garbage that permeate the backstage area."
        "There doesn't seem to be anything of interest here."
        jump actionsmenu
    else:
        menu:
            "Use your metal detector":
                if egg_counter >= 11:
                    "You have walked through the whole backstage area with your metal detector. There doesn't seem to be anything more to find."
                    jump lookbackstage
                elif have_old_coin==True:
                    if have_batteries==False:
                        "Your metal detector seems to have run out of batteries."
                        jump lookbackstage
                    elif have_batteries==True:
                        if have_chest==False:
                            "You change the batteries of your metal detector for new ones. Suddenly the machine seems to beep with newfound vigour."
                            "Something heavy hides beneath the mud of the backstage area."
                            "You plunge your hands in to the mud, using your fingers to find the edges of the object." 
                            "Finally your hands find something that you can grab on to firmly."
                            "You pull with all your strength, and you manage to get the object out of the mud."
                            "It is your suitcase of emergency funds!"
                            $ have_chest =  True
                            jump actionsmenu
                        if have_gold==False:
                            "You dig around and find a bar of gold!"
                            $ have_gold = True
                            $ egg_counter += 1
                            jump lookbackstage
                        elif egg_counter==10:
                            "You dig around and find an easter egg!"
                            "Doesn't seem like you can do anything with it though..."
                            $ egg_counter += 1
                            jump lookbackstage
                        elif egg_counter>0:
                            "You dig around but find nothing."
                            $ egg_counter += 1
                            jump lookbackstage   
                else:
                    "You walk around the backstage area until your metal detector beeps."
                    if have_coin==False:
                        "You dig around and find a small coin!"
                        "This one is worth 25 cents."
                        $ cents += 25
                        $ have_coin = True
                        jump lookbackstage
                    elif have_coin2==False:
                        "You dig around and find a small coin!"
                        "This one is worth five cents."
                        $ cents += 5
                        $ have_coin2 = True
                        jump lookbackstage
                    elif have_coin3==False:
                        "You dig around and find a small coin!"
                        "This one is worth ten cents."
                        $ cents += 10
                        $ have_coin3 = True
                        jump lookbackstage
                    elif have_old_coin==False:
                        "You dig around and find a small coin!"
                        "This one seems to be late Anglo-Saxon, from the first half of the eleventh century."
                        "It is quite obvious that it is from the reign of Cnut the Great (c. 990 - 1035) instead of Aethelred I of Wessex (c. 845 - 871), since it has been minted in Cambridge around the year 1000 AD."
                        "Of course, another obvious sign that it is from the reign of Cnut is that the obverse of the coin depicts a \"pointed helmet\" style of portrait, a trademark of Cnut's."
                        "But since you aren't particulary interested in old coins, you throw it away."
                        $ have_old_coin = True
                        jump lookbackstage   
            "Back":
                jump actionsmenu
