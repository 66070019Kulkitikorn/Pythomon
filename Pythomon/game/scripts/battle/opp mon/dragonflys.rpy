label dragonfly:
    #["Dash", "Dogfight", "Chase"]
    if skill_di_opp == "Dash":
        if con == "win":
            play audio "Attack3.ogg"
            show oppythomon at farleft with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ your_hp -= dmg_opp
            "[dmg_opp] Damage!"
        else:
            play audio "Attack3.ogg"
            show oppythomon at farleft with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ dmg += 50
            $ your_hp -= dmg_opp
            "[dmg_opp] Damage! High damage on draw!"
    elif skill_di_opp == "Dogfight":
        if con == "win":
            play audio "Attack3.ogg"
            show oppythomon at farleft with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ your_hp -= dmg_opp
            "[dmg_opp] Damage!"
        else:
            play audio "Attack3.ogg"
            show oppythomon at farleft with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ dmg += 50
            $ your_hp -= dmg_opp
            "[dmg_opp] Damage! High damage on draw!"
    elif skill_di_opp == "Chase":
        play audio "Flash2.ogg"
        show oppythomon at farleft with pixellate
        $ opp_cri = 3
        "Dragonfly raise critical hit rate to 1/3!"
return