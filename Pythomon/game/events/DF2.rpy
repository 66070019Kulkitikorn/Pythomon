label df2:
    "ผมเดินไปเรื่อยๆจนกระทั่งเจอคนไม่คาดคิด"
    # pl1 = ลูกกระจอก Project Prologue 1
    pl1 "หืมคนในLABMEMงั้นเรอะ"
    py "อ้อคนใน Project Prologue นี่เอง"
    "พอเคยได้ยินมาบ้าง แต่ก็ไม่เคยเจอจริงๆ"
    pl1 "พวกเรา Project Prologue ต้องหยุดการวิจัยของพวกแกซะ"
    pl1 "อย่างน้อยชั้นจะไม่ให้แกผ่านไปเด็ดขาด!"
    mc "ปกติพวก Project Prologue มันเลือดร้อนขนาดนี้เลยหรอ"
    py "จากฐานข้อมูลบางอย่าง เห็นว่า Project Prologue ให้เงินเยอะถ้าจัดการคนในLABMEMได้"
    mc "หิวเงินนี่เอง"
    py "นายคงไม่โดนมันจัดการง่ายๆหรอกใช่มั้ย?"
    mc "อืมคงงั้นมั้ง"
    py "อย่ามามั้งสิ!"
    #############################################
    $ df2 = True
    $ opp_mon_hp = 650
    $ opp_skill_position1 = ["Dash", "Dogfight", "Chase"]
    $ opp_skill_dmg_position1 = [250, 99, 0]
    $ oppmonster1 = "Dragonfly"
#############################################
    call reset
    call hide_all
    scene black with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df2 = False
#############################################
    py "สุดท้ายก็หนีไปจนได้"
    mc "ต้องตามล่ามั้ย"
    py "ล่าได้ก็ดี แต่ว่าแค่เก็บงานวิจัยจากdragonflyของมันก็พอละ"
    py "เหมือนจะมีแยกทางอีกแล้วนะ ไปทางไหนดี?"
    menu df2_select2:
        "เลี้ยวซ้าย":
            call df0_fight
        "เดินตรงไป":
            call df0_fight
        "เลี้ยวขวา":
            call df0_fight

