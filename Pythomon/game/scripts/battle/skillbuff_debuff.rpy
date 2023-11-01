label skill_buff_debuff:
    if your_turn == True:
        call your_skill
    elif opp_turn ==  True:
        call opp_skill
return

label your_skill:
    if skill_di == "Pounce":
        show pythomon1 at farright with hpunch
        $ mon_hp -= dmg
        "[dmg] Damage!"
    elif skill_di == "Bite":
        if con == "win":
            show pythomon1 at farright with hpunch
            $ mon_hp -= dmg
            "[dmg] Damage!"
        else:
            show pythomon1 at farright with hpunch
            $ dmg += 100
            $ mon_hp -= dmg
            "[dmg] Damage! High damage on draw!"
    elif skill_di == "Trick":
        if con == "win":
            show pythomon1 at farright with hpunch
            $ mon_hp -= dmg
            "[dmg] Damage!"
        else:
            show pythomon1 at farright with hpunch
            $ dmg += 200
            $ mon_hp -= dmg
            "[dmg] Damage! High damage on draw!"
##########################################################
    elif skill_di == "Sickles":
        if con == "draws":
            show pythomon1 at farright with hpunch
            $ dmg = 99 
            $ mon_hp -= dmg
            "[dmg] Damage! Low damage on draw...."
        else:
            show pythomon1 at farright with hpunch
            $ mon_hp -= dmg
            "[dmg] Damage!"
    elif skill_di == "Grip":
        if con == "draws":
            show pythomon1 at farright with hpunch
            $ dmg = 199
            $ mon_hp -= dmg
            "[dmg] Damage! Low damage on draw...."
        else:
            show pythomon1 at farright with hpunch
            $ mon_hp -= dmg
            "[dmg] Damage!"
    elif skill_di == "Guillotine":
        if con == "draws":
            show pythomon1 at farright with hpunch
            $ your_hp -= 1000
            "It's Draw!! You take 1000 Damage!"
            "XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
        else:
            show pythomon1 at farright with hpunch
            $ mon_hp -= dmg
            "[dmg] Damage!"
##########################################################
    elif skill_di == "Leap":
        if dive == True:
            show pythomon1 at farright with hpunch
            $ dmg += 150
            $ mon_hp -= dmg
            "[dmg] Damage!"
        else:
            show pythomon1 at farright with hpunch
            $ mon_hp -= dmg
            "[dmg] Damage!"
    elif skill_di == "Flipper":
        if dive == True:
            show pythomon1 at farright with hpunch
            $ dmg += 150
            $ mon_hp -= dmg
            "[dmg] Damage!"
        else:
            show pythomon1 at farright with hpunch
            $ mon_hp -= dmg
            "[dmg] Damage!"
    elif skill_di == "Dive":
        show pythomon1 at farright with pixellate
        $ dive = True
        "Dolphin start to dive!! Raises ATK, loses buff after taking DMG."
return

label opp_skill:
    if con == "lose" or con == "draws":
        $ dive = False
    if oppmonster1 == "Dodo":
        call dodo
return

label dodo:
    if skill_di_opp == "Peck":
        show oppythomon at farleft with hpunch
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Kick":
        show oppythomon at farleft with hpunch
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Flap":
        show oppythomon at farleft with pixellate
        $ opp_skill_dmg_position[0] = opp_skill_dmg_position[0] + 50
        $ opp_skill_dmg_position[1] = opp_skill_dmg_position[1] + 50
        "Dodo raise ATK!"
return