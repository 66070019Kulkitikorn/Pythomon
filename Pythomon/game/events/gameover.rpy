label gameover:
    scene black with dissolve
    centered "{=stroke_red}{size=+30}GAMEOVER{/size}{/stroke_yellow}"
    menu gameoverr:
        py "do you want to continue?"
        "YES":
            if df0 == True:
                call df0_fight
            elif df1 == True:
                call df1
        "NO":
            py "OK :("
            $ renpy.quit()
    return