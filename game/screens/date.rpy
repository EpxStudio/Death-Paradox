screen calendar_screen(date, location, year):
    add "section_bg.png" xalign 1.0 yalign 0.0
    vbox:
        xalign 0.25
        yalign 0.5
        text date xalign 0 color '#ffffff' font 'fonts/Anurati-Regular.otf' kerning 10
        null height 20
        text location xalign 0 color '#ffffff' font 'fonts/Coves Bold.otf' kerning 5
        null height 20
        text year xalign 0 color '#ffffff' font 'fonts/Coves Light.otf' kerning 10

label Calendar(date, location, year):
    show screen calendar_screen(date, location, year)
    with Diamonds('#ffffff')
    pause
    hide screen calendar_screen
    with Diamonds('#ffffff')
    return