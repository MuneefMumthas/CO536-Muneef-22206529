import sys
import pygame
import numpy as np
import time
import random
import copy

from board import Board 
from ai import AI
from constants import *

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
            time.sleep(1.5)  # Pause for 1.5 seconds
            return True
        
        # Check if the board is full
        if self.board.is_board_full():
            draw_sound.play()
            pygame.display.update()
            time.sleep(1.5) # Pause for 1.5 seconds
            return True
        return False
    
    def restart(self):

        screen.fill(bg_colour)
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.running = True
        self.show_lines()


        if self.game_mode == "ai_game":
            self.game_mode = "ai_game"

        else:
            self.game_mode = "pvp"

        if self.ai_difficulty == "hard":
            self.ai.difficulty = "hard"

        elif self.ai_difficulty == "easy":
            self.ai.difficulty = "easy"

        elif self.ai_difficulty == "medium":
            self.ai.difficulty = "medium"
    
    # method to display the winner
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
    