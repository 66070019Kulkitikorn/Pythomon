init python:
    #โจมตีทุกตัว
    def atkAll():
        renpy.play(atk_sfx)
        renpy.pause(0.2, hard=True)
        for t in battle_monsters:
            if not t.dead:
                if accFormula(currentplayer, t):
                    dmgFormula(t)
                    t._hp -= t.finaldmg
                    t._mp -= mpdmg
        renpy.show_screen("monster_dmg")
        renpy.with_statement(s_trans)
    #โจมตีศัตรู
    def atkEnemy():
        for t in picked_targs:
            renpy.play(atk_sfx)
            renpy.pause(0.2, hard=True)
            if accFormula(currentplayer, t):
                dmgFormula(t)
                t._hp -= t.finaldmg
                t._mp -= mpdmg
                renpy.show_screen("monster_dmg")
                renpy.with_statement(s_trans)
                afterFX(b_skill, t)
    
    def atkAlly():
        for t in picked_targs:
            renpy.play(atk_sfx)
            renpy.pause(0.2, hard=True)
            t._hp -= damage
            t._mp -= mpdmg
            renpy.with_statement(s_trans)
    
    # def Defend():
    #     currentplayer.defending = True
    #     renpy.play("audio/battle/skills/defend.ogg")
    #     renpy.with_statement(vpunch)

    # def Attack():
    #     global damage
    #     global message
    #     global msg_mons
    #     for t in picked_targs:
    #         damage = currentplayer.atk
    #         msg_mons = t.name
    #         message = "attack_skill"
    #         renpy.play("audio/battle/skills/sword.ogg")
    #         renpy.pause(0.2, hard=True)
    #         if accFormula(currentplayer, t):
    #             t.state = "hit"
    #             dmgFormula(t)
    #             t._hp -= t.finaldmg
    #             t._mp -= mpdmg
    #             renpy.show_screen("monster_dmg")
    #             renpy.with_statement(hpunch)
    #             renpy.pause(0.2)
    #             t.state = None
    def accFormula(a, d):
        global miss_roll
        global message
        global atk_sfx
        global damage
        misschance = 0
        if d.lvl > a.lvl:
            misschance = d.lvl - a.lvl
        accuracy = 10 - int(misschance*0.7)
        miss_roll = renpy.random.randint(1, 10)
        if miss_roll > accuracy:
            missed_t.append(d)
            renpy.play(sfx_whoosh.draw())
            renpy.show_screen("monster_dmg")
            return False
        else:
            return True

    def dmgFormula(m):
        global damage
        pre_dmg = int(damage*1.1 - (damage * renpy.random.randint(1, 20) / 100))
        m.finaldmg = int(pre_dmg*(100/(100+m.dfn)))
        hit_t.append(m)
