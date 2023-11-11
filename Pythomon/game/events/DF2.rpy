label df2:
    "We make some more progress and this time..."
    # pl1 = Prologue Punk 1
    pl1 "Another LAB:MEM? I guess another win for me, then."
    py "Grunt talk. So you're from Project Prologue."
    "Well, let's use this guy to cheer up from the ant fight."
    pl1 "We, Project Prologue, will put an end to your stupid research!"
    pl1 "Now, I'll get rid of this labdog, first!"
    mc "It's called a lapdog... And I'll show you which one of us is it."
    py "From our intel, these "Prologue Punks" have high bounty on LAB:MEM."
    mc "For the money, huh? I can dig it."
    py "Don't sympathize with them!"
    mc "Yeah, yeah. Whatever, just watch."
    py "Alright, let's commit!"
    #############################################
    $ df2 = True
    $ opp_mon_hp = 650
    $ opp_skill_position1 = ["Dash", "Dogfight", "Chase"]
    $ opp_skill_dmg_position1 = [250, 99, 0]
    $ oppmonster1 = "Dragonfly"
#############################################
    call reset
    call hide_all
    scene black with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df2 = False
#############################################
    py "Wow, he retreated even faster than his dragonfly."
    mc "Do we have to chase him?"
    py "No need, I already collected his dragonfly's DNA."
    py "Now which way should we go next?"
    menu df2_select2:
        "Left!":
            call df0_fight
        "Forward!":
            call df0_fight
        "Right!":
            call df0_fight

