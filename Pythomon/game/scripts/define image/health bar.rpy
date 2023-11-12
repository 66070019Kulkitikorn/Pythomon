

screen hp_bars_1v1:
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "{size=+30}[yourmonster]{/size} [your_hp]/[your_max_hp]"
        bar value  your_hp range your_max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "{size=+30}[oppmonster]{/size} [mon_hp]/[mon_max_hp]"
        bar value mon_hp range mon_max_hp