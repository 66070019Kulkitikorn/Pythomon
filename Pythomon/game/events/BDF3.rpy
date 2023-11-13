label bdf_3:
    scene dark forest background with dissolve
    "I decide to keep pushing. But the further I push, the darker it becomes."
    play music "audio/bgm/black forest theme.mp3" loop
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    py scared "You really don't wanna go back?"
    py "If we go any deeper, I don't think you'll get the choice anymore."
    py ahhh "It will only get more and more dangerous from here, it's still not too late."
    hide bluepy 
    hide pychan 
    show scorpion with dissolve
    pause 2.0
    "Suddenly, huge stinger pops out of the bush and points straight at me."
    call hide_all
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    mc "Let's leave the decision-making for after I'm done committing it."
    py scared "Pray that lady luck is on your side, scorpions pack some deadly punches."
    hide scorpion
    #############################################
    $ bdf_3 = True
    $ opp_mon_hp = 600
    $ opp_skill_position1 = ["Claw", "Tail", "Raise"]
    $ opp_skill_dmg_position1 = [200, 450, 0]
    $ oppmonster1 = "Scorpion"
#############################################
    call reset
    call hide_all
    play music "audio/bgm/battle.mp3" loop
    scene forest background blur with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ bdf_3 = False
#############################################
    scene dark forest background with dissolve
    play music "audio/bgm/black forest theme.mp3" loop
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    mc "It might've packed some punches but it couldn't take much either."
    py "Don't get so cocky just because you're lucky..."
    py "I don't think luck alone will be enough after this. Well, have you made your choice?"
    call hide_all
    menu bdf3_choice:
        "Left!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call df4
        "Forward!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call bdf_4
