#
# BACKSTAGE
#

label backstage:
    if day == 2:
        if day_one_end == "money":
            jump backstage_d2a
        elif day_one_end == "whisky":
            jump backstage_d2b
        else:
            "Something has gone wrong."
            jump map_screen

    scene bg backstage
    with fade
    if technician_first_talk==True:
        "The backstage area is full of activity. People are running around, technicians are unloading cases, and artists are preparing for their shows."
        "An interesting looking man notices you and hurriedly makes his way towards you."
        show chara technician frightened
        with dissolve
        $ technician_first_talk = False
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
            jump backstage
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
                    jump backstage
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
                    jump backstage

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
                    jump backstage
                "This is just what I needed, thanks!":
                    t "No problemo, man!"
                    jump talklarry
        else:
            t "Hey [player_name]! Are you ready to start the festival?"
            menu:
                "Start the festival (End the day)":
                    p "Yeah, let's get this show started! (End the day)"
                    t "Alright! Rock'n'roll, man!"
                    jump ending
                "Don't start the festival yet":
                    p "Nah, let me actually make sure everything is in order before we start."
                    t "Okay, sounds good. Let me know when you're ready to start the festival!"
                    jump backstage
    menu:
        "Tell Larry you'll go talk to the town supervisor" if mayor_first_talk==True:
            p "Not yet. I'll go do that now."
            t "Alright, good luck!"
            jump backstage
        "Ignore the town supervisor and start the festival" if mayor_happy==False:
            p "Screw the town supervisor. We'll continue forward with the festival."
            "Larry looks shocked."
            t "Are you sure?! He said he's going to come in here with the sheriff and shut everything down by force if we don't leave by 8 o'clock!"
            menu:
                "Ignore Larry's concerns and start the festival (End the day)":
                    p "Yes I'm sure. C'mon, let's get this show started!"
                    t "Okay, if you say so..."
                    jump ending
                "Hmm... maybe it's better to go talk to him first.":
                    t "Yes, I think that's a good idea! Good luck!"
                    "You leave the stage manager as he lights up a cigarette with shaking hands."
                    jump backstage
        "Offer Larry the bottle of whisky" if have_whisky==True:
            p "Hey Larry, you want this bottle of whisky?"
            show chara technician angry
            with dissolve
            t "I SAID I'M OUT OF *BEER* GODDAMNIT!!"
            "You have never seen Larry this angry before."
            show chara technician happy
            with dissolve
            "But just as quick, he returns to his usual relaxed self."
            t "Whisky's not really my thing, man!"
            jump actionsmenu
        "Ask Larry for some change" if have_seen_vending_machine==True:
            p "Hey Larry, do you happen to have some extra change on you?"
            if have_larry_coin==False:
                t "Uh... I don't really believe in money, man..."
                t "But here, I found this in the pocket of these sweet pants!"
                "Larry hands you a coin worth five cents."
                $ have_larry_coin = True
                $ cents += 5
                menu:
                    "Thank Larry for the coin":
                        p "Thanks!"
                        t "No problem, man!"
                        jump actionsmenu
                    "Ask Larry about his pants":
                        p "Are those not your pants?"
                        t "Whoa man!"
                        t "That's kind of a capitalist mentality if you ask me!"
                        t "I mean do we really ever \"own\" anything??"
                        p "You're totally right. Nobody really \"owns\" anything. Especially when it comes to copyrighted music some students might want to use for their video game course project."
                        t "Right on, man! That's what I'm talking about!"
                        "You decide to leave Larry alone."
                        jump backstage
            else:
                t "Nah, I have no more coins on me, man."
                t "I thought you were supposed to be good with money? How come you're totally broke?"
                menu:
                    "Explain to Larry that you are not \"totally broke\"":
                        p "I'm not \"totally broke\"!"
                        t "I think you are if you're asking me for change..."
                        "You decide it's better to immediately end the conversation and leave."
                        jump backstage
                    "Explain to Larry that you've essentially thrown all your money away":
                        p "I made some bad investments."
                        t "Yeah man, it happens!"
                        t "My brother and I went to the casino last year..."
                        t "I don't really know how the whole thing works, but my brother told me that if the ball lands on the red square two times in a row, the next time it'll land on the black one for sure!"
                        t "So, we eventually lost our mom's house..."
                        "You decide it's better to not continue this conversation any longer."
                        jump actionsmenu
        "Ask Larry for help with the town supervisor" if mayor_first_talk==False:
            p "Yes, I talked to him, but he won't budge."
            p "I don't know what to do, honestly."
            t "Hmm. I hear he loves whisky. Maybe you could give some to him?"
            p "Whisky?"
            t "Yeah, the guy apparently loves whisky like nothing else."
            p "OK, that sounds like a good idea! I'll go find him some whisky."
            "You leave Larry to go find some whisky."
            $ playertip = "I should find some whisky for the town supervisor."
            jump backstage
        "Tell Larry that the town supervisor wants to get re-elected" if mayor_election_concern==True:
            p "The mayor's worried about his re-election campaign."
            p "I think I could maybe use that as some sort of leverage."
            t "That's a good idea! Have you tried to offer him a bribe?"
            menu:
                "Tell Larry about the bar of gold" if mayor_wants_gold == True:
                    p "Yeah, I offered to find him a bar of gold."
                    t "A bar of gold? Where do you think you're going to find a bar of gold around here?"
                    t "No offence, but that's a pretty far-out idea, even for me!"
                    p "Yeah I guess you're right..."
                    p "I better go offer him something else."
                    t "That's a pretty good idea."
                    t "You could always try to offer him some whisky?"
                    t "The guy apparently loves whisky like nothing else."
                    p "Whisky... OK, that's not a bad idea!"
                    p "Thanks for the tip!"
                    t "No worries man, we're all in this together! It's one love!"
                    "You leave Larry to go find some whisky."
                    $ playertip = "I should either offer the town supervisor something else, or find some whisky for him."
                    jump backstage
                "Tell Larry about the briefcase full of money" if mayor_wants_chest == True:
                    p "Yeah, I offered to find him a briefcase full of money."
                    t "A briefcase full of money? Where do you think you're going to find another briefcase full of money around here?"
                    p "Honestly, no idea. I'm not really sure what to do."
                    t "That's a bummer, man. So the whole festival will be shut down now?"
                    p "It's certainly starting to look that way. Damn, there must be another way..."
                    "You and Larry stand around for a bit, both deep in thought."
                    t "This is one tough nut to crack!"
                    t "It's a shame we can't use the festival emergency fund..."
                    p "\"The festival emergency fund\"? What's the festival emergency fund?"
                    t "You know, the briefcase full of cash we have in case of an emergency?"
                    p "Larry, for the love of God -"
                    p "THIS IS AN EMERGENCY!!"
                    p "Where is this briefcase full of money, then?!"
                    t "It's buried somewhere underground."
                    "You start to feel as if someone is playing a mean prank on you."
                    t "I thought you'd know all this stuff, since you were the one who told us to bury it!"
                    P "Why can't I remember any of this?!"
                    t "You were hitting the sauce pretty hard last night man, same as everyone else."
                    "You try to remember anything about a briefcase getting buried last night..."
                    "But no clear memory appears in your mind."
                    p "So the thinking clearly was that the money would be safe if buried underground. Problem is, we don't seem to have any memory of where we buried it."
                    p "I need to find some way to find where this briefcase is buried. Any ideas?"
                    t "Me and my brother used to have a water-dowsing stick. But I'm not sure if that's any help in this case?"
                    p "No Larry, I'm pretty sure a water-dowsing stick would be of no use right now."
                    p "I'll just have to find some way to locate this briefcase buried underground."
                    $ playertip = "I need to find a way to locate the briefcase buried underground."
                    t "Okay, good luck man!"
                    "You leave to find a way to locate the briefcase buried underground."
                    jump backstage
                "Tell Larry you're not sure what to offer to the town supervisor":
                    p "I'm not sure what to offer him."
                    t "Hmm. I hear he loves whisky. Maybe you could give some to him?"
                    p "Whisky?"
                    t "Yeah, the guy apparently loves whisky like nothing else."
                    p "OK, that sounds like a good idea! I'll go find him some whisky."
                    "You leave Larry to go find some whisky."
                    $ playertip = "I should find some whisky for the town supervisor."
                    jump backstage

        "Tell Larry that the problem with the permit has been sorted." if mayor_happy==True:
            p "The mayor won't be a problem for us anymore." 
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
                            "You find a briefcase full of money!"
                            $ have_chest =  True
                            jump actionsmenu
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
                        "This one is worth 10 cents."
                        $ cents += 10
                        $ have_coin = True
                        jump lookbackstage
                    elif have_coin2==False:
                        "You dig around and find a small coin!"
                        "This one is worth five cents."
                        $ cents += 5
                        $ have_coin2 = True
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

label backstage_d2a:
    "This is backstage area day 2 if the town supervisor got paid on the first day. Not much more here yet."
    jump map_screen

label backstage_d2b:
    "This is backstage area day 2 if the town supervisor got whisky on the first day. Not much more here yet."
    jump map_screen