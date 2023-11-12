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
            elif df2 == True:
                call df2
            elif df3_1 == True:
                call df3_1
            elif df3_2 == True:
                call df3_2
            elif df4 == True:
                call df4_fight
            elif df5 == True:
                call df5_fight
            elif bdf_2 == True:
                call bdf_2
            elif bdf_3 == True:
                call bdf_3
            elif bdf_4 == True:
                call bdf_4
        "NO":
            py "OK :("
            $ renpy.quit()
    return