#
# TOILETS
#

label toilets:
    scene bg toilets
    with fade
    if day_one_end == "money":
        if talked_to_kid == False:
            $ talked_to_kid = True
            "You hear shouting and banging coming from one of the stalls."
            k "Help! Is anyone there?"
            p "Is that Maddox?"
            k "My name is Marty!"
            p "Right, Marty!"
            p "Listen, I'm here to get you out!"
            k "Oh thank God! It's really hot in here and I have the film camera with me in here!"
            k "This film will get destroyed if I don't get out of here quick!"
            p "And then I won't get paid!"
            k "Sorry, what was that? Say again?"
            p "Nothing!"
            p "I'm gonna get you out of there! I just need to figure out how to do that!"
            k "Okay, but you need to hurry!"
            jump actionsmenu
        else:
            jump actionsmenu
    else:
        jump toilets_d2b
    

label talktoilets:
    menu:
        "Talk to the kid in the toilet":
            p "Is there a problem?"
            k "What do you think?!"
            k "I'm stuck in here!"
            k "It's sweltering!"
            jump talktoilets
        "Can you unlock the door?":
            k "Do you think I haven't tried?!"
            jump talktoilets
        "Ask Mary Jane to start up the winch" if winch_hooked:
            "The kid is free."
            k "Thank you so much! Even my camera's fine!"
            $ day_two_end = "winch"
            jump day2_ending
        "Leave":
            k "Hey, don't leave me here!"
            jump actionsmenu

label looktoilets:
    if have_talked_mj == False:
        $ have_talked_mj = True
        "You look around for a bit and notice a girl looking back at you."
        "She's waiting in line to use a toilet."
        show chara girl neutral
        with dissolve
        mj "Hey, why are you shouting at someone inside a toilet?"
        mj "I'm sure another one will be free to use soon."
        menu:
            "Tell the girl to mind her own business":
                p "Mind your own business!"
                mj "Damn, you've gotta go that bad, huh?"
                mj "Alright, I'll leave you to it."
                mj "Have a nice festival!"
                "The girl leaves you alone."
                jump actionsmenu
            "Explain the situation":
                p "No, it's not that. There's someone stuck in one of the toilets."
                p "It's my responsibility to get them out."
                mj "Wow, that's really nice of you to help them out!"
                p "Yeah well, I'm the producer of this festival..."
                p "So if this kid doesn't get out soon, I'm pretty screwed."
                mj "You're the one putting this whole thing together?"
                p "Not really. I'm just someone that was hired to make sure everything runs smoothly."
                mj "That's cool."
                mj "Well, I hope you get that kid out soon! I'm sure being stuck in one of these toilets is no fun in this heat..."
                menu:
                    "Ask the girl who she is":
                        p "So what's your name?"
                        mj "My name's Mary Jane! Nice to meet you!"
                        p "Likewise. Are you here for the whole weekend?"
                        mj "Yeah, I actually live in this town!" 
                        mj "I spend the summers working on this farm actually."
                        mj "It's pretty exciting how all of these people from around the country have come here just for this..."
                        mj "I think it's good for the people in the town to see that there are a lot of us young people who think the same way."
                        menu:
                            "Ask Mary Jane what she means":
                                p "What do you mean \"think the same way\"?"
                                mj "I have some friends who have been sent off to Vietnam. This can't go on like this, you know."
                                mj "Why is it us young people who have to go fight some stupid war the U.S. shouldn't even be a part of?"
                                mj "Come to think of it, I guess this whole festival is a sort of wake-up call for a lot of people."
                                p "How so?"
                                mj "This festival is all over the news."
                                mj "All the old folks are saying that we just want to take drugs and do nothing with our lives..."
                                mj "But isn't this whole thing really about us young people making a statement?"
                                mj "Maybe we don't want the same things as our parents do?"
                                mj "Who knows if tomorrow we wake up and suddenly there are missiles flying all over the place?"
                                mj "What we really want is peace, and the freedom to choose what we want for ourselves."
                                mj "Isn't that why the festival was put together in the first place?"
                                mj "To show the world that we can get together for 3 days, without any violence or trouble?"
                                menu:
                                    "Tell Mary Jane you don't really care":
                                        p "Honestly, I haven't had the time to think about any of that."
                                        p "I'm here just to get paid."
                                        mj "Well aren't you the anti-hero!"
                                    "Tell Mary Jane she's right":
                                        p "Yeah, that was basically the idea from what I've heard."
                                        mj "Exactly!"
                                        mj "We're pretty lucky that we're here in this moment in time, and that we get to see all this."
                                        mj "And the music is just awesome!"
                                p "Yeah..."
                                p "I've got to get this kid out. Hope you have a nice festival."
                                mj "You too! Good luck!"
                                jump actionsmenu
                            "Say bye to the girl":
                                p "I've gotta go find a way to get this kid out."
                                p "Have a nice festival."
                                mj "Good luck!"
                                jump actionsmenu
                    "Say goodbye to the girl":
                        p "I'm going to go find a way to get this kid out."
                        p "I hope you have a nice festival."
                        mj "You too! And good luck!"
                        jump actionsmenu
    else:
        "The kid is still stuck in the toilet."
        if truck_fixed == True:
            "The truck is in the toilet area, ready to be used."
        "Also, the girl you talked to before is still hanging around the toilet area."
        menu:
            "Try to pull the door open":
                "The door doesn't budge."
                jump looktoilets
            "Use the winch on the truck to open the toilet" if winch_here == True:
                "You try to use the winch-system on the truck, but unfortunately you have no idea how to use it."
                "Feeling quite frustrated by your lack of skills with machinery, you leave the winch alone."
                jump actionsmenu
            "Use the axe to break the toilet door" if have_axe == True:
                "You break down the door. The kid is free."
                k "Thank you so much!"
                k "But my camera broke..."
                $ day_two_end = "axe"
                jump day2_ending
            "Talk to the girl":
                show chara girl neutral
                mj "Ah, it's you!"
                mj "How's it going?"
                menu:
                    "Ask the girl about using the winch" if winch_here == True:
                        p "You wouldn't know how to use a winch would you?"
                        mj "What's the problem?"
                        p "I have no idea how to use this thing."
                        mj "Well it's not very hard, is it? You just tie the cable around the thing you want pulled, and you turn the winch on."
                        p "Right..."
                        p "How come you know how to use this thing?"
                        mj "Like I said, it's not exactly rocket science."
                        mj "But I spend summers working for Max Yasgur's farm."
                        mj "Using a winch is pretty much the easiest thing when working on a farm."
                        p "I bet. Let's get this winch started then!"
                        mj "Sure thing!"
                        "You connect the winch and use it. Marty gets out and the camera is OK."
                        jump day2_ending
                    "Say bye to the girl":
                        p "Good. I need to get some stuff done."
                        mj "Right on! I'll see you around!"
                        jump actionsmenu
            "Don't talk to the girl":
                jump actionsmenu

label toilets_d2b:
    if farmer_found == False:
        "Talking with the hippy chick about the farmer."
        "She tells you that Bessie the cow can find the farmer from anywhere by smell."
        "You can call for Bessie in the field now."
        $ mj_farmer_talk = True
        jump actionsmenu
    else:
        "Bessie find the farmer."
        "The farmer can help you move the cows."
        "You go to the field and the cows leave."
        $ day_two_end = "happycows"
        jump day2_ending