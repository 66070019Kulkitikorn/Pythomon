# #############################################
#     $ df3_1 = True
#     $ opp_mon_hp = 1
#     $ opp_skill_position1 = ["Kick", "Stomp", "Sway"]
#     $ opp_skill_dmg_position1 = [1, 1, 0]
#     $ oppmonster1 = "Stick Bug"
# #############################################
#     $ df3_1 = False

label stickbug:
    if skill_di_opp == "Kick":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Stomp":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[dmg_opp] Damage!"
    elif skill_di_opp == "Sway":
        play audio "Attack3.ogg"
        show oppythomon at farleft with hpunch
        pause 0.3
        play audio "Damage3.ogg"
        $ your_hp -= dmg_opp
        "[oppmonster1] does nothing!"
return