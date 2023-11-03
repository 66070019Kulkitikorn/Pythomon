label df1:
    "พวกเราเดินตรงมาตามทางในป่าไปเรื่อยๆจนกระทั่ง"
    #มดออกมา
    py "มด?"
    mc "ฉันว่าเราอย่าไปยุ่งดีกว่านะ แค่มดตัวน้อยๆอย่ารังแก---"
    py "ยังไงก็ต้องสู้"
    mc "เดี๋ยว ทำไมเราต้องสู้กับมด---"
    py "เ พื่ อ ก า ร วิ จั ย"
    mc "ห๊ะ----"
    #############################################
    $ df1 = True
    $ opp_mon_hp = 888
    $ opp_skill_position1 = ["Sting", "Bite", "Pheromone"]
    $ opp_skill_dmg_position1 = [150, 222, 0]
    $ oppmonster1 = "Ant"
#############################################
    call reset
    call hide_all
    scene black with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df1 = False
#############################################
    mc "ถึกเอาเรื่องเลยแฮะ"
    mc "เธอนี่โหดร้ายใช่เล่นเลยแฮะ"
    py "ก็พวกProject Prologueขโมยไปซะเหี้ยนเลย ยังไงก็ต้องทำแหละ"
    py "ฉันบันทึกเรียบร้อยแล้ว พวกเราเดินหน้าต่อเถอะ"
    "พวกLABMEMคนก่อนๆ นี่โหดร้ายกันขนาดนี้รึป่าวนะ?"
    menu df1_next:
        "เดินตรงไป":
            scene black with slowdisslove
            call df2
        # "เลี้ยวซ้าย":
