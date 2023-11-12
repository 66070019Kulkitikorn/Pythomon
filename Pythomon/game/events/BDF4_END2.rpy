label bdf_4:
    scene darktree with dissolve
    "I've decided to go for the final push, I can practically feel danger crawling on my spine."
    play music "audio/bgm/monika.mp3" loop
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    mc "You know, you sure seem awfully nervous when we have the recall technology on our side."
    mc lookatme "I'll leave as soon as I'm done with the mission."
    py nervous "That's true but..."
    show pychan at right
    mc nervous "There's a but?"
    py ahhh "You should only rely on recall sparingly..."
    show pychan at right
    mc "Why?"
    call hide_all
    play audio "audio/Monster2.ogg"
    show truestring with hpunch
    play music "audio/bgm/climax.mp3" loop
    nara "Before I can get my answer, the murderous intent has caught my attention and prompted me to turn."
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    py normal "There it is! That's the True Sting!"
    show pychan at right
    mc nervous "This looks way more dangerous than anything we've encountered..."
    py jeez "Too late for regrets now! Prepare to commit!"
    hide truestring
    #############################################
    $ bdf_4 = True
    $ opp_mon_hp = 1500
    $ opp_skill_position1 = ["Plague", "Purge", "Propagation"]
    $ opp_skill_dmg_position1 = [150, 250, 0]
    $ oppmonster1 = "True Sting"
#############################################
#############################################
    call reset
    call hide_all
    play music "audio/bgm/truestring theme.mp3" loop
    scene darktree blur with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ bdf_4 = False
#############################################
    #Commit True String
    scene darktree with dissolve
    play music "audio/bgm/monika.mp3" loop
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    mc nervous "It's way too strong! Looks like it got bored of us and left, though..."
    py angry "Enough about that! We've got its DNA let's hurry up and leave!"
    py "Let's recall and submit the research!"
    show pychan at right
    mc "I'm already trying to... but..."
    stop music
    call hide_all
    nara "Recall has been banned."
    scene darktree red with dissolve
    play music "audio/bgm/climax.mp3" loop
    nara "The surroundings suddenly start to turn red."
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    mc angry "It's disabled..."
    py dotdotdot "..."
    show pychan at right
    nara "Even though, we went through all that..."
    mc "There must be another way, but first we have to get out of here!" with hpunch
    nara "I try to backtrack."
    nara "But..."
    mc "It's blocked!" with hpunch
    py dotdotdot "..."
    show pychan at right
    mc "I can't call Hiyajou either!" with hpunch
    py uh "[povname]"
    show pychan at right
    mc "Huh?"
    py "I think we're out of luck."
    show pychan at right
    mc "Out of luck?"
    show pychan at right
    nara "Pychan stares straight into my soul."
    py jeez "I told you, didn't I? Nobody can exit the danger zone."
    show pychan at right
    mc nervous "!" with hpunch
    py nervous "If I have to guess, Project Prologue already took control of the firewall."
    py "But regardless of the method, we can't do anything anymore."
    show pychan at right
    mc nervous "..."
    py normal "But don't worry. You still have me."
    py "AI cannot detoriate away, so I'll stay with you."
    hide bluepy with slowdisslove
    stop music fadeout 1.0
    py "Forever."
    hide pychan with dissolve
    hide yuukii with dissolve
    "Looks like I really messed up this time."
    "I try many times but recall keeps on giving me the silent treatment."
    "Looks like I'm stuck here."
    "There's no way out."
    "Not even the sound of anyone."
    "Except for Pychan."
    "This mission... is a failure."
    "Chapter 1: Ending 2"
    $ renpy.quit()

    
