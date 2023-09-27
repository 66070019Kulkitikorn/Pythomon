#ค่อยกลับมาทำ
init pyhton:
    def opp_monsters_fixed():
        global monsters_total
        global battle_monsters
        global m1
        global m2
        global m3
        mboss = copy.deepcopy(empty)
        m1 = copy.deepcopy(empty)
        m2 = copy.deepcopy(empty)
        m3 = copy.deepcopy(empty)
        if fixedset == "set 1":
            m1 = copy.deepcopy(mon1)
            m2 = copy.deepcopy(mon2)
            m3 = copy.deepcopy(mon3)
            battle_monsters = [m1,m2,m3]
        else:
            mboss = copy.deepcopy(mboss)
            battle_monsters = [mboss]
        monsters_total = len(battle_monsters)
        for m in battle_monsters:
            if m.name:
                m._hp = m.hpmax

#ตำแหน่ง mon
###########################
    def assign_pos():
        monster_slot[0].sprite_pos =
        monster_slot[1].sprite_pos =
        monster_slot[2].sprite_pos =
        monster_slot[0].dmg_pos =
        monster_slot[1].dmg_pos =
        monster_slot[2].dmg_pos =


#เปลี่ยนที่
##########################
    def swapSlot(old_slot, new_slot):
        renpy.hide_screen("display_monsters")
        monster_slot[old_slot], monster_slot[new_slot] = monster_slot[new_slot], monster_slot[old_slot]
        asignPos()
        renpy.show_screen("display_monsters")

#ฟื้นเลือด
##########################
    def restorehp():
        for c in party_list:
            c._hp = c.hpmax
#ฟื้น mp (ถ้าทำ)
##########################
    def restoremp():
        for c in party_list:
            c._mp = c.mpmax
#เริ่มเทิร์น
##########################
    def startPlayersTurn():
        for p in battle_players:
            p.turn = False

