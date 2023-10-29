# label battle_loop:
#     $ current_hp = [0, 0, 0]
#     $ current_hp[0] = mon1_hp
#     $ current_hp[1] = mon2_hp
#     $ current_hp[2] = mon3_hp
#     $ change_back = False
#     $ skill_position = []
#     $ skill_dmg_position = []
#     $ opp_skill_position = opp_skill_position1
#     $ opp_skill_dmg_position = opp_skill_dmg_position1
#     Hiyajou "What"
#     define mp = 100
#     while True:
#         # your turn
#         ####################################################
#         call change_mon 
#         call yourmon_turn
#         call cri_chance_you
#         call yoursmotion_move
#         show pythomon1 at farright with move
#         "[yourmonster] used [skill_di]!"
#         $ mon = yourmonster
#         call skill_buff_debuff
#         $ mon_hp -= dmg
#         if dmg != 0:
#             show opppythomon at right with hpunch
#         else:
#             show pythomon1 at left with pixellate
#         show pythomon1 at left with move
#         if cri_success == True:
#             "A CRITICAL HIT!"
#             $ cri_success = False
#         #opp dies
#         ####################################################
#         if mon_hp <= 0 and opp_mon2 == False and opp_mon3 == True:
#             $ opp_mon3 = False
#         if mon_hp <= 0 and (opp_mon2 == False or opp_mon3 == False):
#             hide opppythomon with dissolve
#             "[oppmonster] faint!"
#             "You win!"
#             hide screen hp_bars_1v1
#             return
#         if mon_hp <= 0 :#and (opp_mon2 = True or opp_mon3 = True)
#             "[oppmonster] faint!"
#             $ opp_mon1 = False
#             if opp_mon1 == False and oppmonster == oppmonster2:
#                 $ opp_mon2 = False
#             if opp_mon2 == True:
#                 $ mon_hp = opp_mon2_hp
#                 $ oppmonster = oppmonster2
#                 $ opp_skill_position = opp_skill_position2
#                 $ opp_skill_dmg_position = opp_skill_dmg_position2
#                 "I sent [oppmonster]"
#             elif opp_mon3 == True:
#                 $ mon_hp = opp_mon3_hp
#                 $ oppmonster = oppmonster3
#                 $ opp_skill_position = opp_skill_position3
#                 $ opp_skill_dmg_position = opp_skill_dmg_position3
#                 "I sent [oppmonster]"
#         #opp turn
#         ####################################################
#         call oppmon_turn
#         call cri_chance_opp
#         show opppythomon at farleft with move
#         "[oppmonster] used [skill_di]!"
#         $ mon = oppmonster
#         call skill_buff_debuff
#         $ your_hp -= dmg
#         if dmg != 0:
#             show pythomon1 at left with hpunch
#         else:
#             show opppythomon at right with pixellate
#         show opppythomon at right with move
#         if cri_success == True:
#             "A CRITICAL HIT!"
#             $ cri_success = False
#         "HP [mon_hp] left!"
#         #You dies
#         ####################################################
#         if your_hp <= 0 and yourmonster == yourmonster1:
#             $ mon1 = False
#         elif your_hp <= 0 and yourmonster == yourmonster2:
#             $ mon2 = False
#         elif your_hp <= 0 and yourmonster == yourmonster3:
#             $ mon3 = False
#         if your_hp <= 0 and mon1 == False and mon2 == False and mon3 == False:
#             hide opppythomon with dissolve
#             "GAME OVER!"
#             $ renpy.quit()
#     # hide screen hp_bars_1v1
#     return
# # return

# #yourskill!
# label yourmon_turn:
#     menu player_attack_choice:
#         "What [yourmonster] do?"
#         "[skill_position[0]]" if mp > 0:
#             $ dmg = skill_dmg_position[0]
#             $ skill_di = skill_position[0]
#         "[skill_position[1]]" if mp > 0:
#             $ dmg = skill_dmg_position[1]
#             $ skill_di = skill_position[1]
#         "[skill_position[2]]" if mp > 0:
#             $ dmg = skill_dmg_position[2]
#             $ skill_di = skill_position[2]
#         "[skill_position[3]]" if mp > 0:
#             $ dmg = skill_dmg_position[3]
#             $ skill_di = skill_position[3]
#         "Change Pythomon" if mon2 == True or mon3 == True:
#             jump change_mon
#     return
    
# #change pythomon!
# label change_mon:
#     if change_back == False:
#         menu change_mon_choice:
#             "Select your Pythomon!"
#             "[yourmonster1]" if mon1 == True:
#                 $ yourmonster = yourmonster1
#                 $ skill_position = skill_position1.copy()
#                 $ skill_dmg_position = skill_dmg_position1.copy()
#                 $ your_max_hp = mon1_hp
#                 $ your_hp = your_max_hp
#                 $ your_hp = current_hp[0]
#                 show screen hp_bars_1v1
#                 $ change_back = True
#                 hide pythomon2
#                 hide pythomon3
#                 call your_stand
#                 call opp_stand
#                 call yourmon_turn
#             "[yourmonster2]" if mon2 == True:
#                 $ yourmonster = yourmonster2
#                 $ skill_position = skill_position2.copy()
#                 $ skill_dmg_position = skill_dmg_position2.copy()
#                 $ your_max_hp = mon2_hp
#                 $ your_hp = your_max_hp
#                 $ your_hp = current_hp[1]
#                 show screen hp_bars_1v1
#                 $ change_back = True
#                 call your_stand
#                 call opp_stand
#                 call yourmon_turn
#             "[yourmonster3]" if mon3 == True:
#                 $ yourmonster = yourmonster3
#                 $ skill_position = skill_position3.copy()
#                 $ skill_dmg_position = skill_dmg_position3.copy()
#                 $ your_max_hp = mon3_hp
#                 $ your_hp = your_max_hp
#                 $ your_hp = current_hp[2]
#                 show screen hp_bars_1v1
#                 $ change_back = True
#                 call your_stand
#                 call opp_stand
#                 call yourmon_turn
#             "back" if change_back == True:
#                 call yourmon_turn

# #Critical chance start from 1/10
# label cri_chance_you:
#     $ number = renpy.random.randint(1, your_cri)
#     if number == 1:
#         $ dmg = dmg * 2
#         $ cri_success = True
#     return

# label cri_chance_opp:
#     $ number = renpy.random.randint(1, opp_cri)
#     if number == 1:
#         $ dmg = dmg * 2
#         $ cri_success = True
#     return

# #opp turn!
# label oppmon_turn:
#     $ number = renpy.random.randint(1, 4)
#     if number == 1:
#         $ dmg = opp_skill_dmg_position[0]
#         $ skill_di = opp_skill_position[0]
#     elif number == 2:
#         $ dmg = opp_skill_dmg_position[1]
#         $ skill_di = opp_skill_position[1]
#     elif number == 3:
#         $ dmg = opp_skill_dmg_position[2]
#         $ skill_di = opp_skill_position[2]
#     elif number == 4:
#         $ dmg = opp_skill_dmg_position[3]
#         $ skill_di = opp_skill_position[3]
#     return

label battle_loop:
    while True:
        show pythomon1 at left
        show oppythomon at right
        show screen hp_bars_1v1
        call choose_skill_player
        call choose_skill_opp
        show your_pick at left with dissolve
        show opp_pick at right with dissolve
        pause 1
        hide your_pick with dissolve
        hide opp_pick with dissolve
        # hide opp_pick with dissolve
        call rock_paper_cissors_check
        if mon_hp <= 0:
            hide oppythomon with dissolve
            "You Win!"
            hide screen hp_bars_1v1
            return
        elif your_hp <= 0:
            hide pythomon1 with dissolve
            "You Lose :("
            hide screen hp_bars_1v1
            $ renpy.quit()
        $ your_turn = False
        $ opp_turn = False
    return

label choose_skill_player:
    menu player_attack_choice:
        "What [yourmonster] do?"
        "[skill_position[0]]":
            $ dmg = skill_dmg_position[0]
            $ skill_di = skill_position[0]
            $ yours = "Scissors"
        "[skill_position[1]]":
            $ dmg = skill_dmg_position[1]
            $ skill_di = skill_position[1]
            $ yours = "Rock"
        "[skill_position[2]]":
            $ skill_di = skill_position[2]
            $ yours = "Paper"
    return

label choose_skill_opp:
    $ number = renpy.random.randint(1, 3)
    if number == 1:
        $ dmg_opp = opp_skill_dmg_position[0]
        $ skill_di_opp = opp_skill_position[0]
        $ opp = "Scissors"
    elif number == 2:
        $ dmg_opp = opp_skill_dmg_position[1]
        $ skill_di_opp = opp_skill_position[1]
        $ opp = "Rock"
    elif number == 3:
        $ skill_di_opp = opp_skill_position[2]
        $ opp = "Paper"
    return

default rps_beats_attack = [('Rock', 'Scissors'), ('Scissors', 'Paper')]
default rps_beats_buff = [('Paper', 'Rock')]
default rps_draw_buff = [('Paper', 'Paper')]

label rock_paper_cissors_check:
    if (yours, opp) in rps_beats_attack:
        centered "[yourmonster] WIN!"
        show pythomon1 at farright with move
        "[yourmonster] used [skill_di]!"
        show pythomon1 at farright with hpunch
        $ mon_hp -= dmg
        show pythomon1 at left
#########################################################
#########################################################
    elif (yours, opp) in rps_draw_buff:
        centered "DRAW!"
#
        show pythomon1 at farright with move
        "[yourmonster] used [skill_di]!"
        show pythomon1 at farright with pixellate
        $ your_turn = True
        call skill_buff_debuff
        show pythomon1 at left
#
        show oppythomon at farleft with move
        "[oppmonster] used [skill_di_opp]!"
        show oppythomon at farleft with pixellate
        $ opp_turn = True
        call skill_buff_debuff
        show oppythomon at right
#######################################################
#######################################################
    elif (opp, yours) in rps_beats_attack:
        centered "[oppmonster] WIN!"
        show oppythomon at farleft with move
        "[oppmonster] used [skill_di_opp]!"
        show oppythomon at farleft with hpunch
        $ your_hp -= dmg_opp
        show oppythomon at right
#######################################################
#######################################################
    elif (opp, yours) in rps_beats_buff:
        centered "[oppmonster] WIN!"
        show oppythomon at farleft with move
        "[oppmonster] used [skill_di_opp]!"
        show oppythomon at farleft with pixellate
        $ opp_turn = True
        call skill_buff_debuff
        show oppythomon at right
#######################################################
#######################################################
    elif (yours, opp) in rps_beats_buff:
        centered "[yourmonster] WIN!"
        show pythomon1 at farright with move
        "[yourmonster] used [skill_di]!"
        show pythomon1 at farright with pixellate
        $ your_turn = True
        call skill_buff_debuff
        show pythomon1 at left
#######################################################
#######################################################
    else :
        centered "DRAW!"
#
        show pythomon1 at farright with move
        "[yourmonster] used [skill_di]!"
        show pythomon1 at farright with hpunch
        $ mon_hp -= dmg
        show pythomon1 at left
#
        show oppythomon at farleft with move
        "[oppmonster] used [skill_di_opp]!"
        show oppythomon at farleft with hpunch
        $ your_hp -= dmg_opp
        show oppythomon at right
#######################################################
    return

