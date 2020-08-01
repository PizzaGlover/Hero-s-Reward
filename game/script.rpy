#init -1 python:
    #config.screen_width = 800
    #config.screen_height = 600

    
init python:
    def force_integer_multiplier(width, height):
        multiplier = min(width / config.screen_width, height / config.screen_height)
        multiplier = max(int(multiplier), 1)
        return (multiplier * config.screen_width, multiplier * config.screen_height)

## use integer scaling only
define config.adjust_view_size = force_integer_multiplier

## actual graphics resolution
define config.screen_width = 200
define config.screen_height = 150

## clamp rendering to integer values
define config.nearest_neighbor = True

## render in game resolution not the desktop resolution
## (this had the side-effect of doing the same to the debug tools)
## (scaling is still in the native desktop resolution, there isn't a workaround for that)
define config.use_drawable_resolution = True
    
    
    
    #config.use_drawable_resolution = False
    #config.nearest_neighbor = True
    #config.screen_width = 200
    #config.screen_height = 150
    #config.adjust_view_size = (800,600)

    
     


init:
    image ctc_blink:
        "clickthing01.png"
        linear 0.5 alpha 1.0
        "clickthing02.png"
        linear 0.5 alpha 1.0
        repeat
    

    define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
    define s = Character("Slime", image = "slime", ctc = "ctc_blink", show_two_window = True, who_ypos=5, who_xpos=16, ctc_position = "nestled")
    
    define whiteflash = Fade(0.0, 0.0, 0.4, color = "fff")
    
image bg forest = "bg_forest.png"
image bg splash = "bg_splash.png"
image white = "#fff"
image fin = "ending_fin.png"
image herosreward = "reward.png"

image endadventure = "adventure.png"
image endwedding = "wedding.png"

image buttonchoice = "button_choice.png"
image buttonchoice_hover = "button_choice_hover.png"
image buttonsplash = "button_splash.png"
image buttonsplash_hover = "button_splash_hover.png"

image sword = "sword.png"
image slime normal = "slime_normal.png"
image slime meat = "slime_meat.png"
image slime happy = "slime_happy.png"
image slime angry = "slime_angry.png"
image slime surprised = "slime_surprised.png"
image slime eyebrow = "slime_eyebrow.png"
image slime blush = "slime_blush.png"

image slime dick1:
    "slime_dick01.png"
    0.15
    "slime_dick02.png"
    0.2
    "slime_dick03.png"
    0.15
    "slime_dick04.png"
    0.15
    repeat
    
image slime dick2:
    "slime_dick01.png"
    0.1
    "slime_dick02.png"
    0.13
    "slime_dick03.png"
    0.1
    "slime_dick04.png"
    0.1
    repeat

image slime cum:
    "slime_cum01.png"
    0.5
    "slime_cum02.png"
    0.15
    "slime_cum03.png"
    0.5
    "slime_cum04.png"
    0.15
    "slime_cum05.png"
    0.5
    "slime_cum06.png"
    0.15
    "slime_cum07.png"
    0.5
    "slime_cum08.png"
    0.15

image credits:
    Text("* Code & Art *\n\nPizzaGlover\n\n\n\n* Special Thanks *\n\nHoney B\nDieselBrain\n\n\n\nMade with Renpy\n")
    ypos 0.5 yanchor 0.5 xalign 0.5
    #anchor(0.5,0.0)
    #pos(0.5,1.0)
    #linear 4.0 ypos 0.5 yanchor 0.5
    
image click:
    Text("{color=#000}Click to Play{/color}")


#action Preference("display", 4.0)

label splashscreen:
    #$ renpy.set_physical_size((800, 600))
    
    #show logo at position
    #click to continue i guess
    
    show bg forest at Position (xpos=0, ypos=0, xanchor=0, yanchor=0)
    
    show herosreward at Position (xpos= 0.5, ypos= 0.45)
    
    show click at Position (xpos=0.5, ypos= 0.8)
    pause
    
    ####this was for the text version, but it makes a box too...
    #"{size=20}{color=#000}Hero's Reward{/color}{/size}"
    
    hide herosreward
    hide click
    show bg forest:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        linear 2.0 xpos 0 ypos -225  
    $ renpy.pause(2.0,hard=True)

    jump start
    
label start:
    $ renpy.block_rollback()

    $ marry = False
    
    "Fresh off a grand adventure, you find yourself on a sun-dappled forest path."
    
    show slime normal at Position(xpos = .5, ypos = .6)
    
    "Suddenly, you encounter a slime or something!"
    "What do??"

menu:
    
    "Feed the bastard.":
        jump food
        
    "Kill it!":
        jump dead
        
label food:
    
    show slime meat
    "It graciously accepts your food."
    
    jump repay
    
label dead:
    show slime surprised
    with vpunch
    show slime angry
    show sword at Position (xpos=117,ypos=68)
    with whiteflash
    "Turns out it's invulnerable! Good job, asshat."
    "It kills you instead."
    scene black with vpunch
    centered "Bad End."
    
    jump splashscreen
    
label repay:
    
    show slime happy
    s "Thanks for the grub, Great Hero!"
    s "How can I ever repay your kindness, etc."
    
menu:
    
    "Join my party!":
        jump dick
        
    "Marry me?":
        $ marry = True
        jump dick
        
label dick:
    s surprised "Are you serious? Heck no!"
    s blush "Why don't I just, like, suck your dick and we'll call it even?"
    
menu:
    "Heck yes!":
        jump yesDick
    "Uh, no thanks...":
        jump noDick
        
label noDick:
    s angry "Wow. Really?"
    s "And here I am, trying to be a good trope and repay your kindness..."
    s "Prick."
    hide slime
    "The slime wobbles away."
    scene black
    centered "Boring End."
    
    jump splashscreen
    
label yesDick:
    show slime normal
    s "Alright then, off with the pants!"
    
    show slime dick1 at Position (xpos=0.5,ypos=130)
    pause
    
    show slime dick2
    pause
    
    show slime cum
    $ renpy.pause(1.6, hard=True)
    
    scene white
    with Dissolve(3.5)
    
    $ renpy.pause(1.0, hard=True)
    if marry:
        show endwedding with Dissolve(3.5)
                
    else:
        show endadventure with Dissolve(3.5)

    hide window
    show fin:
        alpha 0.0
        xalign .7 yalign .8
        linear 1.5 alpha 1.0 xalign.9
    pause
    jump credits
    
label credits:
    scene black with dissolve
    show credits with dissolve
    $ renpy.pause(1.5, hard=True)
    pause

    
    jump splashscreen
