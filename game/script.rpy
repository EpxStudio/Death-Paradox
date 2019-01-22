# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("MAIN CHARACTER")
define da = Character("DAUGHTER")
define pa = Character("PARTNER")
define sc = Character("SCIENTIST")
define bartender = Character("BARTENDER")


# The game starts here.

label start:
    scene bg room
    
    call Calendar("TUESDAY", "TOKYO", "TEN YEARS AGO")

    # Prologue
    call prologue

    return

