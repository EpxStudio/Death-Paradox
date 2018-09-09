define transitioncolors = [
    '#111111', # black
    '#ffffff', # white
]

define diamonds = ImageDissolve("images/transitions/diamonds.png", 1.0)

define Diamonds = lambda color=None: MultipleTransition([
    False, diamonds,
    (color if color != None else renpy.random.choice(transitioncolors)), diamonds,
    True])