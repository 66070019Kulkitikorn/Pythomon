label df1:
    "We make our way through the forest until..."
    #An ant shows up
    py "An ant?"
    mc "Yeah, no jack. What do you think it was?"
    py "Let's fight it."
    mc "Wait, you just said it was an ant."
    py "Fight. It."
    mc "Oh, geez..."
    #############################################
    $ df1 = True
    $ opp_mon_hp = 888
    $ opp_skill_position1 = ["Sting", "Bite", "Pheromone"]
    $ opp_skill_dmg_position1 = [150, 222, 0]
    $ oppmonster1 = "Ant"
#############################################
    call reset
    call hide_all
    scene black with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df1 = False
#############################################
    mc "That one was definitely tougher than Lemon."
    mc "Anyway, not a fan of peace?"
    py "Since our intel was stolen by Project Prologue, it's best we accumulate some more data."
    py "Anyway, I recorded it's DNA. Let's keep going."
    "Not a hint of symphathy, huh. Had no idea LAB:MEMB was this cruel at work."
    menu df1_next:
        "Forward!":
            scene black with slowdisslove
            call df2
        # "Left!":
