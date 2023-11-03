label dodo:
    if skill_di_opp == "Peck":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Kick":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Flap":
        play audio "Absorb2.ogg"
        show oppythomon at farleft with pixellate
        $ opp_skill_dmg_position[0] = opp_skill_dmg_position[0] + 50
        $ opp_skill_dmg_position[1] = opp_skill_dmg_position[1] + 50
        "Dodo raise ATK!"
return