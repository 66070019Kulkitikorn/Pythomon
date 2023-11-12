# #############################################
#     $ df5 = False
#     $ opp_mon_hp = 1000
#     $ opp_skill_position1 = ["Queen's Swarm", "Queen's Stinger", "Queen's Larvae"]
#     $ opp_skill_dmg_position1 = [300, 400, 0]
#     $ oppmonster1 = "Queen Bee"
# #############################################
#     $ df5 = False

label queenbee:
    if skill_di_opp == "Queen's Swarm":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Queen's Stinger":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Queen's Larvae":
        play audio "Heal2.ogg"
        show oppythomon at farleft with pixellate
        $ mon_hp += 250
        if mon_hp >= 1200:
            $ mon_hp = 1200
            "[oppmonster1] HP is already full."
        else:
            "[oppmonster1] Restores 250 HP!"
return