import sys
import pygame
import numpy as np
import time
import random
import copy
import asyncio

from constants import *
from game import Game
import config

game = Game()



#initialising the buttons
#main menu buttons
play_button = pygame.Rect(Width // 2 - 100, Height // 2 - 75, 200, 75)
settings_button = pygame.Rect(Width // 2 - 100, Height // 2 + 37.5, 200, 75)

#game mode selection buttons
pvplayer_button = pygame.Rect(Width // 2 - 150, Height // 2 - 150, 300, 75)
pvcomputer_button = pygame.Rect(Width // 2 - 150, Height // 2 - 37.5, 300, 75)
back_button_game_mode_menu = pygame.Rect(Width // 2 - 100, Height // 2 + 75, 200, 75)

#settings buttons
bg_colour_button = pygame.Rect(Width // 2 - 100, Height // 2 - 75, 200, 75)
back_button_settings_menu = pygame.Rect(Width // 2 - 100, Height // 2 + 37.5, 200, 75)

#game over buttons
restart_button = pygame.Rect(Width // 2 - 100, Height // 2 - 75, 200, 75)
main_menu_button = pygame.Rect(Width // 2 - 100, Height // 2 + 37.5, 200, 75)

#difficulty selection buttons
easy_button = pygame.Rect(Width // 2 - 325, Height // 2 - 56.25, 200, 75)
medium_button = pygame.Rect(Width // 2 - 100, Height // 2 - 56.25, 200, 75)
impossible_button = pygame.Rect(Width // 2 + 125, Height // 2 - 56.25, 200, 75)
back_button_difficulty = pygame.Rect(Width // 2 - 100, Height // 2 + 75, 200, 75)

#game state
current_screen = "main_menu"

#Method to draw buttons to the screen
def draw_button(button, text, color=Black, text_color=White):
    pygame.draw.rect(screen, color, button)
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (button.centerx - text_surface.get_width() // 2, button.centery - text_surface.get_height() // 2))

#Methods to create game screens

#Method to create the main menu
def main_menu():
    screen.fill(bg_colour)
    draw_button(play_button, "Play")
    draw_button(settings_button, "Settings")

#Method to create the game mode selection menu
def game_mode_menu():
    screen.fill(bg_colour)
    draw_button(pvplayer_button, "Player vs Player")
    draw_button(pvcomputer_button, "Player vs Computer")
    draw_button(back_button_game_mode_menu, "Back")

#Method to create the settings menu
def settings_menu():
    screen.fill(bg_colour)
    draw_button(bg_colour_button, "Switch Colour")
    draw_button(back_button_settings_menu, "Back")

#Method to create the game over screen
def game_over():
    screen.fill(bg_colour)
    draw_button(restart_button, "Restart")
    draw_button(main_menu_button, "Main Menu")

#Method to create difficulty selection menu for player vs computer
def difficulty_selection_menu():
    screen.fill(bg_colour)
    draw_button(easy_button, "Easy")
    draw_button(medium_button, "Medium")
    draw_button(impossible_button, "Impossible")
    draw_button(back_button_difficulty, "Back")




#main method for the game
#def main():
    

async def main():   
        global current_screen, bg_colour, Line_Colour     
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    #mouse click event
                if event.type == pygame.MOUSEBUTTONUP:
                    
                    #left click only
                    if event.button == 1:

                        #Main Menu
                        if current_screen == "main_menu":
                        
                            if play_button.collidepoint(event.pos):
                                current_screen = "game_mode_selection"
                                click_sound.play()

                            elif settings_button.collidepoint(event.pos):
                                current_screen = "settings"
                                click_sound.play()

                        #Game Mode Menu Screen
                        elif current_screen == "game_mode_selection":

                            if pvplayer_button.collidepoint(event.pos):
                                
                                #creating the game layout
                                current_screen = "game"
                                click_sound.play()
                                screen.fill(bg_colour)    
                                game.game_mode = "pvp"
                                game.restart()
                        
                            elif pvcomputer_button.collidepoint(event.pos):
                            
                                current_screen = "difficulty_selection"
                                click_sound.play()

                            elif back_button_game_mode_menu.collidepoint(event.pos):
                                click2_sound.play()
                                current_screen = "main_menu"
                        
                        #Difficulty Selection Menu Screen
                        elif current_screen == "difficulty_selection":
                            
                            if easy_button.collidepoint(event.pos):
                                click_sound.play()
                                current_screen = "game"
                                screen.fill(bg_colour)
                                game.game_mode = "ai_game"
                                game.restart()
                                game.ai.difficulty = "easy"
                                game.ai_difficulty = "easy"

                            elif medium_button.collidepoint(event.pos):
                                click_sound.play()
                                current_screen = "game"
                                screen.fill(bg_colour)
                                game.game_mode = "ai_game"
                                game.restart()
                                game.ai.difficulty = "medium"
                                game.ai_difficulty = "medium"

                            elif impossible_button.collidepoint(event.pos):    
                                click_sound.play()
                                current_screen = "game"
                                screen.fill(bg_colour)
                                game.game_mode = "ai_game"
                                game.restart()
                                game.ai.difficulty = "impossible"
                                game.ai_difficulty = "impossible"

                            elif back_button_difficulty.collidepoint(event.pos):
                                click2_sound.play()
                                current_screen = "game_mode_selection"
                                
                        #Settings Menu Screen
                        elif current_screen == "settings":
                            #Switching Background Colour
                            if bg_colour_button.collidepoint(event.pos):
                                click_sound.play()
                                if bg_colour == Light_Purple:
                                    bg_colour = Light_Red
                                    Line_Colour = Line_Colour_Red
                                    config.current_theme = "red"

                                elif bg_colour == Light_Red:
                                    bg_colour = Light_Purple
                                    Line_Colour = Line_Colour_Purple
                                    config.current_theme = "purple"
        
                            elif back_button_settings_menu.collidepoint(event.pos):
                                click2_sound.play()
                                current_screen = "main_menu"

                        #Player input for Game Screen in pvp mode      
                        elif current_screen == "game" and game.game_mode == "pvp":
                            #getting the row and column of the square clicked
                            pos = event.pos
                            row = pos[1] // Square_Size #y axis
                            col = pos[0] // Square_Size #x axis
                            
                            if 0 <= row < 3 and 0 <= col < 3:
                                #allowing to mark the square only if it is empty
                                if game.board.is_square_empty(row, col):
                                    #marking the square with the player and updating the board (numpy grid)
                                    game.board.mark_square(row, col, game.player)
                                    game.mark_square_in_display(row, col)
                                    mark_sound.play()
                                    game.switch_player()
                                    print(game.board.squares)

                                    #checking if the game is over
                                    if game.is_game_over():
                                        await asyncio.sleep(1.5)
                                        game.running = False
                                        current_screen = "game_over"
                        
                        #Player input for Game Screen in ai mode 
                        elif current_screen == "game" and game.game_mode == "ai_game" and game.player == 1:

                            #getting the row and column of the square clicked
                            pos = event.pos
                            row = pos[1] // Square_Size #y axis
                            col = pos[0] // Square_Size #x axis
                            
                            if 0 <= row < 3 and 0 <= col < 3:
                                #allowing to mark the square only if it is empty
                                if game.board.is_square_empty(row, col):
                                    #marking the square with the player and updating the board (numpy grid)
                                    game.board.mark_square(row, col, game.player)
                                    game.mark_square_in_display(row, col)
                                    mark_sound.play()
                                    game.switch_player()
                                    print(game.board.squares)
                                    

                                    #checking if the game is over
                                    if game.is_game_over():
                                        game.running = False
                                        await asyncio.sleep(1.5)
                                        current_screen = "game_over"
                
                        #Game Over Screen
                        elif current_screen == "game_over":

                            if restart_button.collidepoint(event.pos):
                                click_sound.play()
                                current_screen = "game"
                                game.restart() 

                            elif main_menu_button.collidepoint(event.pos):
                                click2_sound.play()
                                current_screen = "main_menu"
            
            if current_screen == "main_menu":
                main_menu()
            elif current_screen == "game_mode_selection":
                game_mode_menu()
            elif current_screen == "settings":
                settings_menu()
            elif current_screen == "game_over":
                game_over()
                game.display_winner()
            elif current_screen == "difficulty_selection":
                difficulty_selection_menu()

            #AI's turn in ai mode
            elif current_screen == "game" and game.game_mode == "ai_game" and game.player == game.ai.player:
                

                pygame.display.update()
                await asyncio.sleep(0.5)
                pygame.display.update()
                row, col = game.ai.evaluate(game.board)

                game.board.mark_square(row, col, game.ai.player)
                game.mark_square_in_display(row, col)
                mark_sound.play()
                game.switch_player()
                print(game.board.squares)

                #checking if the game is over
                if game.is_game_over():
                    game.running = False
                    await asyncio.sleep(1.5)
                    current_screen = "game_over"


            pygame.display.update()
            await asyncio.sleep(0)

asyncio.run(main())