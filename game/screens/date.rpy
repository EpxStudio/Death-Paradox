screen calendar_screen(date, location):
    add "section_bg.png" xalign 1.0 yalign 0.0
    vbox:
        xalign 0.5
        yalign 0.5
        text date xalign 0.5 color '#ffffff'
        null height 20
        text location xalign 0.5 color '#ffffff'

label Calendar(date, location):
    show screen calendar_screen(date, location)
    with Diamonds('#ffffff')
    pause
    hide screen calendar_screen
    with Diamonds('#ffffff')
    return