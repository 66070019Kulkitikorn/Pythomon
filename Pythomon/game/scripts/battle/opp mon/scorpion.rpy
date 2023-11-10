# #############################################
#     $ bdf_3 = False
#     $ opp_mon_hp = 600
#     $ opp_skill_position1 = ["Claw", "Tail", "Raise"]
#     $ opp_skill_dmg_position1 = [200, 450, 0]
#     $ oppmonster1 = "Scorpion"
# #############################################
#     $ bdf_3 = False

label scorpion:
    if skill_di_opp == "Claw":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Tail":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Raise":
        play audio "Absorb2.ogg"
        show oppythomon at farleft with pixellate
        $ opp_cri = 3
        "[oppmonster1] raise CRIT Rate!"
return