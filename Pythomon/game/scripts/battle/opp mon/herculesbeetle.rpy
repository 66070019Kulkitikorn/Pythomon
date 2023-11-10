# #############################################
#     $ df4 = False
#     $ opp_mon_hp = 1000
#     $ opp_skill_position1 = ["Rush", "Thrust", "Lift"]
#     $ opp_skill_dmg_position1 = [300, 400, 444]
#     $ oppmonster1 = "Hercules Beetle"
# #############################################
#     $ df4 = False

label herculesbeetle:
    if skill_di_opp == "Rush":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Thrust":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Lift":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
return