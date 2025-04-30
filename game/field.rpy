#
# FIELD
#

label field:
    scene bg field
    with fade
    if day_two_end == "happycows":
        jump farmer_and_cows
    if day_one_end == "whisky":
        "You arrive to the landing site that's full of cows grazing."
    jump actionsmenu

label talkfield:
    menu:
        "Try to communicate with the cows":
            p "Moo?"
            "MOO!"
            jump talkfield
        "Ask farmer to move cows" if farmer_awake:
            p "Could you move the cows, Max?"
            "The farmer moves the cows."
            $ day_two_end = "happycows"
            jump day2_ending
        "Back":
            jump actionsmenu

label cow_talk_menu:
    menu:
        "Ask Shelley to find John":
            "Shelley doesn't understand who's being talked about."
            jump cow_talk_menu
        "Ask Shelley to find Marty":
            "Shelley doesn't understand who's being talked about, but she gives a quick glance toward the festival area."
            jump cow_talk_menu
        "Ask Shelley to find Max":
            c "Mooooooooooooox!!"
            "Suddenly, Shelley starts running off toward the festival area."
            "You run after Shelley as fast as you can."
            $ farmer_found = True
            $ location = "toilets"
            $ talk_to = "farmer"
            jump toilets
        "Ash Shelley to find JFK":
            "All of a sudden, Shelley looks a bit sad."
            c "Moo..."
            jump cow_talk_menu
        
label lookfield:
    if day_one_end == "whisky":
        menu:
            "The cows seem udderly uninterested in you or the socio-political importance of Woodstock."
            "Call for Shelley" if mj_farmer_talk == True:
                p "Shelley! Shelley! Here, cow!"
                "You see a happy looking cow run over to you."
                show chara bessie neutral
                with dissolve
                c "Moooooooooo <3!"
                menu:
                    "Ask Shelley to find the farmer":
                        p "Shelley! Find the farmer! Find the farmer for me!"
                        "Shelley looks at you with confused eyes."
                        p "Damn. Maybe I need to use the farmer's name?"
                        p "What was it...?"
                        jump cow_talk_menu
                    "Leave Shelley alone":
                        p "Thanks Shelley! I'm all good!"
                        c "Moo!"
                        "Shelley runs back in to the field."
                        hide chara bessie neutral
                        with dissolve
                        jump lookfield
                
            "Carefully try to move the cows":
                "You try to nudge the cows a little bit, but they don't budge."
                jump lookfield
            "Shout":
                p "Okay, come on cows! Let's move!"
                p "LET'S MOVE!"
                p "SHOO! SHOO!"
                p "Jimi Hendrix is supposed to come here to play!!"
                "The cows don't seem to fully appreciate what you're saying."
                jump lookfield
            "Shove the cows":
                "The cows seem to get visibly angry."
                "Their nostrils flare, as they start to move towards you menacingly."
                "It should be noted that cows are responsible for an average of 22 human deaths in the U.S. each year."
                menu:
                    "Fight the cows":
                        "You decide to challenge the cows in hand-to-hoof combat."
                        "The cows form a ring around you, and you see a big cow make its way towards you."
                        "The rest of the herd starts mooing loudly, and you have hardly any time to react as the big bad cow launches its attack on you."
                        "The last thing you remember before waking up in the hospital is a massive hoof approaching your face."
                        $ day_two_end = "cowfight"
                        jump day2_ending
                    "Leave the cows alone":
                        p "Okay, chill! Don't have a cow..."
                        p "I mean, I've really got no beef with any of you. I mean-"
                        p "Ah, the hell with this."
                        "You ran away from the cows as fast as you can."
                        jump field
            "Back":
                jump actionsmenu

    elif day_one_end == "money":
        if winch_here == False:
            "You see a lonely truck sitting in the middle of a field."
            if town_supervisor_toilettalk == True:
                p "Maybe this was the truck the town supervisor was talking about?"
                "You take a closer look at the truck, and you notice that there is a winch-pulley system attached to it."
                menu:
                    "Get in the truck":
                        "The truck seems to be unlocked."
                        "You get in and find the keys inside the glove compartment."
                        menu:
                            "Drive the truck to the toilet area":
                                if truck_fixed == False:
                                    "You try to start the engine, but nothing happens."
                                    $ truck_started = True
                                    "Someone with some experience with cars might know what's the problem."
                                    "As it stands, you leave the truck alone."
                                    jump field
                                elif truck_fixed == True:
                                    "The engine starts with a cough."
                                    "You drive the truck to the toilet area."
                                    $ location = "toilets"
                                    $ talk_to = "kid in the toilet"
                                    $ winch_here = True
                                    jump toilets
                            "Leave the truck alone":
                                "You put the keys back in to the glove compartment and leave the car alone."
                                jump field
                    "Leave the truck alone":
                        "You let the truck sit idly in the field."
                        jump actionsmenu
            else:
                jump actionsmenu
        else:
            "The field is empty."
            jump actionsmenu
        jump actionsmenu

label farmer_and_cows:
    "You arrive at the landing site with Max and Shelley."
    show chara farmer neutral
    with dissolve
    f "Alright girls, let's get you back in to your pen!"
    "The farmer swiftly but gently gestures the cows back in to their pen."
    "In no time at all, the field has been emptied."
    p "Wow, that was fast! Thank you so much!"
    f "Heh heh..."
    f "It ain't much, but it's honest work!"
    "With the field now empty, the helicopters carrying crew and band members soon start arriving."
    "You see a man carrying a guitar case climb out of a helicopter, and walk towards you."
    show chara hendrix neutral
    with dissolve
    h "How's it going?"
    h "I saw the crowds from the helicopter..."
    h "This is pretty far out, man!"
    show chara farmer neutral
    with dissolve
    f "Pleasure to meet you, sir! I'm Max Yasgur!"
    show chara hendrix neutral
    with dissolve
    h "Hello, hello! I'm Jimi."
    show chara farmer neutral
    with dissolve
    f "What kind-a gee-tar you have in that case there?"
    show chara hendrix neutral
    with dissolve
    h "Oh you know, it's just a Stratocaster..."
    show chara farmer neutral
    with dissolve
    f "Very nice! Would it be possible for me to see it?"
    show chara hendrix neutral
    with dissolve
    h "Yeah, sure. Do you play?"
    show chara farmer neutral
    with dissolve
    f "I sure do! Nothing fancy, though!"
    show chara hendrix neutral
    with dissolve
    h "It doesn't matter, I'm always up for a jam. C'mon, let's go check what kind of amps they have here."
    show chara farmer neutral
    with dissolve
    f "Sounds good to me! Lead the way, Jimi!"
    hide chara farmer neutral
    with dissolve
    "You watch as Hendrix and Max walk away."
    "There doesn't seem to be anything more left to do."
    "Your weekend as the producer of Woodstock Music Festival is coming to a close."
    "As you head back towards the festival area, you suddenly hear Max's voice coming over the loudspeakers."
    "In the distance, his voice can be heard echoing far and wide."
    "You listen in to what Max has to say."
    f "I'm a farmer…"
    "You hear the crowd cheering."
    f "I don't know how to speak to twenty people at one time, let alone a crowd like this."
    f "But I think you people have proven something to the world..."
    f "Not only to the Town of Bethel, or Sullivan County, or New York State..."
    f "You've proven something to the world."
    f "This is the largest group of people ever assembled in one place." 
    f "We have had no idea that there would be this size group, and because of that you've had quite a few inconveniences as far as water, food, and so forth."
    f "Your producers have done a mammoth job to see that you're taken care of... they'd enjoy a vote of thanks."
    "You hear the crowd cheering and clapping loudly in the distance."
    f "But above that, the important thing that you've proven to the world is that a half a million kids..."
    f "And I call you kids because I have children that are older than you are..."
    f "A half million young people can get together and have three days of fun and music, and have nothing BUT fun and music..."
    f "and I - God Bless You for it!"
    "As the crowd erupts in to an applause, you head towards your trailer for a well-earned rest."
    jump day2_ending
