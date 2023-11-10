# #############################################
#     $ df3_2 = True
#     $ opp_mon_hp = 600
#     $ opp_skill_position1 = ["Sting", "Stinger", "Work"]
#     $ opp_skill_dmg_position1 = [99, 300, 0]
#     $ oppmonster1 = "Bee"
# #############################################
#     $ df3_2 = False

label bee:
    if skill_di_opp == "Sting":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Stinger":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Work":
        play audio "Heal2.ogg"
        show oppythomon at farleft with pixellate
        if mon_hp >= 600:
            $ mon_hp == 600
            "[oppmonster1] HP is already full."
        else:
            $ mon_hp += 100
            "[oppmonster1] Restores 100 HP!"
return