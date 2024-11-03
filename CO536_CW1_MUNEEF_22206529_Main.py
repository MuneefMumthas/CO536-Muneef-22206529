import sys
import pygame
import numpy as np

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
Line_Colour_Purple = (189, 120, 196)
Line_Colour_Red = (255, 153, 153)

#Background Colours
Light_Purple = (207, 196, 230)
Light_Red = (250, 198, 206)

Line_Colour = Line_Colour_Purple
bg_colour = Light_Purple

#initialising pygame and setting up the screen
pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("TIC TAC TOE  (CO536_CW1_Muneef_22206529)")
screen.fill(bg_colour)

#initialising the buttons
play_button = pygame.Rect(Width // 2 - 100, Height // 2 - 75, 200, 75)
settings_button = pygame.Rect(Width // 2 - 100, Height // 2 + 37.5, 200, 75)

pvplayer_button = pygame.Rect(Width // 2 - 150, Height // 2 - 150, 300, 75)
pvcomputer_button = pygame.Rect(Width // 2 - 150, Height // 2 - 37.5, 300, 75)
back_button_game_mode_menu = pygame.Rect(Width // 2 - 100, Height // 2 + 75, 200, 75)

bg_colour_button = pygame.Rect(Width // 2 - 100, Height // 2 - 75, 200, 75)
back_button_settings_menu = pygame.Rect(Width // 2 - 100, Height // 2 + 37.5, 200, 75)

#font for button text
font = pygame.font.Font(None, 36)

#game state
current_screen = "main_menu"

#Method to Create the main menu
def main_menu():
    screen.fill(bg_colour)

    #Play button
    pygame.draw.rect(screen, Black, play_button)
    play_text = font.render("Play", True, White)
    screen.blit(play_text, (play_button.centerx - play_text.get_width() // 2, play_button.centery - play_text.get_height() // 2))

    #Settings button
    pygame.draw.rect(screen, Black, settings_button)
    settings_text = font.render("Settings", True, White)
    screen.blit(settings_text, (settings_button.centerx - settings_text.get_width() // 2, settings_button.centery - settings_text.get_height() // 2))

#Method to Create the game mode selection menu
def game_mode_menu():
    screen.fill(bg_colour)

    #Player vs Player button
    pygame.draw.rect(screen, Black, pvplayer_button)
    pvplayer_text = font.render("Player vs Player", True, White)
    screen.blit(pvplayer_text, (pvplayer_button.centerx - pvplayer_text.get_width() // 2, pvplayer_button.centery - pvplayer_text.get_height() // 2))

    #Player vs Computer button
    pygame.draw.rect(screen, Black, pvcomputer_button)
    pvcomputer_text = font.render("Player vs Computer", True, White)
    screen.blit(pvcomputer_text, (pvcomputer_button.centerx - pvcomputer_text.get_width() // 2, pvcomputer_button.centery - pvcomputer_text.get_height() // 2))

    #Back button game mode menu
    pygame.draw.rect(screen, Black, back_button_game_mode_menu)
    back_text = font.render("Back", True, White)
    screen.blit(back_text, (back_button_game_mode_menu.centerx - back_text.get_width() // 2, back_button_game_mode_menu.centery - back_text.get_height() // 2))

#Method to Create the settings menu
def settings_menu():
    screen.fill(bg_colour)

    #Background  button
    pygame.draw.rect(screen, Black, bg_colour_button)
    bg_colour_text = font.render("Switch Colour", True, White)
    screen.blit(bg_colour_text, (bg_colour_button.centerx - bg_colour_text.get_width() // 2, bg_colour_button.centery - bg_colour_text.get_height() // 2))

    #Back button settings menu
    pygame.draw.rect(screen, Black, back_button_settings_menu)
    back_button_text = font.render("Back", True, White)
    screen.blit(back_button_text, (back_button_settings_menu.centerx - back_button_text.get_width() // 2, back_button_settings_menu.centery - back_button_text.get_height() // 2))

#Board Class
class Board:
    def __init__(self):

        #creating a 3x3 grid with numpy
        self.squares = np.zeros((Rows, Columns))
        print(self.squares)

    #method to mark the square with the player
    def mark_square(self, row, col, player):
        self.squares[row][col] = player

    #method to check if the square is empty
    def is_square_empty(self, row, col):
        return self.squares[row][col] == 0

#Game Class
class Game:
    def __init__(self):
        self.board = Board()
        self.player = 1
        self.show_lines()

    #method to draw the lines on the screen
    def show_lines(self):
        #Horizontal Lines
        pygame.draw.line(screen, Line_Colour, (0, Square_Size), (Width, Square_Size), 15)
        pygame.draw.line(screen, Line_Colour, (0, Height - Square_Size), (Width, Height - Square_Size), 15)

        #Vertical Lines
        pygame.draw.line(screen, Line_Colour, (Square_Size, 0), (Square_Size, Height), 15)
        pygame.draw.line(screen, Line_Colour, (Width - Square_Size, 0), (Width - Square_Size, Height), 15)

    #method to switch the player after each turn
    def switch_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    #method to draw and mark the square in the display 
    #with either cross or circle based on the player
    def mark_square_in_display(self, row, col):
        if self.player == 1:
            
            #draw cross
            #Decending Line (\)
            start_point_descending_line = (col * Square_Size + 50, row * Square_Size + 50 )
            end_point_descending_line = (col * Square_Size + Square_Size - 50, row * Square_Size + Square_Size - 50)
            pygame.draw.line(screen, Black, start_point_descending_line, end_point_descending_line, 25)
        
            #Ascending Line (/)
            start_point_ascending_line = (col * Square_Size + Square_Size - 50, row * Square_Size + 50)
            end_point_ascending_line = (col * Square_Size + 50, row * Square_Size + Square_Size - 50)
            pygame.draw.line(screen, Black, start_point_ascending_line, end_point_ascending_line, 25)

        elif self.player == 2:
            
            #draw circle
            Radius = Square_Size // 2 * 0.8
            center = (col * Square_Size + Square_Size // 2, row * Square_Size + Square_Size // 2)
            pygame.draw.circle(screen, Black, center, Radius, 15)

#main method for the game
def main():
    global current_screen, bg_colour, Line_Colour
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #mouse click event
            elif event.type == pygame.MOUSEBUTTONUP:
                #left click only
                if event.button == 1:
                
                    #Main Menu
                    if current_screen == "main_menu":
                    
                        if play_button.collidepoint(event.pos):
                            current_screen = "game_mode_selection"

                        elif settings_button.collidepoint(event.pos):
                            current_screen = "settings"

                    #Game Mode Menu
                    elif current_screen == "game_mode_selection":

                        if pvplayer_button.collidepoint(event.pos):
                            
                            #creating the game layout
                            current_screen = "game"
                            screen.fill(bg_colour)
                            game = Game()    
                    
                        elif pvcomputer_button.collidepoint(event.pos):
                        
                            print("Player vs Computer")

                        elif back_button_game_mode_menu.collidepoint(event.pos):
                            current_screen = "main_menu"
                    
                    #Settings Menu
                    elif current_screen == "settings":
                        #Switching Background Colour
                        if bg_colour_button.collidepoint(event.pos):
                            if bg_colour == Light_Purple:
                                bg_colour = Light_Red
                                Line_Colour = Line_Colour_Red

                            elif bg_colour == Light_Red:
                                bg_colour = Light_Purple
                                Line_Colour = Line_Colour_Purple
    
                        elif back_button_settings_menu.collidepoint(event.pos):
                            current_screen = "main_menu"

                    #Game        
                    elif current_screen == "game":

                        #getting the row and column of the square clicked
                        pos = event.pos
                        row = pos[1] // Square_Size #y axis
                        col = pos[0] // Square_Size #x axis
                        
                        #allowing to mark the square only if it is empty
                        if game.board.is_square_empty(row, col):
                            #marking the square with the player and updating the board (numpy grid)
                            game.board.mark_square(row, col, game.player)
                            game.mark_square_in_display(row, col)
                            game.switch_player()
                            print(game.board.squares)
        
        if current_screen == "main_menu":
            main_menu()
        elif current_screen == "game_mode_selection":
            game_mode_menu()
        elif current_screen == "settings":
            settings_menu()

        pygame.display.update()

main()