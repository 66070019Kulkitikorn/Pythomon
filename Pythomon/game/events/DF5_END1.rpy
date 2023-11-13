label df5:
    "To find out the truth for myself, I entered the Hive with Pychan and Yuri."
    show yuri
    maid "This is as far as I can help you, I'll take my leave."
    play audio "Open5.ogg"
    scene red_castle with dissolve
    "Yuri walks off into the distant hallway, leaving only me and Pychan."
    show bluepy 
    show pychan at right with dissolve
    show yuukii at left
    play music "audio/bgm/reine castle.mp3" loop
    py "Looks like the mission is nearing its end."
    mc nervous "What if she really doesn't have the True Sting?"
    py happy "There's no doubt about it. If the True Sting is free in the danger zone, even the food chain there will be ruined."
    py "Now let's finish this."
    ##Entering the Throne Room###
    hide bluepy 
    hide pychan
    "After entering the throne room, there were already two people. One down, and one thriving."
    call hide_all
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py uh "Isn't that Lemon? Why is she down on the floor?"
    hide bluepy 
    hide pychan
    show reine with dissolve
    mc angry "So, you really were an enemy!" with hpunch
    reine "Could you perhaps be her acquaintance, LAB:MEM?"
    reine smile "My name is Reine des Abeilles, the rightful heir of Hivemind."
    reine talk "If you've made it this far, it means Yuri let you pass, didn't she?"
    show reine
    mc "I'll have you know, we bulldozed our way through her."
    call hide_all
    show reine
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py angry "Don't make us sound like the villains here!" with hpunch
    call df5_fight

label df5_fight:
    scene red_castle
    show reine
    show yuukii at left
    stop music fadeout 1.0
    reine "How you made it here doesn't matter, this is as far as you'll go."
    reine smile "I know you LAB:MEMs never give up without a fight, so please excuse me for destroying you here and now."
    reine angry "I need those research you're holding after all."
    call hide_all
    show reine
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py jeez "She's getting full of herself just because she's the boss, let her have it!"
    #############################################
    $ df5 = True
    $ opp_mon_hp = 1200
    $ opp_skill_position1 = ["Queen's Swarm", "Queen's Stinger", "Queen's Larvae"]
    $ opp_skill_dmg_position1 = [300, 400, 0]
    $ oppmonster1 = "Queen Bee"
#############################################
    call reset
    call hide_all
    play music "audio/bgm/reine theme.mp3" loop
    scene red castle blur with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df5 = False
############################################
    scene red_castle with dissolve
    show reine with dissolve
    show yuukii at left with dissolve
    play music "audio/bgm/dramatic yuri.mp3" loop
    reine sad "How... I was doing exactly as instructed..."
    call hide_all
    show reine
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py nervous "Why didn't she bring out the True Sting?"
    show pychan
    nara "That's because she doesn't even have it..."
    nara "But instructions? For what?"
    hide bluepy 
    hide pychan
    reine sad "I just want to cleanse the name of my blood..."
    reine "Those guys said that the world will be saved if we can stop the LAB:MEM."
    reine "Even if I didn't believe it. I don't really have much of a choice."
    show reine
    show lemon at right with dissolve
    stop music fadeout 1.0
    lemon "So you just do as they say? That's it?"
    show reine
    show lemon at right
    play music "audio/bgm/forest theme.mp3" loop
    mc angry "LEMON!?" with hpunch
    lemon "Oh, it's you again. How long have I been out."
    reine "Approximately 4 hours."
    lemon what "Why, that's nothing!"
    show reine
    show lemon at right
    mc lookatme "What's going on here, she didn't knock you out?"
    lemon "Oh, that? I just came to talk business with lady Reine here, so she brought me these fresh lemonade."
    lemon "I just can't get enough of it and caught a brain freeze, sorry about that."
    show reine
    show lemon at right
    mc "..."
    call hide_all
    show reine
    show lemon at right
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py dotdotdot "..."
    hide bluepy 
    hide pychan
    reine smile "Yuri is already on her way to harvest more lemons. Don't worry, there will be enough for everyone."
    show reine
    nara "So that's what the basket was all about..."
    lemon "So what did you come here for?"
    show reine
    show lemon at right
    mc "I came for the True Sting but it doesn't seem to be here."
    reine "The rumors again, I see. I'm used to it."
    lemon "So that's it... Let's get to the point then."
    lemon "I'm here to collect the debt from the Hivemind."
    lemon "But when I'm here, the lemonade was worth way more!" 
    show reine
    show lemon at right
    mc "What a sour reason..."
    lemon "So I think I was going to change my mind but I passed out first."
    reine nani "You mean you will lift the debt!?" with hpunch
    call hide_all
    show reine
    show lemon at right
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py dotdotdot "She's more generous than I thought."
    hide bluepy 
    hide pychan
    lemon what "Well, you're half right. But there's a condition."
    show lemon at right
    reine "A condition?"
    lemon "First, you have to transform the Hivemind into a lemonade factory."
    nara "This is going way too overboard..."
    lemon "Our company will back it up so it's sure to be famous worldwide, or universewide..."
    lemon "The mafia gang will be as good as disbanded and your name is cleansed, isn't this just perfect?"
    reine "It certainly seems tempting."
    nara "She likes lemonade that much? I feel like I used to know someone like that."
    lemon "Now for the last condition, give us your assistance and help us put an end to Project Prologue instead."
    lemon "I know that you were forced to comply, but don't worry, we're your allies."
    show reine
    show lemon at right
    mc closeeye "Well, there's that. I was just sent by Hiyajou, no hard feelings."
    call hide_all
    show reine
    show lemon at right
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py angry "Stop with the villain talk already!" with hpunch
    hide bluepy 
    hide pychan
    mc "But the desire to turn over a new leaf. I can dig that."
    mc normal "Project Prologue is indiscriminately striving for their goal. Who knows how many people they've hurt."
    mc "I'm sure someone as kind and strong as you will be of great help."
    call hide_all
    show reine
    show lemon at right
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py dotdotdot "Being an mc all of a sudden, huh?"
    hide bluepy 
    hide pychan
    reine "..."
    reine smile "If that's what you think then I'm glad to help."
    reine "Project Prologue reminds me of the old Hivemind, I'll help you stop them from hurting more people."
    reine talk "Listen, their real goal is to-"
    hide reine
    stop music
    play audio "error.mp3"
    show reineerror
    pause 0.1
    hide reineerror
    scene red_castle_error
    show reineerror2
    pause 0.1
    hide reineerror2
    show reineerror3
    pause 0.1
    hide reineerror3
    scene red_castle_red
    show yuukii at left
    show lemon at right
    centered ""
    nara "But suddenly Reine disappeared into thin air, and the surroundings turned all red."
    play music "audio/bgm/climax.mp3" loop
    lemon look "Did she just get force-recalled?!"
    show lemon at right
    mc angry "Force-recall? What is that?" with hpunch
    play audio "Open5.ogg"
    show yuri with dissolve
    nara "Yuri storms in."
    maid what "Reine! Lady Reine!" with hpunch
    show lemon at right
    show yuri
    mc "Let's recall and notify Hiyajou!" with hpunch
    lemon look "Yeah, and quick!"
    show lemon at right
    nara "We all try to initiate the recall process."
    nara "But to no avail..."
    lemon look "It's not working..."
    show lemon at right
    show yuri
    mc "Doesn't look like I can connect to Hiyajou either, are we stuck here?"
    maid what "Lady Reine!" with hpunch
    show lemon at right
    show yuri
    mc "Pychan! Status report?"
    call hide_all
    show yuri
    show lemon at right
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py nervous "..."
    py "This is bad."
    show pychan at right
    mc "On a scale of 10?"
    py scared "Could be an 11. Looks like Project Prologue already gained full control of the firewall."
    show pychan at right
    mc "Can't you do anything about it with your mighty AI technology?"
    py uh "Well, do you think ChatGPT would be able to do anything about it?"
    show pychan at right
    mc "ChatGP- What are you even talking about?"
    hide bluepy 
    hide pychan
    lemon look "I don't think Project Prologue can completely take authority of the firewall."
    lemon "We have to figure out what they did and stop them fast."
    hide lemon with dissolve
    hide yuri with dissolve
    hide yuukii with dissolve
    "Why did they do it right after Reine was about to say something important..."
    "Could it be our fault that lady Reine disappeared?"
    "Were their eyes on us this whole time?"
    "What is happening to the simulated universe?"
    "My mind is in a tempest but I cannot stop here."
    "Just wait for me, I'll save you, Reine. ...But for now, I'll have to 'save' the game first, please excuse me."
    "Chapter 1: Ending 1"
    $ renpy.movie_cutscene("videos/goodend.webm", loops=0, stop_music=True)
    $ renpy.quit()








