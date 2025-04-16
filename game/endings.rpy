#
# DETERMINING WHICH ENDING HAPPENS
#


label ending:


    if mayor_happy==False:
        jump bad_ending
    elif monster_dead==False:
        jump neutral_ending
    else:
        jump good_ending


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
    "Game Over. (Ending C)"
    return


label neutral_ending:


    scene neutral_ending
    with fade
    "The festival is started."
    "Everything goes according to plan and the festival is a great success."
    "More than 460,000 people visit the festival over the weekend."
    "The music and the political message of the festival attains a mythical status as a symbol of the 1960's counter-culture movement."
    "You are known as the person who made it all happen, and you spend the rest of your days organizing various successful music events."
    "In 2019, a podcast series gains popularity all over the world."
    "The series describes the history of Woodstock Music Festival and its cultural impact." 
    "The final episode of the series focuses on the mysterious disappearance of all the townspeople of Bethel following the festival weekend."
    "No rational reason is found as to how an entire town of 3,959 people can suddenly disappear between Monday 18th and Tuesday 19th of August, 1969."
    "Game Over. (Ending B)"
    return


label good_ending:


    scene good_ending
    with fade
    "The festival is started."
    "Everything goes according to plan and the festival is a great success."
    "More than 460,000 people visit the festival over the weekend."
    "The music and the political message of the festival reach a mythical status as a symbol of the 60's counter-culture movement."
    "You are known as the person who made it all happen, and you spend the rest of your days organizing various successful music events."
    "In 2019, a podcast series gains popularity all over the world."
    "The series describes the history of Woodstock Music Festival and its cultural impact." 
    "The final episode of the series describes how world peace was achieved following the festival weekend."
    "In interviews, numerous world leaders from the 1960's describe how they felt like \"a great malice\" had been removed from the world during Woodstock Music Festival."
    "Mankind has enjoyed a golden era of peace and prosperity for a thousand years now."
    "Game Over. (Ending A)"
    return


label death:


    scene bg death
    with fade
    "You are dead. Game Over. (Ending E)"
    menu:
        "Try again":
            jump monster_battle
        "Exit game":
            return
