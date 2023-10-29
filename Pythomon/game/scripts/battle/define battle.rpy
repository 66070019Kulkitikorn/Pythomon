# define mon1 = False
# define mon2 = False
# define mon3 = False
# define mon1_hp = 0
# define mon2_hp = 0
# define mon3_hp = 0
# define skill_position1 = []
# define skill_position2 = []
# define skill_position3 = []
# define skill_dmg_position1 = []
# define skill_dmg_position2 = []
# define skill_dmg_position3 = []
# define yourmonster1 = ""
# define yourmonster2 = ""
# define yourmonster3 = ""

# define your_cri = 10
# define opp_cri = 10
# define cri_success = False
# define skill_di = ""

# define opp_mon1 = False
# define opp_mon2 = False
# define opp_mon3 = False
# define opp_mon1_hp = 0
# define opp_mon2_hp = 0
# define opp_mon3_hp = 0
# define opp_skill_position1 = []
# define opp_skill_position2 = []
# define opp_skill_position3 = []
# define opp_skill_dmg_position1 = []
# define opp_skill_dmg_position2 = []
# define opp_skill_dmg_position3 = []
# define oppmonster1 = ""
# define oppmonster2 = ""
# define oppmonster3 = ""
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

image oppythomon = ConditionSwitch("opp_mon1 == True and event_prolog == True", "pythomon_opp/dodo opp.png",
"opp_mon2 == True and event_prolog == True", "pythomon_yours/cat yours.png")
