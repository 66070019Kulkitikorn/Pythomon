# $ show_score = True
# $ show_mon = True    
# $ mon_max_hp = mon_hp_max  # เลือดทั้งหมดของมอน
# $ mon_hp = mon_hp # เลือด ณ ปัจจุบันของมอน
# $ actor_attack_point  = you_attack_point # พลังโจมตีของตัวเอก
# $ actor_cri_point  =  you_attack_point * 2# พลังโจมตีติดคริของตัวเอก
# $ mon_attack_point  = op_attack_point # พลังโจมตีของมอน
# $ mon_cri_point  = mon_attack_point * 2 # พลังโจมตีติดคริของมอน
# $ hit = False
# $ miss = False

# label load_monster:
#     # $ var = Monster(name, mon_hp_max, skill1, skill2, skill3, skill4)
#     $ ruri = Monster("Ruri", 100, "Crossslash", "Kamehameha", "FantasySeal", "Masterspark")
#     return

label battle_loop:
    Hiyajou "What"
    define mon_hp = 100
    define mp = 100
    # $ skill1, skill2, skill3, skill4  = "Final Kamehameha", "MastersSpark", "Viator", "defff"
    # $ skill1dmg, skill2dmg, skill3dmg, skill4dmg, = 10, 1000, 20, 50
    # define
    # define
    # define 
    while mon_hp > 0:
        menu player_attack_choice:
            "What [yourmonster] do?"
            "[skill1]" if mp > 0:
                $ mon_hp -= skill1dmg
            "[skill2]" if mp > 0:
                $ mon_hp -= skill2dmg
            "[skill3]" if mp > 0:
                $ mon_hp -= skill3dmg
            "[skill4]" if mp > 0:
                $ mon_hp -= skill4dmg
        Hiyajou "HP [mon_hp] left!"
    return
# return

