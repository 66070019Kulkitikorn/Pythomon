
label prologue:
    #เขีนนdialogueตรงนี้
    scene black with slowdisslove
    $ povname = renpy.input("YOUR CODE NAME", length = 15)
    centered "Simulated Universe, a constructed world where life from both the past and the present exist in harmony."

    centered "Extinct species are brought back and developed to be compatible with this world resembling the present days, all for the sake of research."

    centered "It was published to public and was known worldwide, lives in this universe even include humans who chose to be part of the research, some took advantage of the freedom to establish organizations and some tried to use the exclusive, extinct species for business purposes."

    centered "We, the LABMEM, uses the Simulated Universe for the sole purpose of researching TAP, the perfect lifeform."

    centered “Our crucial information was leaked to Project Prologue which leads to our current mission to find and retrieve our intel from them."

    centered “All the while, collecting the DNA of lifeforms we’ve encountered in our journey to progress our research.”

    centered "As least that’s what I know so far."

    centered "Because my parents passed away since I was a child, I was taken in by the LABMEM."

    centered "Yuuki, that’s what they called me since I’ve started working with them, and this is the start of my next mission."
    show yuukii at left
    mc "But first, I have to talk to the professor."
    scene labmem_room with slowdisslove
    show yuukii at left
    show hiyajou
    h happy "Oh, you’re here, Yuuki."
    mc "Yes, I came to talk about the next mission."
    nara "Professor hiyajou is giving a serious look."
    h "Have you heard that Project Prologue has stolen our research on TAP and escaped to the Simulated Universe?"
    mc "I’ve heard about it."
    mc "Could it be that my mission is to go after them and retrieve the intel?"
    h "Basically, yes. But you’ve never been in the Simulated Universe, have you?"
    mc "That’s right. I’ve been thinking of trying it out but I’m already too busy with the real world for that."
    mc "I’ve heard that some lab members entered it for research, though. And I’ve seen about 10 of them entering it once in a while."
    mc "Still, they all entered for research purposes."
    h happy "Let’s not dive in too deep and listen to me first..."
    h "I want you to choose your partner for this mission."
    nara "Professor hiyajou The professor takes out what appears to be a set of cards from his bag."
    h "You won’t survive in the simulated universe without one of these!"
    mc "People in the simulated universe likes to play poker?"
    h "Well, you’re half right about the luck part."
    h "In the simulated universe, pythomon battles are very centralized, they pitch their creatures against each other for various purposes like gambling or just playing around."
    h confused "Kinda like Pokemon?"
    mc nervous "Poke-what?"
    h "Anyway, you will get it with practice."
    h normal "First, choose one of the 3 from their respective factions."
    h "First is Mantis from the insect faction, he deals a lot of damage but also takes a lot."  
    h "Next is Fox from the beast faction, he’s stronger when the result was a draw."
    h "The last but not least is Dolphin from the ocean faction, she’s stronger after entering the “Dive” state."
    h normal "Now choose the one you like the most!"
    mc "(Is this animal abuse..?)"
    "choose one of the 3 options"
    mc lookatme "Then I’ll go with this one."
    h happy "Oh, good choice! Hope you two get along well."
    h normal "Anyway, let’s get into topic. Our intel said that we’ve located True String in the DORM zone. I want you to go check it out."
    h "It seems to be in the possession of a girl named  \"Reine\" des abeilles from Hivemind, heard she stole it or something."
    h "You might have to fight her but don’t worry, I’ll send you an AI to assist you."
    h ""She’ll handle all the DNA extractions and teach you how to battle properly."
    show hiyajou
    mc "Sweet, so when do I start?"
    h happy "Right now. Hold that card in your hand and equip this device on your head and you’ll get sent to the Simulated Universe right away."
    nara "The professor gives Yuuki a smile as he puts on the device, blinding his vision."
    h lookat "I’ll send you somewhere around the forest then.Good luck!"
    hide labmem_room with dissolve
    call hide_all

    #เลือกตัวละคร
    menu select_mon:
        h "Select one monster"
        "Fox":
            $ yourmonster = "Fox"
            $ your_max_full = 900
            $ skill_position1 = ["Pounce", "Bite", "Trick"]
            $ skill_dmg_position1 = [200, 300, 100]
            $ Fox = True
        "Dophin":
            $ yourmonster = "Dophin"
            $ your_max_full = 850
            $ skill_position1 = ["Leap", "Flipper", "Dive"]
            $ skill_dmg_position1 = [200, 300, 0]
            $ Dophin = True
        "Mantis":
            $ yourmonster = "Mantis"
            $ your_max_full = 180
            $ skill_position1 = ["Sickles", "Grip", "Guillotine"]
            $ skill_dmg_position1 = [500, 500, 999]
            $ Mantis = True
    image pythomon1 = ConditionSwitch("Fox", "pythomon_yours/fox yours.png", "Dophin", "pythomon_yours/dophin yours.png", "Mantis", "pythomon_yours/mantis yours.png")
    $ mon1 = True
    call df0
#     $ event_prolog = True
#     ##################################
# #############################################
#     $ opp_mon1 = True
#     $ opp_mon_hp = 500
#     $ opp_skill_position1 = ["Peck", "Kick", "Flap"]
#     $ opp_skill_dmg_position1 = [95, 99, 0]
#     $ oppmonster1 = "Dodo"
# #############################################
#     call reset
#     hide Professor Hiyajou nice with dissolve
#     call battle_loop
#     hide pythomon1 with dissolve
#     $ opp_mon1 = False
#     "here some another test battle !"
# #############################################
# #     $ opp_mon2 = True
# #     $ opp_mon_hp = 200
# #     $ opp_skill_position1 = ["Battle fang", "Strike", "Far-sighted focus"]
# #     $ opp_skill_dmg_position1 = [45, 60, "Far-sighted focus"]
# #     $ oppmonster1 = "Cat"
# # #############################################
# #     call reset
# #     call battle_loop
#     $ opp_mon1 = False
#     "That the end of test what do you think?"
