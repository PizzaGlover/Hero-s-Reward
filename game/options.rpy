## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    
    config.windows_icon = "heros_reward_icon.png"
    config.window_icon = "heros_reward_icon.png"


    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = False

    ## These control the width and height of the screen.

    #config.screen_width = 200
    #config.screen_height = 150
    #config.adjust_view_size = (800, 600)

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Hero's Reward"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "Hero's Reward"
    config.version = "1.14"

    #########################################
    # Themes

    ## We then want to call a theme function. theme.roundrect is
    ## a theme that features the use of rounded rectangles.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.marker(
        ## Theme: Marker
        ## Color scheme: Swamp Critter

        ## The color of an idle widget face.
        widget = "#753D00",

        ## The color of a focused widget face.
        widget_hover = "#B19A48",

        ## The color of the text in a widget.
        widget_text = "#CCCAC2",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#ffffff",

        ## The color of a disabled widget face.
        disabled = "#A2521D",

        ## The color of disabled widget text.
        disabled_text = "#753D00",

        ## The color of informational labels.
        label = "#ffffff",

        ## The color of a frame containing widgets.
        frame = "#fff",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "bg splash",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#B09D5A",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = "window_dialogue.png"

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 19
    style.window.right_padding = 18
    style.window.top_padding = 10
    style.window.bottom_padding = 10

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 57
    style.window.ymaximum = 57
    style.say_who_window.xmaximum = 42
    style.say_who_window.ymaximum = 19
    
    ## code for character name window stuff
    
    style.say_who_window.background = "window_name.png"
    
    style.say_who_window.xalign = 0.0
    style.say_who_window.yalign = 0.0
    
    style.say_who_window.xpos = 0 
    style.say_who_window.ypos = -1
    
    style.say_who_window.left_padding = 0
    style.say_who_window.top_padding = 0
    style.say_who_window.right_padding = 0
    style.say_who_window.bottom_padding = 0
    
    style.say_who_window.xminimum = 200 
    style.say_who_window.yminimum = 19 
    
    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    style.default.font = "pixelmix.ttf"

    ## The default size of text.

    style.default.size = 8

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.
    
    style.default.antialias = False


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = False

    ## Set this to False if the game does not have any music.

    config.has_music = False

    ## Set this to True if the game has voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    # config.main_menu_music = "main_menu_theme.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = None

    ## Used between screens of the game menu.
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = None

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = None

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = None

    ## Used when a game is loaded.
    config.after_load_transition = None

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = dissolve

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = dissolve

    ## Used when yesno is shown.
    config.enter_yesno_transition = None

    ## Used when the yesno is hidden.
    config.exit_yesno_transition = None

    ## Used when entering a replay
    config.enter_replay_transition = None

    ## Used when exiting a replay
    config.exit_replay_transition = None

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = None

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
python early:
    config.save_directory = "Forest Encounter-1456797750"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    config.gl_resize = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 20

    ## The default auto-forward time setting.

    config.default_afm_time = 0

    #########################################
    ## More customizations can go here.

    #_preferences.Display = 4.0


    ##Code for customizing in-game menu choices. I guess.

    style.menu_choice_button.background = Frame("buttonchoice")
    style.menu_choice_button.hover_background = Frame("buttonchoice_hover")
    style.menu_choice_button.yminimum = 20
    style.menu_choice_button.ymaximum = 20

    ##Code for customizing the text on the buttons what what
    style.menu_choice.color = "#fff"
    style.menu_choice.size = 8
    
    #code for the splash screen buttons and text
    style.mm_button.background = Frame("buttonsplash")
    style.mm_button.hover_background = Frame("buttonsplash_hover")
    
    style.mm_button_text.color = "#fff"
    style.mm_button_text.size = 8
    
    #action Preference("display", 4.0)
    
    
    ########################
    ## build settings I guess??
    
    build.directory_name = "heros_reward"
    build.executable_name = "heros_reward"
    
     ## Classify files as None to exclude them from the built distributions.

    build.classify('**.rpy', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.txt', None)
    
    ## To archive files, classify them as 'archive'.
    
    build.classify('**/**.ico', 'archive')
    build.classify('**/**.icns', 'archive')
    build.classify('**/**.json', 'archive')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogg', 'archive')
    