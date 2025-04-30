#
# DETERMINING WHICH ENDING HAPPENS
#


label ending:


    if mayor_happy==False:
        jump bad_ending
    elif day_one_end=="whisky":
        $ day = 2
        $ mayor_happy = False
        jump d2b_start
    else:
        $ day = 2
        $ mayor_happy = False
        jump d2a_start

label day2_ending:
    if day_two_end=="cowfight":
        jump d2_bad
    elif day_two_end=="happycows":
        jump d2_neutral_b
    elif day_two_end=="axe":
        jump d2_neutral_a
    else:
        jump d2_best
    


label bad_ending:


    scene bg bad_ending
    with fade
    "The festival is started."
    "However, before the gates are even opened, the sheriff and his boys arrive in their pick-up trucks."
    "They start rounding up and beating on the festival guests."
    "The festival is shut down and your reputation as a festival organizer is destroyed."
    "You end up paying for various legal and medical fees for the rest of your life."
    "If you had insurance, it would have covered all damages."
    "As it stands, Woodstock Music Festival disappears in to the waves of history."
    "56 years from now, no-one remembers what happened on that weekend of August 15th to 18th, 1969."
    "Game Over. (Ending D)"
    return


label d2b_start:


    scene neutral_ending
    with fade
    "Day one is over."
    "You solved your problems with alcohol."
    jump day2_trailer

label d2a_start:


    scene neutral_ending
    with fade
    "Day one is over."
    "You solved your problems with money."
    jump day2_trailer


label good_ending:


    scene bg intro1
    with fade
    show chara technician happy
    with dissolve
    "Larry the Technician wasn't bummed out anymore after he found some beer."
    "He continued to fight the man by working as a technician at primo concerts."
    show chara mayor neutral
    with dissolve
    "The town supervisor Daniel Amatucci faced criticism from the conservatives in his constituency and lost his re-election bid later that year."
    "The local clergy played a hand at ousting him because of his pro hippie viewpoints."
    show chara girl neutral
    with dissolve
    "Mary Jane Blunt stays on to work with farmer Max and eventually inherits the farm. Groovy!"
    "She helps draft dodgers hide in the farm."
    show chara kid neutral
    with dissolve
    "Marty gains some fame because of working on the crew of the excellent documentary that cements Woodstock's place in history and contemporary culture."
    "After helping make Woodstock the phenomenon it is in our collective memory, Martin Scorsese moved on to make some pretty famous fictional films."
    show chara hendrix neutral
    with dissolve
    "The festival runs late and finally early Monday morning Jimi Hendrix plays his famous solo and adds to the cultural legacy of the most important concert ever."
    hide chara hendrix neutral
    with dissolve
    "You really have a knack for the music business. Well done! You keep on working in the business and organise successful festivals one after another."
    "Though none can live up to the memory of Woodstock."
    scene bg intro2
    with dissolve
    "Game Over. (Ending A)"
    return


label death:


    scene bg death
    with fade
    "You are dead."
    "Game Over. (Ending E)"
    menu:
        "Try again":
            jump monster_battle
        "Exit game":
            return


label d2_bad:
    scene bg intro1
    with fade
    show chara technician happy
    with dissolve
    "Larry the Technician wasn't bummed out anymore after he found some beer."
    "He continued to fight the man by working as a technician at primo concerts."
    show chara mayor neutral
    with dissolve
    "Because of the part the town supervisor Daniel Amatucci played in the failure of Woodstock, the clergy and other conservatives in his constituency praised his name and re-elected him with huge margins later that year."
    "As a new conservative darling, he went on to work for the Nixon administration."
    show chara girl neutral
    with dissolve
    "Mary Jane Blunt stays on to work with farmer Max and eventually inherits the farm. Groovy!"
    "She helps draft dodgers hide in the farm."
    show chara farmer neutral
    with dissolve
    "Farmer Max really enjoyed the concert. His speech from the main stage was a huge hit."
    show chara kid neutral
    with dissolve
    "The kid Marty was stuck in the toilet for far too long."
    "The heat in the port-a-potty destroyed the film and the camera and thus the possibility of cementing Woodstock's place in history and contemporary culture."
    "Despite this failure, Martin Scorsese moved on to make some pretty famous fictional films."
    show chara hendrix neutral
    with dissolve
    "The concert fizzled out during the weekend because many of the artists were not able to land by helicopter."
    "Jimi Hendrix was never able to play Woodstock."
    hide chara hendrix neutral
    with dissolve
    "You got hurt pretty bad by the cows. Physically and emotionally."
    "The music business is obviously not for you. After some serious soul-searching you go on to work the town supervisor Amatucci's re-election campaign."
    "You actively push out any memories of Woodstock."
    scene bg intro2
    with dissolve
    "Game Over. (Ending C)"
    return

label d2_best:
    jump good_ending

label d2_neutral_a:
    scene bg intro1
    with fade
    show chara technician happy
    with dissolve
    "Larry the Technician wasn't bummed out anymore after he found some beer."
    "He continued to fight the man by working as a technician at primo concerts."
    show chara mayor neutral
    with dissolve
    "The town supervisor Daniel Amatucci faced criticism from the conservatives in his constituency and lost his re-election bid later that year."
    "The local clergy played a hand at ousting him because of his pro hippie viewpoints."
    show chara girl neutral
    with dissolve
    if girl_name == "Mary Jane":
        "Mary Jane Blunt stays on to work with farmer Max and eventually inherits the farm. Groovy!"
        "She helps draft dodgers hide in the farm."
    else:
        "Mary Jane Blunt dedicates her life to designing more secure port-a-potties. Heavy!"
    show chara kid neutral
    with dissolve
    "Marty's crew never finishes the film because the camera is destroyed."
    "Your axe-wielding ways destroy the possibility of cementing Woodstock's place in history and contemporary culture."
    "Despite this failure, Marty moved on to make some pretty famous fictional films."
    "With your violent antics you became an inspiration to his films Like a Raging Bull and Taxi Driver."
    show chara hendrix neutral
    with dissolve
    "The festival runs late and finally early Monday morning Jimi Hendrix plays his famous solo."
    "Only around 40 000 people are left to hear him play. Unfortunately, no record remains and the cultural weight of the moment is not felt nation-wide."
    hide chara hendrix neutral
    with dissolve
    "You have some ability for the music business. Not too bad!"
    "Unfortunately, you lose part of your pay because the documentary never gets made – and your employer was really looking forward to it."
    "Strapped for cash you turn to your second passion, real-estate and become a realtor of mid-range houses." 
    "You enjoy your work but every now and then the memory of Woodstock makes you wonder..."
    scene bg intro2
    with dissolve
    "Game Over. (Ending B-1)"
    return

label d2_neutral_b:
    scene bg intro1
    with fade
    show chara technician happy
    with dissolve
    "Larry the Technician wasn't bummed out anymore after he found some beer."
    "He continued to fight the man by working as a technician at primo concerts."
    show chara mayor neutral
    with dissolve
    "The town supervisor Daniel Amatucci faced criticism from the conservatives in his constituency and lost his re-election bid later that year."
    "The local clergy played a hand at ousting him because of his pro hippie viewpoints."
    show chara girl neutral
    "Mary Jane Blunt stays on to work with farmer Max and eventually inherits the farm. Groovy!"
    "She helps draft dodgers hide in the farm."
    show chara bessie neutral
    with dissolve
    "Shelley the Cow lives happily on farmer Max's farm."
    show chara farmer neutral
    with dissolve
    "Farmer Max really enjoyed the concert. His speech from the main stage was a huge hit."
    show chara kid neutral
    with dissolve
    "The kid Marty was stuck in the toilet for far too long."
    "The heat in the port-a-potty destroyed the film and the camera and thus the possibility of cementing Woodstock's place in history and contemporary culture."
    "Despite this failure, Martin Scorsese moved on to make some pretty famous fictional films."
    show chara hendrix neutral
    with dissolve
    "The festival runs late and finally early Monday morning Jimi Hendrix plays his famous solo."
    "Only around 40 000 people are left to hear him play. Unfortunately, no record remains and the cultural weight of the moment is not felt nation-wide."
    hide chara hendrix neutral
    with dissolve
    "You have some ability for the music business. Not too bad!"
    "Unfortunately, you lose part of your pay because the documentary never gets made - and your employer was really looking forward to it."
    "Strapped for cash you turn to your second passion, real-estate and become a realtor of mid-range houses." 
    "You enjoy your work but every now and then the memory of Woodstock makes you wonder..."
    scene bg intro2
    with dissolve
    "Game Over. (Ending B-2)"
    return