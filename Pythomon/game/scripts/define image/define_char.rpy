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

style stroke_kiki:
    outlines [ ( 5, "#000000", 1, 1) ]
    color "#ff0000"

style stroke_red:
    outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
    color "#ff0000"
    size 100

style stroke_yuri:
    outlines [ ( 5, "#000000", 1, 1) ]
    color "#ff5c5c"

style stroke_reine:
    outlines [ ( 5, "#000000", 1, 1) ]
    color "#c65cff"

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
define yuriname = "???"

image yuukii = At("side yuuki normal", sprite_highlight("i_yuuki"))
image hiyajou = At("hiyajou normal", sprite_highlight("i_hiyajou"))
image pychan = At("pychan normal", sprite_highlight("i_pychan"))
image lemon = At("lemon normal", sprite_highlight("i_lemon"))
image keke1 = At("kiki1", sprite_highlight("i_kiki1"))
image keke2 = At("kiki2", sprite_highlight("i_kiki2"))
image yuri = At("yuri normal", sprite_highlight("i_yuri"))
image reine = At("reine normal", sprite_highlight("i_reine"))


define nara = Character(callback=name_callback, cb_name=None)
define h = Character("{size=+20}Professor Hiyajou{/size}" , style="stroke_hiyajou", image="hiyajou", callback=name_callback, cb_name="i_hiyajou")
define mc = Character("{size=+20}LABMEM011: [povname]{/size}" ,style="stroke_yuuki",image="yuuki", callback=name_callback, cb_name="i_yuuki")
define py = Character("{size=+20}[pychanname]{/size}" , style="stroke_pychan", image="pychan", callback=name_callback, cb_name="i_pychan")
define lemon = Character("{size=+20}[lemonname]{/size}" , style="stroke_lemon", image="lemon", callback=name_callback, cb_name="i_lemon")
define pl1 = Character("{size=+20}Prologue Punk 1{/size}" , style="stroke_kiki", image="kiki1", callback=name_callback, cb_name="i_kiki1")
define pl2 = Character("{size=+20}Prologue Punk 2{/size}" , style="stroke_kiki", image="kiki2", callback=name_callback, cb_name="i_kiki2")
define maid = Character("{size=+20}[yuriname]{/size}" , style="stroke_yuri", image="yuri", callback=name_callback, cb_name="i_yuri")
define reine = Character("{size=+20}Reine Des Abeilles{/size}" , style="stroke_reine", image="reine", callback=name_callback, cb_name="i_reine")



