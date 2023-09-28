default eventrunning = False
default _game_menu_screen = "preferences"

# เปลี่ยน cursor mouse ยังไม่ทำ หรืออาจจะไม่ทำ
##################
# init python:
#     if not renpy.variant("touch"):
#         config.mouse = {"default":[ ("images/cursor.png", 1, 1) ] }
##################

label load_setup:
    call load_monsters
    call load_items
    $ pythomon_list = [] #เริ่มมายังไม่มีซักตัว
    $ fixedset = "set 1"
    $ wild_monsters = [] #ยังไม่ใส่ศัตรู
    $ restorehp()
    return