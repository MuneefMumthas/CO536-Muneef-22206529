# Name: Muneef Ahamed Mohamed Mumthas
# Student ID: 22206529
# Game Title: Tic Tac Toe

# game.py - This file is used to store the Game class which is used to create the game object and to implement the game logic.

# Importing pygame
import pygame

# Importing the required files
from board import Board 
from ai import AI
from constants import *
import config

#Game Class
class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.running = True
        self.game_mode = "pvp"
        self.ai_difficulty = "easy"
        self.show_lines()

    #method to draw the lines on the screen
    def show_lines(self):

        #Setting the line colour based on the current theme
        if config.current_theme == "blue":
            Line_Colour = Line_Colour_Steel

        elif config.current_theme == "purple":
            Line_Colour = Line_Colour_Purple

        elif config.current_theme == "red":
            Line_Colour = Line_Colour_Red

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
    #the colour of the cross and circle are constant and not theme based
    def mark_square_in_display(self, row, col):
        if self.player == 1:
            
            #draw cross
            #Decending Line (\)
            start_point_descending_line = (col * Square_Size + 50, row * Square_Size + 50 )
            end_point_descending_line = (col * Square_Size + Square_Size - 50, row * Square_Size + Square_Size - 50)
            pygame.draw.line(screen, (128, 0, 32), start_point_descending_line, end_point_descending_line, 25)
        
            #Ascending Line (/)
            start_point_ascending_line = (col * Square_Size + Square_Size - 50, row * Square_Size + 50)
            end_point_ascending_line = (col * Square_Size + 50, row * Square_Size + Square_Size - 50)
            pygame.draw.line(screen, (128, 0, 32), start_point_ascending_line, end_point_ascending_line, 25)

        elif self.player == 2:
            
            #draw circle
            Radius = Square_Size // 2 * 0.8
            center = (col * Square_Size + Square_Size // 2, row * Square_Size + Square_Size // 2)
            pygame.draw.circle(screen, (0, 0, 128), center, Radius, 25)

    def is_game_over(self):
        # Checking if there is a winner
        winner = self.board.check_winner(show_winner=True)

        if winner != 0:
            pygame.display.update()  # Update display to show the win line
            #time.sleep(1.5)  # This is replaced with await asyncio.sleep(1.5) in main.py
            return True
        
        # Check if the board is full
        if self.board.is_board_full():
            draw_sound.play()
            pygame.display.update()
            #time.sleep(1.5) # This is replaced with await asyncio.sleep(1.5) in main.py
            return True
        return False
    
    def restart(self):
        
        #Setting the background colour based on the current theme
        if config.current_theme == "blue":
            bg_colour = Light_Blue

        elif config.current_theme == "purple":
            bg_colour = Light_Purple

        elif config.current_theme == "red":
            bg_colour = Light_Red

        screen.fill(bg_colour)
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.running = True
        self.show_lines()


        # setting the game mode and difficulty based on current mode and difficulty.
        if self.game_mode == "ai_game":
            self.game_mode = "ai_game"

        else:
            self.game_mode = "pvp"

        if self.ai_difficulty == "impossible":
            self.ai.difficulty = "impossible"

        elif self.ai_difficulty == "easy":
            self.ai.difficulty = "easy"

        elif self.ai_difficulty == "medium":
            self.ai.difficulty = "medium"
    
    # method to display the winner of the game
    def display_winner(self):
        winner = self.board.check_winner()
        if winner == 1 and self.game_mode == "pvp":
            text = font.render("Player 1 Wins!", True, (0, 0, 0))
            
        elif winner == 2 and self.game_mode == "pvp":
            text = font.render("Player 2 Wins!", True, (0, 0, 0))

        elif winner == 1 and self.game_mode == "ai_game":
            text = font.render("Player Wins!", True, (0, 0, 0))
        
        elif winner == 2 and self.game_mode == "ai_game":
            text = font.render("AI Wins!", True, (0, 0, 0))

        elif winner == 0:
            text = font.render("It's a Draw!", True, (0, 0, 0))
        
        screen.blit(text, (Width // 2 - text.get_width() // 2, Height // 2 - text.get_height() // 2 - 150))
    
    # method to display current game mode and difficulty
    def display_game_mode(self):
        if self.game_mode == "pvp":
            game_mode_text = font.render("Player vs Player", True, (0, 0, 0))
        
        elif self.game_mode == "ai_game":

            game_mode_text = font.render("Player vs Computer", True, (0, 0, 0))

            if self.ai_difficulty == "easy":
                difficulty_text = font.render("Difficulty: Easy", True, (0, 0, 0))
        
            elif self.ai_difficulty == "medium":
                difficulty_text = font.render("Difficulty: Medium", True, (0, 0, 0))

            elif self.ai_difficulty == "impossible":
                difficulty_text = font.render("Difficulty: Impossible", True, (0, 0, 0))

            screen.blit(difficulty_text, (Width // 2 - difficulty_text.get_width() // 2, Height // 2 - difficulty_text.get_height() // 2 - 350))
        
        screen.blit(game_mode_text, (Width // 2 - game_mode_text.get_width() // 2, Height // 2 - game_mode_text.get_height() // 2 - 400))

        
