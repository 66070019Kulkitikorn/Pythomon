init python:
    style.bar_mhp = Style(style.default)
    style.bar_mhp.left_bar = Frame("images/battle/mp_full.png",20,20)
    style.bar_mhp.right_bar = Frame("images/battle/mp_empty.png",20,20)
    style.bar_mhp.xmaximum = 180
    style.bar_mhp.ymaximum = 25

    style.bar_hp = Style(style.default)
    style.bar_hp.left_bar = Frame("images/battle/hp_full.png",20,20)
    style.bar_hp.right_bar = Frame("images/battle/hp_empty.png",20,20)
    style.bar_hp.xmaximum = 213
    style.bar_hp.ymaximum = 40

    style.bar_mp = Style(style.default)
    style.bar_mp.left_bar = Frame("images/battle/mp_full.png",20,20)
    style.bar_mp.right_bar = Frame("images/battle/mp_empty.png",20,20)
    style.bar_mp.xmaximum = 213
    style.bar_mp.ymaximum = 4