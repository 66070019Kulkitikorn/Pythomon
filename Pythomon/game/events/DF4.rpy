label df4:
    #mc = yuki py = pychan maid = yuri
    scene castle_outdoor with dissolve
    "And here we are. Right in front of the Hive."
    "But this seems way too peaceful... Where are all the guards?"
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left with dissolve
    py "There's no doubt about it, I think this is the Hive."
    show pychan at right
    mc "You think? They might as well just give me a DNA extractor..."
    py "Well, keeping you entertained is one of my instructions."
    show pychan at right
    mc nervous "So? Are we going in or not?"
    hide bluepy 
    hide pychan
    show yuri with dissolve
    maid "Do you wish to have an audience with the queen?"
    show yuri
    play music "audio/bgm/maid before.mp3" loop
    nara "I was about to bust through the gate but someone was already in front of me."
    $ yuriname = "Yuri"
    maid "Good day, I am Yuri. The head maid of lady Reine. Do you have any business with her? I can lead the way."
    show yuri
    nara "So Reine is really here."
    nara "And is that a basket of fresh lemons back there..?"
    call hide_all
    show yuri
    show bluepy 
    show yuukii at left
    show pychan at right with dissolve
    py dotdotdot "What is a maid doing in a mafia gang?"
    hide bluepy 
    hide pychan
    nara "I guess the mafias are keeping up with the trend."
    mc normal "I want to talk to Reine so can you lead the way?"
    nara "Yuri wears a smile and starts evaluating me from afar."
    maid "I'm glad you came to see lady Reine too."
    call hide_all
    show yuri
    show bluepy 
    show yuukii at left
    show pychan at right with dissolve
    py "Too? Did she mean Lemon?"
    hide bluepy 
    hide pychan
    show yuri
    maid closeeye "I'm glad that we're having some guests."
    maid mad "But..."
    show yuri
    mc "..."
    maid closeeye "It pains me to say this. But I cannot let you pass."
    call hide_all
    show yuri
    show bluepy 
    show yuukii at left
    show pychan at right with dissolve
    py "Huh..?"
    stop music fadeout 1.0
    hide bluepy 
    hide pychan
    call df4_fight

label df4_fight:
    scene castle_outdoor
    show yuri
    show yuukii at left
    maid "The queen's wish is my demand. That goes for stopping the LAB:MEM as well."
    maid what "I won't let you guys hurt her again!" with hpunch
    call hide_all
    show yuri
    show bluepy 
    show yuukii at left
    show pychan at right with dissolve
    py dotdotdot "Looks like the only way out is to commit..."
    hide bluepy 
    hide pychan
    mc nervous "No helping it. Don't think I'll go easy just because you're a girl."
    #############################################
    $ df4 = True
    $ opp_mon_hp = 1000
    $ opp_skill_position1 = ["Rush", "Thrust", "Lift"]
    $ opp_skill_dmg_position1 = [300, 400, 444]
    $ oppmonster1 = "Hercules Beetle"
#############################################
        #############################################
    call reset
    call hide_all
    play music "audio/bgm/maid theme.mp3" loop
    scene castle outdoor blur with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df4 = False
#############################################
    scene castle_outdoor with dissolve
    show yuri with dissolve
    show yuukii at left
    maid mad "You're strong..."
    maid "You're actually just here to extract the DNA from True String, aren't you?"
    show yuri
    mc nervous "How did you know?"
    maid mad "If not for research, why would LAB:MEM come here?"
    show yuri
    nara "Are we really that boring?"
    play music "audio/bgm/dramatic yuri.mp3" loop
    maid closeeye "Truth be told, I already knew you guys aren't up to no good."
    maid mad "But I've still got work to do."
    show yuri
    mc "Let me guess, Project Prologue again."
    maid mad "..."
    show yuri
    nara "Yuri still wears her smile but it can't really hide anything."
    nara "This facade of a smile is something she's trained to do."
    maid mad "After the boss passed away. Lady Reine had to do the dirty work after him."
    maid "She's always berated at school, and at some point, she stopped attending entirely."
    maid "I've been with her since forever. The hierarchy of Hivemind Boss and the maid goes way back."
    maid what "Honestly, I don't agree with how things work in Hivemind either. It disgusts me."
    maid "Lady Reine is kind, she isn't like them. She entered the simulated universe to prove that."
    maid "But as soon as she set foot here, everyone already resent her and even made accusations."
    show yuri
    mc "Accusations?"
    maid "The queen does not have what you're looking for."
    show yuri
    mc "You mean... the True Sting?"
    maid "Like I said, we don't have the True String at all. We don't even know where it is now."
    call hide_all
    show yuri
    show bluepy 
    show yuukii at left
    show pychan at right with dissolve
    py scared "Aside from here, we would only have the danger zone left. And can we even trust her?"
    py "Like the name implied, that zone is of high danger-level. Those who entered never came back. I wouldn't advise to do it."
    hide bluepy 
    hide pychan
    maid "Whether you want to believe it or not is your choice. If you don't then come this way."
    show yuri
    menu gotohive:
        "Enter the Hive":
            maid "I see. Then follow me."
            maid "There's actually something else I want to say. But I'll leave it to the queen."
            maid "I'm sure she will speak her mind because I know what kind of person she is."
            scene black with slowdisslove
            stop music fadeout 1.0
            call df5
        "Take a detour":
            call hide_all
            show yuri
            show bluepy 
            show yuukii at left
            show pychan at right with dissolve
            py scared "Wait, are you sure about this? Did you not hear what I just said?"
            show pychan at right
            mc "With you here, what is there to afraid? We've got a mission to complete."
            mc "And we can just recall when things get bad, can't we?"
            py scared "But still!"
            hide bluepy 
            hide pychan
            mc "Then, I'll take a detour."
            maid "I see. Then, please excuse me."
            hide yuri with dissolve
            "Yuri left, contented."
            scene black with slowdisslove
            stop music fadeout 1.0
            call bdf_4
            # call df0_fight
