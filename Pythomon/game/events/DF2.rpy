label df2:
    scene forest background with dissolve
    "We make some more progress and this time..."
    play music "audio/bgm/forest theme.mp3" loop
    # pl1 = Prologue Punk 1
    show keke1 with dissolve
    show yuukii at left with dissolve
    pl1 "Another LAB:MEM? I guess another win for me, then."
    # hide yuukii
    call hide_all
    show keke1
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py "Grunt talk. So you're from Project Prologue."
    py happy "Well, let's use this guy to cheer up from the ant fight."
    hide bluepy 
    hide pychan 
    pl1 "We, Project Prologue, will put an end to your stupid research!"
    pl1 "Now, I'll get rid of this labdog, first!"
    show keke1
    mc "It's called a lapdog... And I'll show you which one of us is it."
    call hide_all
    show keke1
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py "From our intel, these \"Prologue Punks\" have high bounty on LAB:MEM."
    show pychan at right
    mc nervous "For the money, huh? I can dig it."
    py dotdotdot "Don't sympathize with them!"
    show pychan at right
    mc lookatme "Yeah, yeah. Whatever, just watch."
    py happy "Alright, let's commit!"
    #############################################
    $ df2 = True
    $ opp_mon_hp = 650
    $ opp_skill_position1 = ["Dash", "Dogfight", "Chase"]
    $ opp_skill_dmg_position1 = [250, 99, 0]
    $ oppmonster1 = "Dragonfly"
#############################################
    call reset
    call hide_all
    play music "audio/bgm/battle.mp3" loop
    scene forest background blur with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df2 = False
#############################################
    play music "audio/bgm/forest theme.mp3" loop
    scene forest background with dissolve
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    py happy "Wow, he retreated even faster than his dragonfly."
    show pychan at right
    mc lookatme "Do we have to chase him?"
    py "No need, I already collected his dragonfly's DNA."
    py "Now which way should we go next?"
    call hide_all
    menu df2_select2:
        "Left!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call df3_1
        "Forward!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call df3_2
        "Right!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call bdf_3

