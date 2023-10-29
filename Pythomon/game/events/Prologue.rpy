
label prologue:
    #เขีนนdialogueตรงนี้
    scene black
    centered "pine apple pizza is good"
    Hiyajou " "

#   #Insert name here!
    Hiyajou "So... What's your name?"
    $ povname = renpy.input("What's your name?", length = 15)

    #เลือกตัวละคร
    menu select_mon:
        Hiyajou "Select one monster"
        "Fox":
            $ yourmonster = "Fox"
            $ your_max_full = 225
            $ skill_position1 = ["Scratch", "Bite", "Amazing Senses"]
            $ skill_dmg_position1 = [50, 25, "Amazing Senses"]
            $ Fox = True
        "Dophin":
            $ yourmonster = "Dophin"
            $ your_max_full = 275
            $ skill_position1 = ["Takle", "Strike", "Playfulness"]
            $ skill_dmg_position1 = [15, 45, "Playfulness"]
            $ Dophin = True
        "Mantis":
            $ yourmonster = "Mantis"
            $ your_max_full = 180
            $ skill_position1 = ["Chop", "Slash", "Stealth Mastery"]
            $ skill_dmg_position1 = [10, 60, "Stealth Mastery"]
            $ Mantis = True
    image pythomon1 = ConditionSwitch("Fox", "pythomon_yours/fox yours.png", "Dophin", "pythomon_yours/dophin yours.png", "Mantis", "pythomon_yours/mantis yours.png")
    $ mon1 = True
    $ event_prolog = True
    $ opp_mon1 = True
    ##################################
#############################################
    $ opp_mon_hp = 200
    $ opp_skill_position1 = ["Tackle", "Pinch", "Wing Flap"]
    $ opp_skill_dmg_position1 = [30, 45, "Wing Flap"]
    $ oppmonster1 = "Dodo"
#############################################
    call reset
    hide Professor Hiyajou nice with dissolve
    call battle_loop
    hide pythomon1 with dissolve
    $ opp_mon1 = False
    "here some another test battle !"
#############################################
    $ opp_mon2 = True
    $ opp_mon_hp = 200
    $ opp_skill_position1 = ["Battle fang", "Strike", "Far-sighted focus"]
    $ opp_skill_dmg_position1 = [45, 60, "Far-sighted focus"]
    $ oppmonster1 = "Cat"
#############################################
    call reset
    call battle_loop
    "That the end of test what do you think?"
