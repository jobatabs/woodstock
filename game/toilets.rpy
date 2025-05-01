#
# TOILETS
#

label toilets:
    scene bg toilets
    with fade
    play music "crowd2.mp3" fadein 2.0 fadeout 2.0
    if day_one_end == "money":
        if talked_to_kid == False:
            $ talked_to_kid = True
            "You hear shouting and banging coming from one of the stalls."
            k "Help! Is anyone there?"
            p "Is that Maddox?"
            k "My name is Marty!"
            p "Right!"
            p "Listen, I'm here to get you out!"
            k "Oh thank God! It's really hot in here and I have the film camera with me in here!"
            k "This film will get destroyed if I don't get out of here quick!"
            p "And then I won't get paid!"
            k "Sorry, what was that?"
            p "Nothing!"
            p "I'm gonna get you out of there! I just need to figure out how to do that!"
            k "Okay, but you need to hurry!"
            jump actionsmenu
        else:
            jump actionsmenu
    else:
        jump toilets_d2b
    

label talktoilets:
    k "Get me out of here!"
    k "I think I'm going to pass out from the smell pretty soon!"
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
                mj "or maybe someone is stuck in a toilet, huh?"
                mj "Well, I'll leave you to it."
                mj "Have a nice festival!"
                "The girl walks away."
                jump toilets
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
                        $ girl_name = "Mary Jane"
                        $ mj = Character("Mary Jane", color="#6eff75")
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
                                jump toilets
                            "Say bye to Mary Jane":
                                p "I've gotta go find a way to get this kid out."
                                p "Have a nice festival."
                                mj "Good luck!"
                                jump toilets
                    "Say goodbye to the girl":
                        p "I'm going to go find a way to get this kid out."
                        p "I hope you have a nice festival."
                        mj "You too! And good luck!"
                        jump toilets
    else:
        "The kid is still stuck in the toilet."
        if truck_fixed == True:
            "The truck is in the toilet area, ready to be used."
        "Also, the girl you talked to before is still hanging around the toilet area."
        menu:
            "Try to pull the toilet door open":
                "The door doesn't budge."
                k "You need to find something to open the door with!"
                jump looktoilets
            "Use the winch on the truck to open the toilet" if winch_here == True:
                "You try to use the winch-system on the truck, but unfortunately you have no idea how to use it."
                "Feeling quite frustrated by your lack of skills with machinery, you leave the winch alone."
                jump looktoilets
            "Use the axe to break the toilet door" if have_axe == True:
                p "I've found a solution to get you out of there!"
                k "Great! What is it?"
                p "I'm going to smash a hole in to the door with this fire axe I have here!"
                k "Huh?!"
                k "Are you crazy?!"
                k "What if the axe goes through the door and hits me?!"
                "The kid might have a point there."
                menu:
                    "Break down the door with the axe":
                        p "You want to get out of there? This is the solution!"
                        p "Now stand back!"
                        "You start hammering on the door with the fire axe."
                        "After a couple of hits, the axe starts to bite in to the tough plastic of the toilet door."
                        k "Be careful! You're using quite a lot of force!"
                        p "Shut up and let me do my job!"
                        "You start using even more force to hit the door with."
                        "Eventually a small crack starts forming on the door."
                        "You decide to push on with even more force."
                        k "Aaagh! I think you're going to punch through the door and hit me!"
                        "The crack on the door has gotten bigger now."
                        "You decide to use all your might for a final push."
                        "Your fire axe flies towards the door, and a great big \"CRACK!\" is heard."
                        "The fire axe has gone completely through the door, and is now stuck in something."
                        p "Oh shit..."
                        p "Hey kid! Are you okay?"
                        k "Yes, I'm alive if that's what you're asking!"
                        k "But the situation is not great I must say!"
                        "You grab the edges of the crack you have made on the door, and rip away the kevlar-like plastic lining."
                        "Inside the toilet, you see a young man who is holding a film camera."
                        "Your fire axe has lodged itself firmly in to the body of the camera."
                        show chara kid neutral
                        with dissolve
                        k "Holy moly! That was close!"
                        k "If I wouldn't have been holding my camera, that axe would have surely hit me straight in the chest!"
                        k "But oh how good it feels to breathe in some fresh air!"
                        "You get the kid out of the toilets and assess the damage."
                        p "Man... I'm stronger than I thought!"
                        p "But that camera is not doing okay..."
                        "The film camera seems to be beyond repair."
                        "It would take an Arthurian effort to remove the axe from the camera."
                        "The impact of the axe has also caused the film cartridge to open. Hundreds of feet of film are unfurled on the ground, exposed to the sun."
                        k "I think making any sort of documentary is out of the question now."
                        p "Damnit!!"
                        k "Hey, don't worry about it! You get me out in one piece!"
                        p "Yep..."
                        k "I'm going to go rest for a bit. What a day..."
                        hide chara kid neutral
                        with dissolve
                        "You see the kid walk away in a daze."
                        "In the distance, you can see Larry walking towards you, waving."
                        show chara technician happy
                        with dissolve
                        t "Hey [player_name]! You managed to get the kid out!"
                        p "Yeah, but the camera got destroyed."
                        t "Ah, bummer!"
                        t "But at least now we didn't have to deal with a potential onset of a syncope caused by a gradual overload of the olfactory sensory neurons due to exposure to fecal matter!"
                        p "Fucking, WHAT?!"
                        t "Ha ha! Sorry, I'm babbling again!"
                        t "I just dropped some acid. I think it's starting to hit."
                        t "Hey, I think Hendrix is about to play soon!"
                        t "Let's go check him out!"
                        "There doesn't seem to be anything more left to do."
                        "Your weekend as the producer of Woodstock Music Festival is coming to a close."
                        "You start walking towards the main stage with Larry."
                        t "Are you seeing what I'm seeing?"
                        p "Probably not, since I haven't dropped any acid yet. What's up?"
                        t "I just had this vision of a bunch of students making a game about this very festival!"
                        p "That's great. Tell them to make it so that nothing goes wrong and every problem is easily fixed."
                        t "But where's the fun in that?"
                        $ day_two_end = "axe"
                        jump day2_ending
                    "Leave the door alone":
                        p "Maybe I should think this through..."
                        k "Yeah!!"
                        "You take a step back from the door."
                        jump looktoilets

            "Talk to [girl_name]":
                show chara girl neutral
                with dissolve
                mj "Ah, it's you!"
                mj "How's it going?"
                menu:
                    "Ask [girl_name] about using the winch" if winch_here == True:
                        p "You wouldn't know how to use a winch would you?"
                        mj "What's the problem?"
                        p "I have no idea how to use this thing."
                        mj "Well it's not very hard, is it? You just tie the cable around the thing you want pulled, and you turn the winch on."
                        p "Right..."
                        p "How come you know how to use this thing?"
                        mj "Like I said, it's not exactly rocket science."
                        mj "But I spend summers working the farmer's fields."
                        mj "Using a winch is pretty much the easiest thing when it comes to working on a farm."
                        menu:
                            "Ask [girl_name] to help you with the winch":
                                p "Could you help me use the winch to get this kid out?"
                                mj "Of course!"
                                mj "Let's just connect the cable first..."
                                "You watch as [girl_name] connects the winch cable to the toilet door."
                                "Making sure the cable is fastened tightly, she walks over to the truck's winch system."
                                "With a few presses of a button, [girl_name] starts the system."
                                "You watch as the truck's tires dig in to the ground as the cable starts to pull on the toilet door."
                                "Soon, a big loud \"POP\", like a bottle of soda being opened, is heard."
                                "The door of the toilet has cleanly pulled off at the hinges."
                                "Inside the toilet, you see a kid sitting down with a camera clutched in his arms."
                                show chara kid neutral
                                with dissolve
                                k "Oh wow!"
                                k "How'd you do that??"
                                p "That's all her."
                                show chara girl neutral
                                with dissolve
                                mj "Pleasure's all mine."
                                show chara kid neutral
                                with dissolve
                                k "Thanks for getting me out in one piece!"
                                k "It was getting really hot in there!"
                                k "I've got to go cool off this camera so the film isn't destroyed!"
                                k "But I'm sure we'll get the documentary made, no problem!"
                                k "Thanks again!"
                                hide chara kid neutral
                                with dissolve
                                "You see the kid running off with the camera towards the backstage area."
                                "The kid and [girl_name] exchange quick looks and a smile as they pass each other by."
                                show chara girl neutral
                                with dissolve
                                mj "Well, looks like my job here is done."
                                p "Thanks for taking care of that for me! I couldn't have hoped for a better result."
                                mj "No worries, it wasn't too difficult!"
                                mj "Anyway, I think Hendrix is playing soon and I want to go see him!"
                                mj "Hope there'll be no more problems for you to fix!"
                                p "Yeah, me too."
                                p "Hey, go and get free drinks and food at the stalls! Just mention that [player_name], the producer of the festival sent you."
                                mj "Dude, all the stalls are closed!"
                                mj "There's no more food left."
                                mj "There's nothing to drink."
                                mj "Everyone here is dirty, hungry and tired."
                                mj "And it's the best weekend any of us will ever have in our lives."
                                p "Oh... okay."
                                p "Well... thanks for your help then."
                                mj "Don't mention it!"
                                mj "I'm gonna go see Hendrix light his guitar on fire now!"
                                mj "Bye!"
                                hide chara girl neutral
                                with dissolve
                                "You see [girl_name] head towards the main stage."
                                "There doesn't seem to be anything more left to do."
                                "Your weekend as the producer of Woodstock Music Festival is coming to a close."
                                "As you walk towards the main stage, you hear Hendrix and his band setting up."
                                "For some reason, walking amongst the crowd makes you think of the lyrics of some Bob Dylan song Hendrix covered on his latest album..."
                                "\"No reason to get excited, the thief, he kindly spoke\"..."
                                "\"There are many here among us, who feel that life is but a joke\"..."
                                "\"But you and I, we've been through that, and this is not our fate\"..."
                                "\"So let us stop talking falsely now, the hour's getting late\"."
                                jump day2_ending
                            "Try to use the winch yourself":
                                p "I see. I think I'm going to try to use the winch myself then."
                                mj "Suit yourself..."
                                jump toilets
                    "Say you're still trying to get the kid out":
                        p "Good. I'm still trying to figure out this situation with the kid."
                        mj "Good luck! I'll see you around!"
                        jump toilets
            "Leave":
                jump toilets

label toilets_d2b:
    if d2b_toilet_first_visit == True:
        "As you enter the toilet area, you hear someone banging the door of a toilet from inside."
        k "Help! I'm stuck here!"
        p "Sorry, I've got more pressing matters to attend to."
        k "No!!"
        $ d2b_toilet_first_visit = False
    if farmer_found == False:
        "There doesn't seem to be much here except a young hippie girl."
        menu:
            "Talk to the girl":
                show chara girl neutral
                with dissolve
                mj "Hello. Can I help you?"
                menu:
                    "Ask about the farmer" if larry_farmer_talk == True:
                        p "I'm looking for the local farmer. Have you seen him by chance?"
                        mj "Oh, you mean Max? Yeah I know Max! I spend the summers working on his fields."
                        mj "I saw him walking around here a while back, but I haven't seen him in the last hour or so."
                        mj "Although it should be noted that Max has a habit of falling asleep when he's... you know."
                        p "Are you saying that the farmer has fallen asleep while on the toilet?"
                        mj "It's possible."
                        mj "He's a pretty heavy sleeper as well, so I don't think he'll wake up if we try to shout his name."
                        mj "And he doesn't snore, so it might be difficult to find him among all these toilets..."
                        mj "This happens quite often, actually."
                        mj "Usually when I need to ask him about this or that relating to the fields, I can't find him most of the time!"
                        p "Oh geez..."
                        p "I really, really need to find him. Any ideas?"
                        mj "We'll, there is this one cow that Max has..."
                        p "Max has a lot of cows."
                        mj "Yeah, I know but there's this calf named \"Shelley\" that has an amazing sense of smell!"
                        mj "She's like a hound dog!"
                        mj "She can find Max from miles away, just by smell!"
                        p "Do you think Shelley could help me find Max in this field of toilets?"
                        mj "Assuming Max is somewhere here, yeah, sure!"
                        p "Even despite the... smell?"
                        mj "Like I said, Shelley's like a hound dog!"
                        p "Okay..."
                        p "How do I find Shelley among all the other cows?"
                        mj "Just call her name, and she'll come to you!"
                        mj "She's really friendly!"
                        p "Okay, that sounds easy enough. I'll go find Shelley in the field now."
                        mj "Good luck!"
                        "(You can call for Shelley in the field now.)"
                        hide chara girl neutral
                        with dissolve
                        
                        $ mj_farmer_talk = True
                        jump toilets
                    "Leave":
                        p "Actually, never mind. Sorry to bother you."
                        mj "It's okay!"
                        jump toilets
            "Leave":
                jump map_screen
    else:
        "You run after Shelley as she makes her way around the festival area."
        "Crowds of people move out of the way and cheer as Shelley heads towards the toilet area."
        "You arrive at a toilet that is standing at the end of a long line of porta-potties."
        show chara bessie neutral
        with dissolve
        c "Mmmoooo!!"
        "Suddenly, you hear noises from inside the toilet in front of you."
        $ f = Character("Voice from inside the toilet", color="#6d594b")
        f "Shelley? Is that you, girl??"
        "The door of the toilet bursts open, and a large man climbs out of it."
        $ f = Character("Farmer Max", color="#6d594b")
        show chara farmer neutral
        with dissolve
        f "Shelley! What are you doing here, girl?"
        f "Did you come to fetch me for supper?"
        "The farmer notices you standing close by."
        f "Ah, hello! I don't believe we've met! My name is Max Yasgur, I'm the owner of this field!"
        p "Hello, I'm [player_name]. I'm the producer in charge of this festival."
        f "Ah, yes! I've heard about you!"
        p "Hopefully only good things?"
        f "Of course! Everyone is talking about this kid running around, fixing problems!"
        f "I hope everything is alright?"
        p "Yeah... Well, no."
        p "I'm sorry, but the field we are using as a landing site for our helicopters is filled with your cows."
        f "Really? I did lock them in their pen at the end of Thursday!"
        p "Yeah, I know, I know. The cows were let out by someone."
        f "Who let the cows out?"
        p "(Hmm... that could be a song title...)"
        p "It was the town supervisor. He got a little tipsy and decided to let the cows have their freedom."
        f "Ah yes, Danny likes a bit of drink, he does..."
        f "Well it's not the end of the world! I can come and move the cows back in to their pen if you want?"
        p "That'd be excellent, thank you!"
        f "Well alrighty then, let's get going!"
        $ day_two_end = "happycows"
        jump field