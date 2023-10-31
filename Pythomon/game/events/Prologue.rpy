
label prologue:
    #เขีนนdialogueตรงนี้
    scene bg black
    centered "pine apple pizza is good"
    Hiyajou "สวัสดี Labmem:011"

#   #Insert name here!
    Hiyajou "So... What's your name?"
    $ povname = renpy.input("What's your name?", length = 15)
    mc angry "uh ok"
    mc lookatme "Can i leave?"

    #เลือกตัวละคร
    menu select_mon:
        Hiyajou "Select one monster"
        "Fox":
            $ yourmonster = "Fox"
            $ your_max_full = 900
            $ skill_position1 = ["Pounce", "Bite", "Trick"]
            $ skill_dmg_position1 = [200, 300, 100]
            $ Fox = True
        "Dophin":
            $ yourmonster = "Dophin"
            $ your_max_full = 850
            $ skill_position1 = ["Leap", "Flipper", "Dive"]
            $ skill_dmg_position1 = [200, 300, 0]
            $ Dophin = True
        "Mantis":
            $ yourmonster = "Mantis"
            $ your_max_full = 180
            $ skill_position1 = ["Sickles", "Grip", "Guillotine"]
            $ skill_dmg_position1 = [500, 500, 999]
            $ Mantis = True
    image pythomon1 = ConditionSwitch("Fox", "pythomon_yours/fox yours.png", "Dophin", "pythomon_yours/dophin yours.png", "Mantis", "pythomon_yours/mantis yours.png")
    $ mon1 = True
    $ event_prolog = True
    ##################################
#############################################
    $ opp_mon1 = True
    $ opp_mon_hp = 500
    $ opp_skill_position1 = ["Peck", "Kick", "Flap"]
    $ opp_skill_dmg_position1 = [95, 99, 0]
    $ oppmonster1 = "Dodo"
#############################################
    call reset
    hide Professor Hiyajou nice with dissolve
    call battle_loop
    hide pythomon1 with dissolve
    $ opp_mon1 = False
    "here some another test battle !"
#############################################
#     $ opp_mon2 = True
#     $ opp_mon_hp = 200
#     $ opp_skill_position1 = ["Battle fang", "Strike", "Far-sighted focus"]
#     $ opp_skill_dmg_position1 = [45, 60, "Far-sighted focus"]
#     $ oppmonster1 = "Cat"
# #############################################
#     call reset
#     call battle_loop
    $ opp_mon1 = False
    "That the end of test what do you think?"
