label skill_buff_debuff:
    if your_turn == True:
        call your_skill
    if opp_turn ==  True:
        call opp_skill
return

label your_skill:
    if skill_di == "Amazing Senses":
        $ skill_dmg_position[0] = skill_dmg_position[0] + 15
        "[skill_position[0]] Attack Increase!"
    elif skill_di == "Playfulness":
        $ your_hp += 45
        if your_hp >= your_max_hp:
            $ your_hp = your_max_hp
        "Dophin HP Increase!"
    elif skill_di == "Stealth Mastery":
        $ skill_dmg_position[1] = skill_dmg_position[1] + 15
        "[skill_position[1]] Attack Increase!"
    $ your_turn = False
return

label opp_skill:
    if skill_di_opp == "Wing Flap":
        $ mon_hp += 45
        if mon_hp >= mon_max_hp:
            $ mon_hp = mon_max_hp
        "Dodo HP Increase!"
    elif skill_di_opp == "Far-sighted focus":
        $ opp_skill_dmg_position[0] = opp_skill_dmg_position[0] + 15
        "[opp_skill_position[0]] Attack Increase!"
    $ opp_turn = False
return