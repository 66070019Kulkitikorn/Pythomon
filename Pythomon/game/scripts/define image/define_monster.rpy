label load_monster:
    # $ var = Monster(name, mon_hp_max, skill1, skill2, skill3, skill4)
    $ ruri = Monster("Ruri", 100, "Crossslash", "Kamehameha", "FantasySeal", "Masterspark")
    return

init python:
    class Monster(object):
        def __init__(self, name, mon_hp_max, skill1, skill2, skill3, skill4):
            self.name = name
            self.mon_hp_max = mon_hp_max
            self.skill1 = skill1
            self.skill2 = skill2
            self.skill3 = skill3
            self.skill4 = skill4
            
           


$ mon_max_hp = mon_hp_max  # เลือดทั้งหมดของมอน
$ mon_hp = mon_hp # เลือด ณ ปัจจุบันของมอน
$ actor_attack_point  = you_attack_point # พลังโจมตีของตัวเอก
$ actor_cri_point  =  you_attack_point * 2# พลังโจมตีติดคริของตัวเอก
$ mon_attack_point  = op_attack_point # พลังโจมตีของมอน
$ mon_cri_point  = mon_attack_point * 2 # พลังโจมตีติดคริของมอน
$ hit = False
$ miss = False