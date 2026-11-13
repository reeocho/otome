# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define ishe = Character("Ishe")
define steak = Character("Steak")
define clum = Character("Clum")
define main_speaker_pos = Position(xalign=0.7, yalign=0.53)
define player = Character("[playername]")
transform fill_screen:
    xalign 0.5
    yalign 0.5
    size (1280, 720)

transform slow_zoom_in:
    xalign 0.5
    yalign 0.5
    size (1280, 720)
    zoom 1.0
    linear 5.0 zoom 1.5


define ishe_love = 0
define steak_love = 0
define uranus_love = 0
define clum_love = 0

# Game start

label start:
    scene school_gate at fill_screen

    narrator "You stand in front of your new school…"
    narrator "It is the middle of the school year and you are ready for a fresh start."

    scene hallway at fill_screen with Fade(0.5, 0.5, 0.5)
    narrator "You look down at your student ID that arrived in the mail yesterday... best to check your information."
    python:
        playername = renpy.input("Name", length=32)
        playername = playername.strip()
    narrator "[player]... correct"
    narrator "Age... 18... Correct."
    player "They told me that I should head to the Headmaster’s office and get my timetable for today."
    player "I should probably head there now…"
    scene hallway at slow_zoom_in
    narrator "You walk through packed corridors uninterrupted until you reach the door labelled with a shiny plaque, “Headmaster”."
    menu:
        "Knock then open the door":
            pass
    scene club_room at fill_screen with Fade(0.5, 0.5, 0.5)
    "Headmaster" "Nice to meet you, you are [player], I presume… Welcome to USB!"
    narrator "He shuffles around some papers nervously."
    "Headmaster" "Here is your timetable… ahem, have fun in class."
    narrator "You look down at your timetable. It seems like your homeroom class is…"
    menu:
        "1G":
            player "My first class is English..."
            define playerclass = "G"
            jump english_1
        "1A":
            player "My first class is Housekeeping..."
            define playerclass = "A"
            jump housekeeping_1
        "1Y":
            player "My first class is Maths..."
            define playerclass = "Y"
            jump maths_1

    # Class 1

    label english_1:
        scene hallway at fill_screen with Fade(0.5, 0.5, 0.5)
        scene hallway at slow_zoom_in
        narrator "You walk quickly to the English rooms just as the bell signals first period."
        scene class_room at fill_screen with Fade(0.5, 0.5, 0.5)
        jump recess


    label housekeeping_1:
        scene hallway at fill_screen with Fade(0.5, 0.5, 0.5)
        scene hallway at slow_zoom_in
        narrator "You walk quickly to the Housekeeping rooms just as the bell signals first period."
        jump recess


    label maths_1:
        scene hallway at fill_screen with Fade(0.5, 0.5, 0.5)
        scene hallway at slow_zoom_in
        narrator "You walk quickly to the Maths rooms just as the bell signals first period."
        jump recess

    label recess:
    # Game end
    return
