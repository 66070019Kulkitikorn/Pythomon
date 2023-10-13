
# $ yourmonster = empty
# define show_score = False
# define show_mon = False
# define mon_max_hp = 100
# define mon_hpp = mon_max_hp
# define your_max_hp = 100
# define your_hp = your_max_hp
label start:
    scene bg room
    show Professor Hiyajou
    Hiyajou "Welcome LABMEM:011"
    Hiyajou "To the Simulation World!"
    Hiyajou "You can call me Professor Hiyajou"
    show Professor Hiyajou confused
    Hiyajou "Wait what the fuc"
    show Professor Hiyajou nice
    Hiyajou "I didn't understand how to make combat system good i guess?"

#   #Insert name here!
    Hiyajou "So... What's your name?"
    $ povname = renpy.input("What's your name?", length = 15)

    MC "Uh... My name is [povname]"
    Hiyajou "I see....[povname]. You ARE the choosen one!!!"
    Hiyajou "Thank for testing i guess?"
    Hiyajou "oh this is test so..."
    menu select_mon:
        Hiyajou "Select one monster"
        "Mon1":
            $ yourmonster1 = "Mon1"
            $ skill_position1 = ["Trasure Sign \"Ying-Yang Orb", "Divine Arts \"Wind God Kick", "Sign I \"lDream Orb String", "Divine Spirit \"Fantasy Seal"]
            $ skill_dmg_position1 = [10, 10, 20, 1000]
        "Mon2":
            $ yourmonster1 = "Mon2"
            $ skill_position1 = ["Star Sign \"Meteoric Shower", "Light Sign \"Luminous Strike", "Comet \"Blazing Star", "Love Sign \"MasterSpark"]
            $ skill_dmg_position1 = [10, 10, 20, 1000]
        "Mon3":
            $ yourmonster1 = "Mon3"
            $ skill_position1 = ["Esoterica \"Gray Thaumaturgy", "Sea Opening \"Moses's Miracle", "Miracle \"God's Wind", "Snake Sign \"Orochi of Ancient Times"]
            $ skill_dmg_position1 = [10, 10, 20, 1000]
    $ mon1 = True
    $ mon1_hp = 100
    Hiyajou "OK LEST TEST"
    $ mon_max_hp = 100
    $ mon_hp = mon_max_hp
    $ oppmonster = "Dodo"
    $ opp_skill_position1 = ["Tackle", "Pinch", "Hard tackle", "Dodo noise"]
    $ opp_skill_dmg_position1 = [10, 15, 20, 0]
    call battle_loop
    hide screen hp_bars_1v1
    Hiyajou "WOW that nice"

# label battle_loop:
#     call battle
#     $ restorehp()
#     $ restoremp()
#     jump battle_loop
    

#     return
