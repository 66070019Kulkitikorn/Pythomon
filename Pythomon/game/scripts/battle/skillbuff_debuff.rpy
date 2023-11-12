label skill_buff_debuff:
    if your_turn == True:
        call your_skill
    elif opp_turn ==  True:
        call opp_skill
return

label your_skill:
    if skill_di == "Pounce":
        play audio "Attack3.ogg"
        show pythomon1 at farright with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ mon_hp -= dmg
        "[dmg] Damage!"
    elif skill_di == "Bite":
        if con == "win":
            play audio "Attack3.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ mon_hp -= dmg
            "[dmg] Damage!"
        else:
            play audio "Attack3.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ dmg += 100
            $ mon_hp -= dmg
            "[dmg] Damage! High damage on draw!"
    elif skill_di == "Trick":
        if con == "win":
            play audio "Attack3.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ mon_hp -= dmg
            "[dmg] Damage!"
        else:
            play audio "Attack3.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ dmg += 300
            $ mon_hp -= dmg
            "[dmg] Damage! High damage on draw!"
##########################################################
    elif skill_di == "Sickles":
        if con == "draws":
            play audio "Flash2.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ dmg = 99 
            $ mon_hp -= dmg
            "[dmg] Damage! Low damage on draw...."
        else:
            play audio "Flash2.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ mon_hp -= dmg
            "[dmg] Damage!"
    elif skill_di == "Grip":
        if con == "draws":
            play audio "Flash2.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ dmg = 199
            $ mon_hp -= dmg
            "[dmg] Damage! Low damage on draw...."
        else:
            play audio "Flash2.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ mon_hp -= dmg
            "[dmg] Damage!"
    elif skill_di == "Guillotine":
        if con == "draws":
            play audio "Flash2.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ your_hp -= 1000
            "It's Draw!! You take 1000 Damage!"
            "XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
        else:
            play audio "Flash2.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ mon_hp -= dmg
            "[dmg] Damage!"
##########################################################
    elif skill_di == "Leap":
        if dive == True:
            play audio "Water1.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ dmg += 150
            $ mon_hp -= dmg
            "[dmg] Damage!"
        else:
            play audio "Water1.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ mon_hp -= dmg
            "[dmg] Damage!"
    elif skill_di == "Flipper":
        if dive == True:
            play audio "Water1.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ dmg += 150
            $ mon_hp -= dmg
            "[dmg] Damage!"
        else:
            play audio "Water1.ogg"
            show pythomon1 at farright with hpunch
            pause 0.3
            play audio "Damage3.ogg"
            $ mon_hp -= dmg
            "[dmg] Damage!"
    elif skill_di == "Dive":
        play audio "Water2.ogg"
        show pythomon1 at farright with pixellate
        $ dive = True
        "Dolphin start to dive!! Raises ATK, loses buff after taking DMG."
return

label opp_skill:
    if (con == "lose" or con == "draws") and dmg_opp > 0:
        $ dive = False
    if oppmonster1 == "Dodo":
        call dodo
    elif oppmonster1 == "Ant":
        call ant
    elif oppmonster1 == "Dragonfly":
        call dragonfly
    elif oppmonster1 == "Hercules Beetle":
        call herculesbeetle
    elif oppmonster1 == "Mosquito":
        call mosquito
    elif oppmonster1 == "Queen Bee":
        call queenbee
    elif oppmonster1 == "Scorpion":
        call scorpion
    elif oppmonster1 == "Stick Bug":
        call stickbug
    elif oppmonster1 == "Bee":
        call bee
    elif oppmonster1 == "True Sting":
        call truestring
return

#"Sting", "Bite", "Pheromone"
