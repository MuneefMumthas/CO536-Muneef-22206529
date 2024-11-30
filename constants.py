import pygame

#initialising the variables
Width = 900
Height = 900

Rows = 3
Columns = 3

Square_Size = Width // Columns

#defining the colours for settings
Black = (0, 0, 0)
White = (255, 255, 255)

#Line Colours
Line_Colour_Steel = (112, 128, 144)
Line_Colour_Purple = (189, 120, 196)
Line_Colour_Red = (255, 153, 153)

#Background Colours
Light_Blue = (176, 224, 230)
Light_Purple = (207, 196, 230)
Light_Red = (250, 198, 206)

Line_Colour = Line_Colour_Steel
bg_colour = Light_Blue


#font for button text
pygame.font.init()
font = pygame.font.Font(None, 36)

#Initialising the sounds
pygame.mixer.init()
mark_sound = pygame.mixer.Sound("Sounds/mark.wav")
win_sound = pygame.mixer.Sound("Sounds/win.wav")
click_sound = pygame.mixer.Sound("Sounds/click.wav")
click2_sound = pygame.mixer.Sound("Sounds/click2.wav")
draw_sound = pygame.mixer.Sound("Sounds/draw.wav")

#initialising pygame and setting up the screen
pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("TIC TAC TOE  (CO536_CW1_Muneef_22206529)")
screen.fill(bg_colour)