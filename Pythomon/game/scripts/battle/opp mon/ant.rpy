label ant:
    if skill_di_opp == "Sting":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Bite":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Pheromone":
        play audio "Heal2.ogg"
        show oppythomon at farleft with pixellate
        $ mon_hp += 100
        if mon_hp >= 555:
            $ mon_hp = 555
            "[oppmonster1] HP is already full."
        else:
            "[oppmonster1] Restores 100 HP!"
return