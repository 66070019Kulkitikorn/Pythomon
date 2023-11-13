
#Critical chance start from 1/10
label cri_chance_you:
    $ number = renpy.random.randint(1, your_cri)
    if number == 1:
        $ dmg = dmg * 2
        $ cri_success_you = True
    return

label cri_chance_opp:
    $ number = renpy.random.randint(1, opp_cri)
    if number == 1:
        $ dmg_opp = dmg_opp * 2
        $ cri_success_mon = True
    return


label battle_loop:
    while mon_hp > 0:
        call hide_all
        $ cri_success_you = False
        $ cri_success_mon = False
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
        call cri_chance_you
        call cri_chance_opp
        call rock_paper_cissors_check
        $ your_turn = False
        $ opp_turn = False
    return

label choose_skill_player:
    menu player_attack_choice:
        "What [yourmonster] do?"
        "{color=#ff0000}[skill_position[0]]{/color}":
            $ dmg = skill_dmg_position[0]
            $ skill_di = skill_position[0]
            $ yours = "Scissors"
        "{color=#00aeff}[skill_position[1]]{/color}":
            $ dmg = skill_dmg_position[1]
            $ skill_di = skill_position[1]
            $ yours = "Rock"
        "{color=#00ff55}[skill_position[2]]{/color}":
            $ dmg = skill_dmg_position[2]
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
        $ dmg_opp = opp_skill_dmg_position[1]
        $ skill_di_opp = opp_skill_position[2]
        $ opp = "Paper"
    return

default rps_beats_attack = [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')]
default rps_draw = [('Paper', 'Paper'), ('Rock', 'Rock'), ('Scissors', 'Scissors')]

label rock_paper_cissors_check:
    if (yours, opp) in rps_beats_attack:
        centered "{=stroke_green}{size=+30}[yourmonster] WIN!{/size}{/stroke_green}"
        show pythomon1 at farright with move
        "[yourmonster] used [skill_di]!"
        $ con = "win"
        call your_skill
        if cri_success_you == True and dmg > 0:
            "A critical hit!"
        show pythomon1 at left with move
        call win_cont
#########################################################
#########################################################
    elif (yours, opp) in rps_draw:
        centered "{=stroke_yellow}{size=+30}DRAW!{/size}{/stroke_yellow}"
        $ con = "draws"
#
        show pythomon1 at farright with move
        "[yourmonster] used [skill_di]!"
        # show pythomon1 at farright with pixellate
        $ your_turn = True
        call your_skill
        if cri_success_you == True and dmg > 0:
            "A critical hit!"
        show pythomon1 at left with move
        call win_cont
        if mon_hp > 0:
            show oppythomon at farleft with move
            "[oppmonster] used [skill_di_opp]!"
        # show oppythomon at farleft with pixellate
            $ opp_turn = True
            call opp_skill
            if cri_success_mon == True and dmg_opp > 0:
                "A critical hit!"
            show oppythomon at right with move
            call win_cont
#######################################################
#######################################################
    elif (opp, yours) in rps_beats_attack:
        $ con = "lose"
        centered "{=stroke_red}{size=+30}[oppmonster] WIN!{/size}{/stroke_red}"
        show oppythomon at farleft with move
        "[oppmonster] used [skill_di_opp]!"
        # show oppythomon at farleft with pixellate
        $ opp_turn = True
        call opp_skill
        if cri_success_mon == True and dmg_opp > 0:
            "A critical hit!"
        show oppythomon at right with move
        call win_cont
    return


