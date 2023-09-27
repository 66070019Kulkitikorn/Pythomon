# Declare characters used by this game. The color argument colorizes the
# name of the character.
# define Hiyajou = Character("Professor Hiyajou")

# The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show Professor Hiyajou

#     # These display lines of dialogue.
#     Hiyajou "You've created a new Ren'Py game."
#     Hiyajou "Once you add a story, pictures, and music, you can release it to the world!"
    
#     # This ends the game.
label start:
    scene bg room
    show Professor Hiyajou
    Hiyajou "Welcome LABMEM:011"
    Hiyajou "To the Simulation World!"
    Hiyajou "You can call me Professor Hiyajou"
    show Professor Hiyajou confused
    Hiyajou "Wait what the fuc"
    show Professor Hiyajou nice
    Hiyajou "I didn't understand how to make combat system good i guess?"

#   #Insert name here!
    Hiyajou "So... What's your name?"
    $ povname = renpy.input("What's your name?", length = 15)

    MC "Uh... My name is [povname]"
    Hiyajou "I see....[povname]. You ARE the choosen one!!!"
    Hiyajou "Thank for testing i guess?"
    

    return
