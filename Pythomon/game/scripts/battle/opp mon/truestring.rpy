# #############################################
#     $ bdf_5 = False
#     $ opp_mon_hp = 1500
#     $ opp_skill_position1 = ["Plague", "Purge", "Propagation"]
#     $ opp_skill_dmg_position1 = [150, 250, 0]
#     $ oppmonster1 = "True Sting"
# #############################################
#     $ bdf_5 = False

label truestring:
    if skill_di_opp == "Plague":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Purge":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Propagation":
        play audio "Heal2.ogg"
        show oppythomon at farleft with pixellate
        $ mon_hp += 200
        if mon_hp >= 1500:
            $ mon_hp = 1500
            "[oppmonster1] HP is already full."
        else:
            "[oppmonster1] Restores 200 HP!"
return