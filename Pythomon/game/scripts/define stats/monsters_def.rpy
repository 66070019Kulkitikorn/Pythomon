label load_monsters:
    # var = Monster(name, hpmax, atk, dfn, exp, lvl, img, sfx_atk, anim, skills)
    $ empty = Monster(None, None, None, None, None, None, None, None, dead=True)
    $ mon1 = Monster("Lapras", 20, 15, 1.0, 50, 3, "1", "water", anim=slow_sway)#, skills=[arrowhail])
    $ mon2 = Monster("Ditto", 50, 20, 6.0, 50, 4, "2", "pound", anim=squeeze)#, skills=[mindfreeze])
    $ mon3 = Monster("Eevee", 30, 40, 3.0, 50, 5, "3", "tackle", anim=idle_shake)#, skills=[lifedrain])
    
    return

init python:
    class Monster(object):
        def __init__(self, name, hpmax, atk, dfn, exp, lvl, img, sfx_atk, anim=idle_shake, skills=[], state=None, dead=False, finaldmg=0, slot=1, sprite_pos=0, dmg_pos=(0,0)):
            self.name = name
            self.hpmax = hpmax
            self._hp = 0
            self._mp = 0
            self.atk = atk
            self.dfn = dfn
            #self.vel = vel
            self.state = state
            self.lvl = lvl
            self.exp = exp
            self.dead = dead
            self.skills = skills
            self.img = img
            self.sfx_atk = sfx_atk
            #self.sfx_cry = sfx_cry
            #self.sfx_die = sfx_die
            self.finaldmg = finaldmg
            self.slot = slot
            self.anim = anim
            self.sprite_pos = sprite_pos
            self.dmg_pos = dmg_pos
            #self.rarity = rarity
        @property
        def hp(self):
            value = self._hp
            if not ( 0 <= value <= self.hpmax ):
                value = max( 0, min( self.hpmax, value ) )
                self._hp = value
            return self._hp