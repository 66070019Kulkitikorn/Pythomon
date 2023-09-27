##########################
#ยังเขียนไม่เสร็จ อย่าเพิ่ง ctrl + / เดี๋ยวรันแล้ว error
#ถ้าจะเขียน crop code และ ctrl + /
##########################

#Set Battle

# label battle:
# $ stopEvent()
#     if fixedset:
#         $ monstersFixed()
#         $ monster_slot = [m1,m2,m3]
#         $ fixedset = None
#     else:
#         $ monstersRoll()
#         $ monster_slot = [m1,m2,m3]
#         $ renpy.random.shuffle(monster_slot)
#     $ asignPos()
#     $ row1btn = False
#     $ row2btn = False
#     $ missed_t = []
#     $ win = False
#     $ battleEnd = False
#     $ monsters_dead = 0
#     $ currentplayer = None
#     show screen battle_tooltip

# # เพลงจะใส่อีกทีตรงนี้

# ######################

# # ตำแหน่ง pythomon ของเรา
# label player_position:
#     $ battle_pythomon = [p1, p2, p3]
#     $ p1.img_pos = 512
#     $ p1.bar_pos = 944
#     $ p1.dmg_pos = 1136
#     if p2 != "none":
#         $ p1.img_pos = 0
#         $ p1.bar_pos = 432
#         $ p1.dmg_pos = 624
#     else:
#         $ p1 = None
#     if p3 != "none":
#         $ p2.img_pos = 1024
#         $ p2.bar_pos = 1456
#         $ p2.dmg_pos = 1648
#     else:
#         $ p2 = None
#     return

# #################################

# # แสดงศัตรู ยังงงๆอยู่มันคืออะไรนะ?
# screen display_monsters():
#     fixed:
#         pos (576, 640)
#         for m in monster_slot[4:8]:
#             fixed:
#                 xpos m.sprite_pos
#                 if not m.dead:
#                     imagebutton at m.anim:
#                         hover im.MatrixColor(getImage(m), im.matrix.brightness(0.1))
#                         action Return(m), SensitiveIf(canTarget(m))
#                         idle monsterImg(m) anchor (0.5,1.0)
#                         if renpy.get_screen("select_monster"):
#                             insensitive im.MatrixColor(getImage(m), im.matrix.saturation(0.1))
#                         tooltip "{0} HP: {1}".format(m.name, m.hp)
#                     bar style "bar_mhp" value AnimatedValue(value=m.hp, range=m.hpmax, delay=0.25) anchor (0.5,1.0)
#                     text "[m.hp]" xanchor 0.5

# ###########################

# # แสดงข้อความต่อสู้ ของมแปปนะ
# screen battle_message():
#     add "images/battle/messagebox.png"
#     hbox:
#         xpos 110 yalign 0.07
#         if message == "attack":
#             text "Who will attack?"
#         elif message == "skill":
#             text "What will {0} do?".format(currentplayer.name)
#         elif message == "item":
#             text "Select an item"
#         elif message == "other_skill":
#             text "{0} used [msg_skill]!".format(currentplayer.name)
#         elif message == "attack_skill":
#             text "{0} attacked [msg_mons]!".format(currentplayer.name)
#         elif message == "defend":
#             text "{0} raises defense!".format(currentplayer.name)
#         elif message == "m_skill":
#             text "[msg_mons] attacks with [msg_skill]!"
#         elif message == "m_atk":
#             text "[msg_mons] attacks {0}!".format(roll_target.name)
#         elif message == "target_who":
#             text "Who is the target?"
#         elif message == "m_dead":
#             text "[msg_mons] died!"
#         elif message == "player_ko":
#             text "[koplayer] is out of combat!"
#         elif message == "you_win":
#             text "Congrats! You've won!"
#         elif message == "lost":
#             text "You lost..."
#         elif message == "use_on_who":
#             text "Use skill on whom?"
#         elif message == "none":
#             text ""

# ######################
# # ต่อสู้
# label battling:
#     $ inCombat = True
#     while inCombat:
#         if battleEnd == True:
#             $ inCombat = False
#             jump end_battle
#         $ startPlayersTurn()
#         $ message = "attack"
#         call turn_actions
#         $ message = "none"
#         $ monsterTurns()

# ########################3
# # จบต่อสู้
# label end_battle:
#     hide screen battle_overlay
#         with dissolve
#         if win:
#             stop music
#             play sound fanfare
#             "You win!"
#             stop sound
#             $ expFormula()
#         else:
#             $ message = "lost"
#             "You lose."
#         hide screen battle_message
#         hide screen display_monsters
#         return

