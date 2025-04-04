#
# BACKSTAGE
#

define t = Character("Larry the Technician", color="#9c341e")

# Has the player talked to the technician? (Determines if the technician explains the situation when first talking to him)
default technician_first_talk = True

# Has the player gotten a coin from Larry? (Determines if it's possible to get the batteries from the vending machine)
default have_larry_coin = False

# Has the player found 4 coins in the backstage area? (The player needs to pick up 4 coins before the battery runs out)
default have_coin = False
default have_coin2 = False
default have_coin3 = False
default have_old_coin = False

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

label backstage:


    scene bg backstage
    with fade
    if technician_first_talk==True:
        show technician frightened
        with dissolve
        t "[player_name]! You finally woke up!"
        t "We have a huge problem!"
        t "The mayor came by this morning and was yelling at everyone, looking for you."
        t "He's saying that he won't allow the festival to go on!"
        t "And even worse..."
        t "I'M OUT OF BEER!"
        hide technician
        with dissolve
    jump backstagemenu

label backstagemenu:
    scene bg backstage
    menu:
        "What should I do?"

        "Talk to Larry":
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
    show technician frightened
    with dissolve
    t "We need to solve our issue with the mayor."
    t "What are we going to do?!"
    menu:
        "I'll go talk to the mayor. I'm sure we'll figure something out." if mayor_happy==False:
            t "Alright, that sounds like a good plan. Good luck!"
            jump backstagemenu
        "Screw the mayor. We'll continue forward with the festival." if mayor_happy==False:
            "Larry looks shocked."
            t "Are you sure?! He said he's going to come in here with the sheriff and shut everything down by force if we don't leave by 8 o'clock!"
            menu:
                "Yes I'm sure. C'mon, let's get this show started! (End the day)":
                    jump ending
                "Hmm... maybe it's better to go talk to him first.":
                    t "Yes, I think that's a good idea! Good luck!"
                    "You leave Larry alone as he lights up a cigarette with shaking hands."
                    jump backstagemenu
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
                    jump backstagemenu

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
                    jump backstagemenu
                "This is just what I needed, thanks!":
                    t "No problemo, man!"
                    jump backstagemenu
        else:
            t "Hey [player_name]! Are you ready to start the festival?"
            menu:
                "Yep, let's get this show started! (End the day)":
                    jump ending
                "Not just yet. Let me check on a couple of things first. (Leave)":
                    jump backstagemenu
    menu:
        "Not yet. I'll go do that now." if mayor_first_talk==True:
            t "Alright, good luck!"
            jump backstagemenu
        "Screw the mayor. We'll continue forward with the festival." if mayor_happy==False:
            "The stage manager looks frightened."
            t "Are you sure?! He said he's going to come in here with the sheriff and shut everything down by force if we don't leave by 8 o'clock!"
            menu:
                "Yes I'm sure. C'mon, let's get this show started! (End the day)":
                    jump ending
                "Hmm... maybe it's better to go talk to him first.":
                    t "Yes, I think that's a good idea! Good luck!"
                    "You leave the stage manager as he lights up a cigarette with shaking hands."
                    jump backstagemenu
        "Hey Larry do you want this bar of gold?" if have_gold==True:
            t "Nah I'm good, man."
            t "Thanks anyway."
            jump backstagemenu
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
                        jump backstagemenu
                    "...are those not your pants?":
                        t "Whoa man!"
                        t "That's kind of a capitalist mentality if you ask me!"
                        t "I mean do we really ever \"own\" anything??"
                        menu:
                            "You're totally right. Nobody really \"owns\" anything. Especially when it comes to copyrighted music some students might want to use for their video game course project.":
                                t "Right on, man!"
                                jump backstagemenu
                            "I guess that means you don't need to get paid for this gig.":
                                "You decide there are more important matters than a lengthy discussion about the nature of ownership to focus on right now. You thank Larry for the coin and leave."
                                jump backstagemenu
            else:
                t "Nah, I have no more coins on me, man."
                t "I thought you were supposed to be good with money? How come you're totally broke?"
                menu:
                    "I'm not \"totally broke\"!":
                        t "I think you are if you're asking me for change..."
                        "You decide it's better to immediately end the conversation and leave."
                        jump backstagemenu
                    "I made some bad investments.":
                        t "Yeah man, it happens!"
                        t "My brother and I went to the casino last year..."
                        t "I don't really know how the whole thing works, but my brother told me that if the ball lands on the red square two times in a row, the next time it'll land on the black one for sure!"
                        t "So, we eventually lost our mom's house..."
                        "You decide it's better to not continue this conversation any longer."
                        jump backstagemenu
        "Yes, I talked to him. Don't worry, I'll get it sorted." if mayor_first_talk==False:
            t "O-okay! Let me know if anything changes!"
            jump backstagemenu
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
                    jump backstagemenu

# Backstage search


label backstage_items:
    
    
    if have_metal_detector==False:
        "You look around the discarded cardboard boxes and other pieces of garbage that permeate the backstage area."
        "There doesn't seem to be anything of interest here."
        jump backstagemenu
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
                            jump backstagemenu
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
            "Stop looking around":
                jump backstagemenu
