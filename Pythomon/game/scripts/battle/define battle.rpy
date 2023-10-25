define mon1 = False
define mon2 = False
define mon3 = False
define mon1_hp = 0
define mon2_hp = 0
define mon3_hp = 0
define skill_position1 = []
define skill_position2 = []
define skill_position3 = []
define skill_dmg_position1 = []
define skill_dmg_position2 = []
define skill_dmg_position3 = []
define yourmonster1 = ""
define yourmonster2 = ""
define yourmonster3 = ""

define your_cri = 10
define opp_cri = 10
define cri_success = False
define skill_di = ""

define opp_mon1 = False
define opp_mon2 = False
define opp_mon3 = False
define opp_mon1_hp = 0
define opp_mon2_hp = 0
define opp_mon3_hp = 0
define opp_skill_position1 = []
define opp_skill_position2 = []
define opp_skill_position3 = []
define opp_skill_dmg_position1 = []
define opp_skill_dmg_position2 = []
define opp_skill_dmg_position3 = []
define oppmonster1 = ""
define oppmonster2 = ""
define oppmonster3 = ""
define event_prolog = False

define farright = Position(xpos=0.1)
define farleft = Position(xpos=0.9)

image opppythomon = ConditionSwitch("opp_mon1 == True and event_prolog == True", "pythomon_opp/dodo opp.png")