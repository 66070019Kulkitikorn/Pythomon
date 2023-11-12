label df3_1:
    #mc = yuki py = pychan
    scene forest background with dissolve
    "Lemon told us to go straight ahead but I wanted to check out the left wing, and so..."
    play music "audio/bgm/stickbug theme.mp3" loop
    show stickbug with dissolve
    pause 2
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    mc nervous "Oh, man. Hiyajou's gonna like this one."
    py dotdotdot "It doesn't seem to be registered in the database yet, this is a new one."
    py normal "By the way, did you say something about Hiyajou?"
    show pychan at right
    nara "I think I remember seeing Hiyajou laughing at one of these."
    py "Whatever it is, let's stick to the usuals."
    show pychan at right
    mc lookatme "Committing."
    ##The legendary stickbug##
#############################################
    $ df3_1 = True
    $ opp_mon_hp = 1
    $ opp_skill_position1 = ["Kick", "Stomp", "Sway"]
    $ opp_skill_dmg_position1 = [1, 1, 0]
    $ oppmonster1 = "Stick Bug"
#############################################
    call reset
    call hide_all
    play music "audio/bgm/stickbug theme.mp3" loop
    scene forest background blur with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df3_1 = False
#############################################
    play music "audio/bgm/forest theme.mp3" loop
    scene forest background with dissolve
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    py "For something so rare, it sure was weak. I had some moves, though."
    py "Now we could say we're ahead of Project Prologue because we have the data on this."
    show pychan at right
    "I don't think being ahead with this one will mean much..."
    call hide_all
    #choice
    menu choice31:
        "Right!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call df4

