style stroke_pychan:
    outlines [ ( 5, "#000000", 1, 1) ]
    color "#00ffff"

style stroke_hiyajou:
    outlines [ ( 5, "#000000", 1, 1) ]
    color "#ffffff"

style stroke_yuuki:
    outlines [ ( 5, "#000000", 1, 1) ]
    color "#ff008c"

style stroke_lemon:
    outlines [ ( 5, "#000000", 1, 1) ]
    color "#fbff00"

style stroke_red:
    outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
    color "#ff0000"
    size 100

style stroke_green:
    outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
    color "#00ff55"
    size 100

# style stroke_blue:
#     outlines [ ( 100, "#000000", 1, 1) ]
#     color "#00aeff"
#     size 100

style stroke_yellow:
    outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
    color "#e1ff00"
    size 100
define slowdisslove = Dissolve(1)

define pychanname = "???"
define lemonname = "???"

image yuukii = At("side yuuki normal", sprite_highlight("i_yuuki"))
image hiyajou = At("hiyajou normal", sprite_highlight("i_hiyajou"))
image pychan = At("pychan normal", sprite_highlight("i_pychan"))
image lemon = At("lemon normal", sprite_highlight("i_lemon"))


define nara = Character(callback=name_callback, cb_name=None)
define h = Character("{size=+20}Professor Hiyajou{/size}" , style="stroke_hiyajou", image="hiyajou", callback=name_callback, cb_name="i_hiyajou")
define mc = Character("{size=+20}LABMEM011: [povname]{/size}" ,style="stroke_yuuki",image="yuuki", callback=name_callback, cb_name="i_yuuki")
define py = Character("{size=+20}[pychanname]{/size}" , style="stroke_pychan", image="pychan", callback=name_callback, cb_name="i_pychan")
define lemon = Character("{size=+20}[lemonname]{/size}" , style="stroke_lemon", image="lemon", callback=name_callback, cb_name="i_lemon")



