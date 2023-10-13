label battle_loop:
    $ current_hp = [0, 0, 0]
    $ current_hp[0] = mon1_hp
    $ current_hp[1] = mon2_hp
    $ current_hp[2] = mon3_hp
    $ change_back = False
    $ skill_position = []
    $ skill_dmg_position = []
    $ opp_skill_position = opp_skill_position1
    $ opp_skill_dmg_position = opp_skill_dmg_position1
    Hiyajou "What"
    define mp = 100
    while True:
        # your turn
        ####################################################
        call change_mon
        call yourmon_turn
        call cri_chance_you
        "[yourmonster] used [skill_di]!"
        $ mon = yourmonster
        call skill_buff_debuff
        $ mon_hp -= dmg
        if cri_success == True:
            "A CRITICAL HIT!"
            $ cri_success = False
        #opp dies
        ####################################################
        if mon_hp <= 0 and opp_mon2 == False and opp_mon3 == True:
            $ opp_mon3 = False
        if mon_hp <= 0 and (opp_mon2 == False or opp_mon3 == False):
            "[oppmonster] faint!"
            "You win!"
            hide screen hp_bars_1v1
            return
        if mon_hp <= 0 :#and (opp_mon2 = True or opp_mon3 = True)
            "[oppmonster] faint!"
            $ opp_mon1 = False
            if opp_mon1 == False and oppmonster == oppmonster2:
                $ opp_mon2 = False
            if opp_mon2 == True:
                $ mon_hp = opp_mon2_hp
                $ oppmonster = oppmonster2
                $ opp_skill_position = opp_skill_position2
                $ opp_skill_dmg_position = opp_skill_dmg_position2
                "I sent [oppmonster]"
            elif opp_mon3 == True:
                $ mon_hp = opp_mon3_hp
                $ oppmonster = oppmonster3
                $ opp_skill_position = opp_skill_position3
                $ opp_skill_dmg_position = opp_skill_dmg_position3
                "I sent [oppmonster]"
        #opp turn
        ####################################################
        call oppmon_turn
        call cri_chance_opp
        "[oppmonster] used [skill_di]!"
        $ mon = oppmonster
        call skill_buff_debuff
        $ your_hp -= dmg
        if cri_success == True:
            "A CRITICAL HIT!"
            $ cri_success = False
        "HP [mon_hp] left!"
        #You dies
        ####################################################
        if your_hp <= 0 and yourmonster == yourmonster1:
            $ mon1 = False
        elif your_hp <= 0 and yourmonster == yourmonster2:
            $ mon2 = False
        elif your_hp <= 0 and yourmonster == yourmonster3:
            $ mon3 = False
        if your_hp <= 0 and mon1 == False and mon2 == False and mon3 == False:
            "GAME OVER!"
            $ renpy.quit()
    # hide screen hp_bars_1v1
    return
# return

#yourskill!
label yourmon_turn:
    menu player_attack_choice:
        "What [yourmonster] do?"
        "[skill_position[0]]" if mp > 0:
            $ dmg = skill_dmg_position[0]
            $ skill_di = skill_position[0]
        "[skill_position[1]]" if mp > 0:
            $ dmg = skill_dmg_position[1]
            $ skill_di = skill_position[1]
        "[skill_position[2]]" if mp > 0:
            $ dmg = skill_dmg_position[2]
            $ skill_di = skill_position[2]
        "[skill_position[3]]" if mp > 0:
            $ dmg = skill_dmg_position[3]
            $ skill_di = skill_position[3]
        "Change Pythomon" if mon2 == True or mon3 == True:
            call change_mon
    return
    
#change pythomon!
label change_mon:
    if change_back == False:
        menu change_mon_choice:
            "Select your Pythomon!"
            "[yourmonster1]" if mon1 == True:
                $ yourmonster = yourmonster1
                $ skill_position = skill_position1.copy()
                $ skill_dmg_position = skill_dmg_position1.copy()
                $ your_max_hp = mon1_hp
                $ your_hp = your_max_hp
                $ your_hp = current_hp[0]
                show screen hp_bars_1v1
                $ change_back = True
                call yourmon_turn
            "[yourmonster2]" if mon2 == True:
                $ yourmonster = yourmonster3
                $ skill_position = skill_position2.copy()
                $ skill_dmg_position = skill_dmg_position2.copy()
                $ your_max_hp = mon2_hp
                $ your_hp = your_max_hp
                $ your_hp = current_hp[1]
                show screen hp_bars_1v1
                $ change_back = True
                call yourmon_turn
            "[yourmonster2]" if mon2 == True:
                $ yourmonster = yourmonster3
                $ skill_position = skill_position3.copy()
                $ skill_dmg_position = skill_dmg_position3.copy()
                $ your_max_hp = mon3_hp
                $ your_hp = your_max_hp
                $ your_hp = current_hp[2]
                show screen hp_bars_1v1
                $ change_back = True
                call yourmon_turn
            "back" if change_back == True:
                call yourmon_turn

#Critical chance start from 1/10
label cri_chance_you:
    $ number = renpy.random.randint(1, your_cri)
    if number == 1:
        $ dmg = dmg * 2
        $ cri_success = True
    return

label cri_chance_opp:
    $ number = renpy.random.randint(1, opp_cri)
    if number == 1:
        $ dmg = dmg * 2
        $ cri_success = True
    return

#opp turn!
label oppmon_turn:
    $ number = renpy.random.randint(1, 4)
    if number == 1:
        $ dmg = opp_skill_dmg_position[0]
        $ skill_di = opp_skill_position[0]
    elif number == 2:
        $ dmg = opp_skill_dmg_position[1]
        $ skill_di = opp_skill_position[1]
    elif number == 3:
        $ dmg = opp_skill_dmg_position[2]
        $ skill_di = opp_skill_position[2]
    elif number == 4:
        $ dmg = opp_skill_dmg_position[3]
        $ skill_di = opp_skill_position[3]
    return

