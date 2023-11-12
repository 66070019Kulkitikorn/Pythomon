label df3_2:
    #mc = yuki py = pychan pl2 = Prologue Punk 2
    scene forest background with dissolve
    play music "audio/bgm/forest theme.mp3" loop
    show yuukii at left with dissolve
    show keke2 with dissolve
    pl2 "Another LAB:MEM? I guess another win for me, then."
    call hide_all
    show keke2
    show bluepy 
    show yuukii at left
    show pychan at right with dissolve
    py dotdotdot "Is this some kind of slogan? Why are they saying the same thing..."
    hide bluepy 
    hide pychan 
    nara "The grunt intensely stares at me."
    nara "I can already see the dollar signs in their eyes, they're coming for the money."
    pl2 "Since you came right to us, I'll go ahead and take those research on you!"
    mc nervous "Why do they want it so much..?"
    call hide_all
    show keke2
    show bluepy 
    show yuukii at left
    show pychan at right with dissolve
    py jeez "Just forget that and let's commit!"
    #############################################
    $ df3_2 = True
    $ opp_mon_hp = 600
    $ opp_skill_position1 = ["Sting", "Stinger", "Work"]
    $ opp_skill_dmg_position1 = [99, 300, 0]
    $ oppmonster1 = "Bee"
#############################################
    #############################################
    call reset
    call hide_all
    play music "audio/bgm/battle.mp3" loop
    scene forest background blur with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df3_2 = False
#############################################
    play music "audio/bgm/forest theme.mp3" loop
    scene forest background with dissolve
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    py happy "He escaped too."
    py normal "Then let's keep moving."
    show pychan at right
    nara "Not even a little break? I'm starting to want to escape too..."
    nara "When we finally figure out what TAP is, just what are we going to do with it?"
    nara "And why are the Prologue Punks around here?"
    py "It's another split, which way should we go?"
    call hide_all
    menu df3_2choice:
        "Forward!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call df4
        "Right!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call bdf_4
