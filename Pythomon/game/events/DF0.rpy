label df0:
    # mc = yuuki py = pychan lemon = LEMON
    scene black with slowdisslove
    "Before I know it, I woke up in a run-down cottage."
    "I try to look around, but there's nothing in the room."
    "It reminds me of the house I used to play in with my childhood friend before I was adopted."
    "I think she likes some kind of baverage... I remember it vividly."
    "I try to reach for the doorknob, but suddenly I am blinded by some kind of blue light around me."
    "When I opened my eyes, a blue-haired girl has appeared in front of me."
    play music "audio/bgm/pychan theme.mp3" loop
    show bluepy with dissolve
    show yuukii at left with dissolve
    show pychan
    py "..."
    nara "My face is unfazed because I'm used to this kind of things, I knew an AI was gonna show up."
    py jeez "No reaction... A girl just appeared out of thin air, aren't you surprised?"
    show pychan
    mc "I was prepared for it."
    py dotdotdot "Well, that's too bad. I was really looking forward to it. Are all the humans like this?"
    show pychan
    mc nervous "Maybe it's just me."
    nara "The AI looks around before settling to you."
    $ pychanname = "Pychan"
    py nice "Let me introduce myself."
    py happy "I'm an AI sent my Professor Hiyajou, the name's Pychan."
    show pychan
    mc nervous "I'm more surprised that the AI technology has developed this much."
    mc "I thought they would've just sent a tutorial program but you even have free will now?"
    nara "Pychan is looking all smug."
    show pychan
    py "Of course!"
    py normal "I was sent to make sure your mission go smoothly."
    py "Before we get out of this cottage, let's go over that tutorial program you were talking about."
    show pychan at right with move
    #Pictures of the RPS cards here
    show rule at truecenter
    py "It won't take much of your time, it's just rock paper scissors after all."
    py "The pythomon that won will be the only one who get to act."
    py "In the case that it was a draw, both pythomons will get to act."
    py nice "But I'll make sure yours will always go first, I hope that doesn't go against your moral codes!"
    py nervous "Just remember that luck isn't something I can help you with."
    hide rule with dissolve
    show pychan
    mc closeeye "Well, this seems easier than expected."
    mc normal "Wait, I haven't even introduced myself yet. I'm [povname], nice to meet you."
    py normal "But that's just your codename, isn't it. Don't worry, I already know yours."
    show pychan
    nara "Wait, how did she know it was a codename..."
    py "We should get moving before it's dark."
    mc nervous "True."
    hide bluepy and pychan and yuuki with dissolve
    # hide pychan with dissolve
    # hide yuukii at left with dissolve
    stop music fadeout 1.0
    play audio "Open5.ogg"
    scene forest background
    #Entered Forest
    nara "After we leave the cottage, we were surrounded by trees."
    nara "Looks like Hiyajou really just dropped us into a forest."
    nara "Wait, I think I see someone."
    nara "Oh, she already noticed me."
    play music "audio/bgm/forest theme.mp3" loop
    show lemon with dissolve
    show yuukii at left with dissolve
    lemon "!"
    nara "She stared at me and paused for a bit before speaking up."
    lemon "Oh, it's the LAB:MEM! Was wondering why I haven't seen you around here."
    $ lemonname = "LEMON"
    lemon "I'm Lemon, my company is the No.1 sponsor of LAB:MEM, you know?"
    lemon what "I regularly work in the simulated universe and for some reason people here call me the Debtor."
    show lemon
    mc "I'm [povname], know the way to the Hive?"
    lemon "Pretty casual, I like it."
    lemon "You wanna meet Reine too, huh?"
    mc "Did you say too?"
    lemon look "I can guess. Heard she's the current boss of the Hivemind group. The last one just up and died so she took over."
    lemon "Hivemind actually go way back in the real world, now that it's in the simulated universe it's still rejected."
    lemon "Not just because of their old deeds but they also took the True String from the DORM."
    call hide_all
    show lemon
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py "That True Sting she's talking about is the apex of the insect faction, by the way."
    mc "I know, heard it from Hiyajou."
    hide bluepy 
    hide pychan 
    lemon "Something's wrong?"
    show lemon
    mc nervous "Nah, nothing."
    nara "Doesn't look like Lemon can see Pychan, guess only I can see her."
    mc "So, are you coming to Hivemind too?"
    lemon "Yes, but I have to take care of some business around here first."
    lemon "Say, why don't we have a battle before we part?"
    mc nervous "That pythomon battle thing, huh."
    lemon "Exactly! This is your first time, right? Then I'll go easy on you."
    call df0_fight

label df0_fight:
    scene forest background
    show lemon
    show yuukii at left
    lemon "Ready when you are!"
    call hide_all
    show lemon
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py "Just remember what I told you!"
#############################################
    $ df0 = True
    $ opp_mon_hp = 500
    $ opp_skill_position1 = ["Peck", "Kick", "Flap"]
    $ opp_skill_dmg_position1 = [95, 99, 0]
    $ oppmonster1 = "Dodo"
#############################################
    call reset
    call hide_all
    play music "audio/bgm/battle.mp3" loop
    scene forest background blur with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df0 = False
#############################################
    play music "audio/bgm/forest theme.mp3" loop
    scene forest background with dissolve
    show lemon with dissolve
    show yuukii at left
    lemon normal "You're pretty good for a good timer!"
    call hide_all
    show lemon
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py happy "You're pretty good for a good timer!"
    show pychan at right
    mc angry "She already said that just keep quiet!"
    hide bluepy 
    hide pychan 
    lemon what "What did you just say?"
    show lemon
    mc nervous "Oh, nothing. I have a habit of talking to my imaginary friend."
    lemon normal "Huh. Well, I won't judge. That battle was pretty fun!"
    lemon "The Hive is just ahead that way... At least that's what I'm told, I haven't actually been there yet."
    show lemon
    mc lookatme "Wait, then can I even believe you?"
    lemon "Time's out! Next time we meet I hope you will use your real name!"
    show lemon
    hide lemon with dissolve
    nara "Lemon makes haste and went off in her own way."
    mc "Next time?"
    hide yuukii
    show bluepy
    show yuukii at left
    show pychan at right with dissolve
    py "Do you know her?"
    show pychan at right
    mc "Not even familiar."
    py "Putting that aside. Let's see if Lemon gave us the right direction."
    show pychan at right
    mc "Right."
    hide bluepy 
    hide pychan
    hide yuukii
    menu df0_next:
        "Forward!":
            scene black with slowdisslove
            stop music fadeout 1.0
            call df1




