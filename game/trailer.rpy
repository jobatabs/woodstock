#        
# TRAILER
#

# After the starting set-up, the game properly begins
label trailerstart:

    scene bg trailer
    with fade
    "It is the morning of August 15th, 1969."
    "You wake up hungover in your trailer and look around a bit."
    "Last night's launch party was really quite something..."
    "Hazy memories from various scenes of debauchery appear in your mind."
    "It seems like the previous night was nothing but a bacchanal of booze, music, shovels and money."
    "Eventually you pull yourself together and get up from your bed."
    "As you throw on some random clothes from the floor, you try to focus on the day ahead."
    p "Man... what a party last night."
    p "I was hired to make sure this festival goes on without a hitch."
    p "It was a lot of work, but I think we managed to get all the pre-production stuff sorted."
    p "The rest of the weekend should then be pretty straightforward..."
    p "I should head out and go make sure everything is running smoothly today."
    $ playertip = "I should go backstage and talk to Larry."
    menu:
        "Okay, let's get out there and get stuff done. (Leave the trailer)":
            "As you make your way towards the door, you notice a note taped to your wall."
            "Someone has left a message for you."
            "\"[player_name]! The town supervisor came by earlier and was asking about some permit!\""
            "\"Come talk to me as soon as you wake up! I'll be in the backstage area.\""
            "The note has been signed by \"Larry\"."
            "\"P.S. great party last night\""
            "You have a faint memory of hiring someone named Larry to be the lighting technician for the stage..."
            "Looks like you need to go find Larry."
            jump map_screen
        "Wait, who am I?":
            "Your name is [player_name], and you are the producer in charge of putting together the Woodstock Music Festival."
            menu:
                "Oh, okay then. Well, let's get going! (Leave your trailer)":
                    "As you make your way towards the door, you notice a note taped to your wall."
                    "Someone has left a message for you."
                    "\"[player_name]! The town supervisor came by earlier and was asking about some permit!"
                    "\"Come talk to me as soon as you wake up! I'll be in the backstage area.\""
                    "The note has been signed by \"Larry\"."
                    "\"P.S. great party last night\""
                    "You have a faint memory of hiring someone named Larry to be the lighting technician for the stage..."
                    "Looks like you need to go find Larry."
                    jump map_screen
                "Huh? What is \"The Woodstock Music Festival\"":
                    "The Woodstock Music and Art Fair, commonly referred to as Woodstock, was a music festival held from August 15 to 18, 1969, on a dairy farm in Bethel, New York, 40 miles (65 km) southwest of the town of Woodstock."
                    "Billed as \"An Aquarian Exposition: 3 Days of Peace & Music\" and alternatively referred to as the Woodstock Rock Festival, it attracted an audience of more than 460,000."
                    "Thirty-two acts performed outdoors despite overcast and sporadic rain. It was one of the largest music festivals in history and became synonymous with the counterculture of the 1960s."
                    "The festival has become widely regarded as a pivotal moment in popular music history, as well as a defining event for the silent and baby boomer generations."
                    menu:
                        "Cool! Well, let's get going. (Leave your trailer)":
                            "As you make your way towards the door, you notice a note taped to your wall."
                            "Someone has left a message for you."
                            "\"[player_name]! The town supervisor came by earlier and was asking about some permit!"
                            "\"Come talk to me as soon as you wake up! I'll be in the backstage area.\""
                            "The note has been signed by \"Larry\"."
                            "\"P.S. great party last night\""
                            "You have a faint memory of hiring someone named Larry to be the lighting technician for the stage..."
                            "Looks like you need to go find Larry."
                            jump map_screen


label trailer:
    scene bg trailer
    with fade
    if day == 1:
        "Your trailer is a mess. You can still smell the booze from last night."
    else:
        p "Ah, another day in this stinky trailer."

    jump actionsmenu


label day2_trailer:
    scene black with wiperight

    show text "Day 2" at truecenter with dissolve

    pause 1.0

    hide text with dissolve

    pause 0.3

    $ location = "trailer"

    jump day2_trailerstart

label day2_trailerstart:
    scene bg trailer
    with fade
    "You wake up with a renewed sense of focus."
    if day_one_end == "whisky":
        "You're glad you had kept that whisky bottle around, it really smoothed things over with the town supervisor."
    else:
        "You're relieved you had the foresight to keep those emergency funds around. If only you hadn't buried it at the party, though..."
    "Suddenly, a knock comes on your door."
    "Larry is there."
    show chara technician frightened
    with dissolve
    t "[player_name]! Come on, man! It's almost noon!"
    p "Oh man... I did it again."
    t "There's some kid named Marty stuck in a toilet."
    p "So? Why is this important?"
    if day_one_end == "money":
        t "You see, he's part of the film crew. You know, the guys making that documentary?"
        "You vaguely recall something about a film crew..."
        "Suddenly, you remember the fine print that caught your eye when you signed the work contract with the festival."
        "It is stipulated in your contract that your pay for the weekend will be docked if the film crew - for whatever reason - fails to make a documantary about the festival."
        p "Ah, shit!"
        p "What's up with him?"
        t "The kid's carrying the film crew's camera with him. Don't know why he took it with him to the toilet, though."
        menu:
            "Say \"I guess he was told not to let it out of his sight?\"":
                p "I guess he was told not to let it out of his sight?"
                t "Yeah, I guess so. Seems pretty extreme to me, though."
            "Say \"I guess he was told to \"Go film some shit\" or something.":
                p "I guess he was told to \"Go film some shit\" or something."
                t "Really...?"
                t "Man, these guys are really committed to capturing absolutely EVERYTHING from the festival..."
        t "Anyway, I think the film inside the camera is slowly getting cooked by the heat. Those porta-potties get really hot if you keep the door closed for too long!"
        t "I think you gotta get him out of there before the whole roll of film is destroyed!"
        p "Yeah, you're totally right. I have to get him out of there as soon as possible!"
        $ playertip = "Let's see how the kid got stuck."
    else:
        t "You see, he's part of the film crew. You know, the guys making that documentary...?"
        "You vaguely recall something about a film crew..."
        t "But we have an even bigger problem!"
        p "Let me guess, you're out of beer?"
        t "What? No!"
        t "I mean, yes! I'm out of beer! But that's not what I meant!"
        p "What is it, then?"
        t "The helicopter landing area has become unusable!"
        p "Unusable? How has the helicopter landing area become \"unusable\"?"
        t "It's filled with cows!"
        p "Filled with cows?! A heard of cows?!"
        t "Yes, of course I've heard of cows! I'm telling you about them at this very moment!!"
        p "No Larry, I-"
        p "Just... forget it."
        p "How is there a bunch of cows in the helicopter landing site?"
        p "They were supposed to be contained within their little cow pen!"
        t "I know, I know! But somehow they've broken free and now they've launched an assault on the helicopter landing area!"
        t "If you don't get the cows out of there, we have no way to bring in Jimi Hendrix to play his set today!"
        t "A lot of people are looking forward to seeing him play!"
        p "I know, he's today's main performer..."
        t "You gotta wrangle some cows, [player_name]!"
        menu:
            "Go move the cows":
                p "Okay. Time go move some bovine."
                t "Good luck, man!"
            "Ask Larry to move the cows":
                p "Why can't you go deal with the cows?"
                t "Sorry man, I'm legally not allowed to touch any cows that are still alive."
                t "If they were dead, it'd be a totally different matter."
                "You suddenly get the feeling that it would probably be best to not get Larry involved in this business with the cows."
                p "Right. I'll go deal with the cows then."
                t "Good luck, man!"
        $ playertip = "Let's see what can be done about these cows."
    "Larry leaves."
    hide chara
    with dissolve
    jump actionsmenu
    


label looktrailer:
    menu:
        "Note taped to the wall" if day == 1:
            "Someone has left a message for you."
            "\"[player_name]! The town supervisor came by earlier and was asking about some permit!"
            "\"Come talk to me as soon as you wake up! I'll be in the backstage area.\""
            "The note has been signed by \"Larry\"."
            "\"P.S. great party last night\""
            jump looktrailer

        "Under the bed":
            if have_metal_detector == False:
                "Your trusty FEW57ER-9000 Mine Detector lies abandoned under your bed."
                menu:
                    "Take the mine detector":
                        "You take the well-used mine detector with you."
                        $ have_metal_detector = True
                        jump looktrailer
                    "Leave the mine detector":
                        "You leave the mine detector to its fate."
                        jump looktrailer
            else:
                "Apart from a half-eaten hot-dog and an unopened pack of condoms that is past its expiry date, there is not much here."
                jump looktrailer
        
        "Cabinet":
            if have_whisky == False:
                "You find a bottle of whisky in the cabinet."
                "This particular whisky is pretty top-shelf stuff. You've been saving it for a special occasion."
                menu:
                    "Take the bottle":
                        "You take the bottle with you."
                        $ have_whisky = True
                        jump looktrailer
                        
                    "Leave the bottle":
                        p "There's no time to get drunk now."
                        "You leave the bottle."
                        jump looktrailer
            else:
                "The cabinet is smelly, empty, and dirty."
                jump looktrailer

        "Bed":
            "Your bed calls to you, promising comfort beyond belief..."
            menu:
                "Rest a bit":
                    "You lay down and relax for a moment."
                    "Time passes."
                    "You feel rested."
                    menu:
                        "Keep resting":
                            "You keep relaxing for a bit more."
                            "Time passes."
                            "You feel more rested."
                            menu:
                                "Try to fall asleep.":
                                    "You keep relaxing, even though you have a festival to save."
                                    "You try to fall asleep."
                                    "Time passes."
                                    "You have succesfully stared at the ceiling for some time."
                                    if mystical_stone==True:
                                        if monster_dead==False:
                                            menu:
                                                "Try to fall asleep one more time.":
                                                    "You fall in to a deep, mystic slumber."
                                                    jump monster_battle
                                                "Get up":
                                                    "With a sigh, you wrench yourself up."
                                                    jump looktrailer
                                        else:
                                            menu:
                                                "Get up":
                                                    "With a sigh, you wrench yourself up."
                                                    jump looktrailer
                                    else:
                                        menu:
                                            "Get up":
                                                "With a sigh, you wrench yourself up."
                                                jump looktrailer
                                "Get up":
                                    "With a sigh, you wrench yourself up."
                                    jump looktrailer
                        "Get up":
                            "With a sigh, you wrench yourself up."
                            jump looktrailer
                "Stay up":
                    "This isn't the time to rest."
                    jump looktrailer


        "Back":
            jump actionsmenu