label df0:
    # mc = yuuki py = pychan lemon = LEMON
    scene black with slowdisslove
    "Before I know it, I woke up in a run-down cottage."
    "I try to look around, but there's nothing in the room."
    "It reminds me of the house I used to play in with my childhood friend before I was adopted."
    "I think she likes some kind of baverage... I remember it vividly."
    "I try to reach for the doorknob, but suddenly I am blinded by some kind of blue light around me."
    "When I opened my eyes, a blue-haired girl has appeared in front of me."
    show bluepy with dissolve
    show pychan
    py "..."
    "My face is unfazed because I'm used to this kind of things, I knew an AI was gonna show up."
    py "No reaction... A girl just appeared out of thin air, aren't you surprised?"
    mc "I was prepared for it."
    py "Well, that's too bad. I was really looking forward to it. Are all the humans like this?"
    mc "Maybe it's just me."
    "The AI looks around before settling to you."
    $ pychanname = "Pychan"
    py "Let me introduce myself."
    py "I'm an AI sent my Professor Hiyajou, the name's Pychan."
    mc "I'm more surprised that the AI technology has developed this much."
    mc "I thought they would've just sent a tutorial program but you even have free will now?"
    "Pychan is looking all smug."
    py "Of course!"
    py "I was sent to make sure your mission go smoothly."
    py "Before we get out of this cottage, let's go over that tutorial program you were talking about."
    #Pictures of the RPS cards here
    py "It won't take much of your time, it's just rock paper scissors after all."
    py "The pythomon that won will be the only one who get to act."
    py "In the case that it was a draw, both pythomons will get to act."
    py "But I'll make sure yours will always go first, I hope that doesn't go against your moral codes!"
    py "Just remember that luck isn't something I can help you with."
    mc "Well, this seems easier than expected."
    mc "Wait, I haven't even introduced myself yet. I'm [povname], nice to meet you."
    py "But that's just your codename, isn't it. Don't worry, I already know yours."
    "Wait, how did she know it was a codename..."
    py "We should get moving before it's dark."
    mc "True."
    #Entered Forest
    "After we leave the cottage, we were surrounded by trees."
    "Looks like Hiyajou really just dropped us into a forest."
    "Wait, I think I see someone."
    "Oh, she already noticed me."
    show lemon
    lemon "!"
    "She stared at me and paused for a bit before speaking up."
    lemon "Oh, it's the LAB:MEM! Was wondering why I haven't seen you around here."
    $ lemonname = "LEMON"
    lemon "I'm Lemon, my company is the No.1 sponsor of LAB:MEM, you know?"
    lemon "I regularly work in the simulated universe and for some reason people here call me the Debtor."
    mc "I'm [povname], know the way to the Hive?"
    lemon "Pretty casual, I like it."
    lemon "You wanna meet Reine too, huh?"
    mc "Did you say too?"
    lemon "I can guess. Heard she's the current boss of the Hivemind group. The last one just up and died so she took over."
    lemon "Hivemind actually go way back in the real world, now that it's in the simulated universe it's still rejected."
    lemon "Not just because of their old deeds but they also took the True String from the DORM."
    py "That True Sting she's talking about is the apex of the insect faction, by the way."
    mc "I know, heard it from Hiyajou."
    lemon "Something's wrong?"
    mc "Nah, nothing."
    "Doesn't look like Lemon can see Pychan, guess only I can see her."
    mc "So, are you coming to Hivemind too?"
    lemon "Yes, but I have to take care of some business around here first."
    lemon "Say, why don't we have a battle before we part?"
    mc "That pythomon battle thing, huh."
    lemon "Exactly! This is your first time, right? Then I'll go easy on you."
    call df0_fight

label df0_fight:
    lemon "Ready when you are!"
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
    scene black with slowdisslove
    call battle_loop
    hide pythomon1 with dissolve
    $ df0 = False
#############################################
    lemon "You're pretty good for a good timer!"
    py "You're pretty good for a good timer!"
    mc "She already said that just keep quiet!"
    lemon "What did you just say?"
    mc "Oh, nothing. I have a habit of talking to my imaginary friend."
    lemon "Huh. Well, I won't judge. That battle was pretty fun!"
    lemon "The Hive is just ahead that way... At least that's what I'm told, I haven't actually been there yet."
    mc "Wait, then can I even believe you?"
    lemon "Time's out! Next time we meet I hope you will use your real name!"
    "Lemon makes haste and went off in her own way."
    mc "Next time?"
    py "Do you know her?"
    mc "Not even familiar."
    py "Putting that aside. Let's see if Lemon gave us the right direction."
    mc "Right."
    menu df0_next:
        "Forward!":
            scene black with slowdisslove
            call df1




