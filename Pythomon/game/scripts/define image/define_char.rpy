style stroke:
    outlines [ ( 5, "#000000", 1, 1) ]
    color "#00ffff"

style stroke_yuuki:
    outlines [ ( 5, "#000000", 1, 1) ]
    color "#ff008c"

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

image yuukii = At("side yuuki normal", sprite_highlight("i_yuuki"))
image hiyajou = At("hiyajou normal", sprite_highlight("i_hiyajou"))

define nara = Character(callback=name_callback, cb_name=None)
define h = Character("{size=+20}Professor Hiyajou{/size}" , style="stroke", image="hiyajou", callback=name_callback, cb_name="i_hiyajou")
define mc = Character("{size=+20}LABMEM011: [povname]{/size}" ,style="stroke_yuuki",image="yuuki", callback=name_callback, cb_name="i_yuuki")
define lemon = Character("LEMON", image="lemon")



