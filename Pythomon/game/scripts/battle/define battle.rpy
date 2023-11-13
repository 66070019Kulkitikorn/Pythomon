image mantis_card:
    "select/mantis_card.png"
    zoom 0.85

image dophin_card:
    "select/dophin_card.png"
    zoom 0.85

image fox_card:
    "select/fox_card.png"
    zoom 0.85

define your_cri = 10
define opp_cri = 10
# define cri_success = False
# define skill_di = ""


define df0 = False
define df1 = False
define df2 = False
define df3_1 = False
define df3_2 = False
define df4 = False
define df5 = False
define bdf_2 = False
define bdf_3 = False
define bdf_4 = False

define Paper = "Paper"
define Scissors = "Scissors"
define Rock = "Rock"
image your_pick = ConditionSwitch("yours == Scissors", "card/your_scissor.png", "yours == Rock", "card/your_rock.png",
"yours == Paper", "card/your_paper.png")
image opp_pick = ConditionSwitch("opp == Scissors", "card/opp_scissor.png", "opp == Rock", "card/opp_rock.png",
"opp == Paper", "card/opp_paper.png")

define event_prolog = False
define your_turn = False
define opp_turn = False

define farright = Position(xpos=0.1)
define farleft = Position(xpos=0.9)

image oppythomon = ConditionSwitch(
"df0 == True", "pythomon_opp/dodo.png",
"df1 == True", "pythomon_opp/ant.png",
"df2 == True", "pythomon_opp/dragonfly.png",
"df3_1 == True", "pythomon_opp/stickbug.png",
"df3_2 == True", "pythomon_opp/bee.png",
"df4 == True", "pythomon_opp/bossduag.png",
"df5 == True", "pythomon_opp/finalboss.png",
"bdf_2 == True", "pythomon_opp/mosquito.png",
"bdf_3 == True", "pythomon_opp/scorpion.png",
"bdf_4 == True", "pythomon_opp/truestring.png",)

define con = ""

label win_cont:
    if mon_hp <= 0:
        hide oppythomon with dissolve
        play audio "win.mp3"
        "You Win!"
        hide screen hp_bars_1v1
        stop music
        call battle_loop
    elif your_hp <= 0:
        hide pythomon1 with dissolve
        play audio "lose.mp3"
        "You Lose :("
        hide screen hp_bars_1v1
        stop music
        call gameover 
    return
