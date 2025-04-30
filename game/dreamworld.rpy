#
# DREAMWORLD MONSTER BATTLE
#

define c = Character("Cosmic Being", color="#4a1ea2")

# Has the player killed the monster in the dreamworld? (Unlocks the best ending)
default monster_dead = False

label monster_battle:


    scene bg monsterlair
    with fade
    "You wake up in some sort of alternative dimension."
    "Suddenly, you hear a voice in the distance."
    show monster
    with dissolve
    "A large entity that cannot be described by words appears before you."
    "You feel your lifeforce being sapped away by this unimaginable being as you try to find the right words."
    j "Y'ai 'ng'ngah, Yog-Sothoth h'ee - l'geb f'ai throdog uaaah."
    menu:
        "You are my master, and I give my life to thee.":
            "Slowly, the creature feeds on your spirit. You slip in to an endless darkness."
            jump death
        "What are you, some kind of stupid off-brand Jesus?":
            "You hear a voice that seems to be coming from inside your head."
            j "Insolent fool. You wish to challenge my power? I have lived since the beginning, before your kind even had developed ears or eyes."
            j "You will bow before my power. I shall feed on your kind for an eternity."
            menu:
                "Please don't kill me.":
                    "Slowly, the creature feeds on your spirit. You slip in to an endless darkness."
                    jump death
                "I think you look kind of dumb.":
                    j "How dare you. You are an insignificant speck of matter. I will never stop feasting on you. You will suffer for a thousand generations."
                    menu:
                        "I didn't mean it. Don't kill me. Please.":
                            "Slowly, the creature feeds on your spirit. You slip in to an endless darkness."
                            jump death
                        "You fight like a dairy farmer!":
                            j "How appropriate. You fight like a cow!"
                            "The creature's fierce comeback causes the flesh from your bones to evaporate instantly."
                            jump death

                        "u r dumb lol":
                            "The creature in front of you recoils in horror at this insult. You start to feel your lifeforce returning to you."
                            "Over in the infinite distance, the creature seems to scream in anger."
                            "White flames envelop the creature as it makes a sound that seems to continue to echo forever."
                            hide monster
                            with dissolve
                            "Soon, nothing of the creature remains but a blob of dark matter."
                            $ monster_dead = True
                            "With the creature gone, you feel your consciousness shift back in to your corporeal body."
                            jump trailer
