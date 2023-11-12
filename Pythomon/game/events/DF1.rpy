label df1:
    scene forest background with dissolve
    "We make our way through the forest until..."
    #An ant shows up
    play music "audio/bgm/forest theme.mp3" loop
    show ant with dissolve
    pause 2
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    py dotdotdot "An ant?"
    show pychan at right
    mc nervous "Yeah, no jack. What do you think it was?"
    py normal "Let's fight it."
    show pychan at right
    mc nervous  "Wait, you just said it was an ant."
    py jeez  "Fight. It."
    show pychan at right
    mc closeeye "Oh, geez..."
    hide ant
    #############################################
    $ df1 = True
    $ opp_mon_hp = 555
    $ opp_skill_position1 = ["Sting", "Bite", "Pheromone"]
    $ opp_skill_dmg_position1 = [150, 222, 0]
    $ oppmonster1 = "Ant"
#############################################
    call reset
    call hide_all
    play music "audio/bgm/battle.mp3" loop
    scene forest background blur with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df1 = False
#############################################
    play music "audio/bgm/forest theme.mp3" loop
    scene forest background with dissolve
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    mc nervous "That one was definitely tougher than Lemon."
    mc lookatme "Anyway, not a fan of peace?"
    py jeez "Since our intel was stolen by Project Prologue, it's best we accumulate some more data."
    py normal "Anyway, I recorded it's DNA. Let's keep going."
    show pychan at right
    nara "Not a hint of symphathy, huh. Had no idea LAB:MEMB was this cruel at work."
    call hide_all
    menu df1_next:
        "Forward!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call df2
        "Right!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call bdf_2
