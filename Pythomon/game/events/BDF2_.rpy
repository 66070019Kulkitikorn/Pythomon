label bdf_2:
    scene dark forest background with dissolve
    "Maybe I took the wrong turn but this section of the forest is oddly hostile."
    play music "audio/bgm/black forest theme.mp3" loop
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    py scared "Friendly Warning: Just now, we might've entered the danger zone."
    py ahhh "If we go any deeper we might never come out."
    py "It's still not too late to perform a strategic retreat-"
    show pychan at right
    nara "But it was a little too late. The malaria-inflicting monster has already emerged."
    call hide_all
    show mosquito with dissolve
    pause 2.0
    call hide_all
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    mc lookatme "Don't worry, I've dealt with these every night."
    py jeez "Where do you think we are? You can't just swat them with your hands!"
    show pychan at right
    mc closeeye "Fine, time to commit then."
    hide mosquito
    #############################################
    $ bdf_2 = True
    $ opp_mon_hp = 550
    $ opp_skill_position1 = ["Whine", "Pierce", "Suck"]
    $ opp_skill_dmg_position1 = [150, 250, 250]
    $ oppmonster1 = "Mosquito"
#############################################
    #############################################
    call reset
    call hide_all
    play music "audio/bgm/battle.mp3" loop
    scene forest background blur with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ bdf_2 = False
#############################################
    play music "audio/bgm/black forest theme.mp3" loop
    scene dark forest background with dissolve
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    mc "While our pythomon was combat locking the boss, I'm already full of bug bites from the little ones..."
    py "Now you see? Well, I'll leave the choice to you. Do you wanna go back or push deeper."
    call hide_all
    menu bdf_choice:
        "Left!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call df3_2
        "Forward!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call bdf_3
