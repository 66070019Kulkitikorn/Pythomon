# #############################################
#     $ bdf_2 = False
#     $ opp_mon_hp = 550
#     $ opp_skill_position1 = ["Whine", "Pierce", "Suck"]
#     $ opp_skill_dmg_position1 = [150, 350, 250]
#     $ oppmonster1 = "Mosquito"
# #############################################
#     $ bdf_2 = False

label mosquito:
    if skill_di_opp == "Whine":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Pierce":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Suck":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[oppmonster1] Damage! and Restores 200 HP!"
        play audio "Heal2.ogg"
        $ mon_hp += 200
        if mon_hp >= 550:
            $ mon_hp = 550
            "[oppmonster1] HP is already full."
        else:
            "[oppmonster1] Restores 200 HP!"
return