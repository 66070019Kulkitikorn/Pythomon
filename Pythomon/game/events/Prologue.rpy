
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
        "Cat":
            $ yourmonster1 = "cat"
            $ skill_position1 = ["Trasure Sign \"Ying-Yang Orb", "Divine Arts \"Wind God Kick", "Sign I \"lDream Orb String", "Divine Spirit \"Fantasy Seal"]
            $ skill_dmg_position1 = [10, 10, 20, 1000]
            $ cat = True
        "dophin":
            $ yourmonster1 = "dophin"
            $ skill_position1 = ["Star Sign \"Meteoric Shower", "Light Sign \"Luminous Strike", "Comet \"Blazing Star", "Love Sign \"MasterSpark"]
            $ skill_dmg_position1 = [10, 10, 20, 1000]
            $ dophin = True
        "ant":
            $ yourmonster1 = "ant"
            $ skill_position1 = ["Esoterica \"Gray Thaumaturgy", "Sea Opening \"Moses's Miracle", "Miracle \"God's Wind", "Snake Sign \"Orochi of Ancient Times"]
            $ skill_dmg_position1 = [10, 10, 20, 1000]
            $ ant = True
    image pythomon1 = ConditionSwitch("cat", "pythomon_yours/cat yours.png", "dophin", "pythomon_yours/dophin yours.png", "ant", "pythomon_yours/ant yours.png")
    $ mon1 = True
    $ mon1_hp = 100
    $ event_prolog = True
    $ opp_mon1 = True
    $ mon_max_hp = 100
    $ mon_hp = mon_max_hp
    $ oppmonster = "Dodo"
    $ opp_skill_position1 = ["Tackle", "Pinch", "Hard tackle", "Dodo noise"]
    $ opp_skill_dmg_position1 = [10, 15, 20, 0]
    hide Professor Hiyajou nice with dissolve
    call battle_loop
    hide screen hp_bars_1v1