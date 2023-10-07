#ค่อยกลับมาทำ
init python:
    def monstersFixed():
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
    # def assign_pos():
    #     monster_slot[0].sprite_pos =
    #     monster_slot[1].sprite_pos =
    #     monster_slot[2].sprite_pos =
    #     monster_slot[0].dmg_pos =
    #     monster_slot[1].dmg_pos =
    #     monster_slot[2].dmg_pos =


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
#เริ่มเทิร์นผู้เล่น
##########################
    def startPlayersTurn():
        for p in battle_players:
            p.turn = False
#จบเทิร์น
##########################
    def endTurn():
        global currentplayer
        global target
        global hp_lost
        global message
        global misstext
        message = "other_skill"
        misstext = renpy.random.choice(misstext_list)
        if isinstance(b_skill, Skill):
            b_skill.useSkill()
        elif isinstance(b_skill, Item):
            useItem(b_skill)
        if target == "all":
            atkAll()
        if target == "enemy" or target == "row":
            atkEnemy()
        if target == "ally":
            atkAlly()
        if target == "self":
            atkSelf()
        if target == "ko":
            atkAlly()
        if target == "attack":
            Attack()
        if target == "defend":
            message = "defend"
            Defend()
        currentplayer.turn = True
        currentplayer._mp -= mp_lost
        currentplayer._hp -= hp_lost
        renpy.pause(1.5, hard=True)
        playersChk()
        renpy.hide_screen("monster_dmg")


    def startTurn():
        global damage
        global hp_lost
        global atk_sfx
        global target
        global message
        global picked_targs
        global hit_t
        global missed_t
        global skill_t
        global row1btn
        global row2btn
        row1btn = False
        row2btn = False
        target = "enemy"
        message = "skill"
        damage = 0
        hp_lost = 0
        atk_sfx = None
        picked_targs = []
        hit_t = []
        missed_t = []
        skill_t = []

    def playersCnt():
        global players
        global alive_players
        players = 0
        alive_players = []
        for p in battle_players:
            if p.hp > 0:
                p.dead = False
                players += 1
                alive_players.append(p)
    
    def playersChk():
        global message
        global koplayer
        global battleEnd
        global monsters_dead
        global msg_mons
        global win
        for p in battle_players:
            if p.hp == 0 and not p.dead:
                renpy.pause(0.5)
                p.dead = True
                koplayer = p.name
                message = "player_ko"
                renpy.pause(0.7)
        for m in battle_monsters:
            if m.hp <= 0 and not m.dead:
                m.state = "dying"
                msg_mons = m.name
                message = "m_dead"
                renpy.play(sfx_monsterdead.draw())
                renpy.pause(1)
                message = "none"
                monsters_dead += 1
                m.dead = True
        if all(p.hp == 0 for p in battle_players):
            battleEnd = True
        if monsters_dead == monsters_total:
            message = "you_win"
            win = True
            battleEnd = True

    def getImage(i):
        if isinstance(i, Monster):
            return "images/monsters/"+ i.img+".png"
        if isinstance(i, Skill):
            return "images/skills/" + i.img + ".png"

    def playerAction(p):
        if not battleEnd and not p.turn:
            if renpy.get_screen("turn_select"):
                return Return(p)
            else:
                return NullAction()
        else:
            return NullAction()

    def runEvent():
        global eventrunning
        eventrunning = True
        config.allow_skipping = True
        config.rollback_enabled = True
        renpy.choice_for_skipping()
        renpy.hide_screen("tooltip")
        renpy.retain_after_load()
    def stopEvent():
        global eventrunning
        eventrunning = False
        config.allow_skipping = False
        config.rollback_enabled = False
        renpy.block_rollback()
        renpy.choice_for_skipping()
        preferences.afm_enable = False

default fixedset = None
default tt_timer = False
default damage = 0
default m_damage = 0
default dropitem = None
default atk_sfx = None
default mp_lost = 0
default hp_lost = 0
default players = 1
default monsters_total = 0
default monsters_dead = 0

default b_skill = "none"
default message = "none"
default target = "none"

default picked_targs = []
default party_list = []
default wild_monsters = []
default battle_players = []
default alive_players = []
default battle_monsters = []
default misstext_list = ["MISS!"]

default diss = Dissolve(.2)

