import sys
import pygame
import numpy as np
import time
import random
import copy

from constants import *

#Board Class
class Board:
    def __init__(self):

        #creating a 3x3 grid with numpy
        self.squares = np.zeros((Rows, Columns))
        print(self.squares)

        #variable to check the number of marked squares
        self.marked_squares = 0
        
    #method to mark the square with the player
    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1

    #method to check if the square is empty
    def is_square_empty(self, row, col):
        return self.squares[row][col] == 0

    #method to get the empty squares in the board (numpy grid - for AI)
    def get_empty_squares(self):
        available_empty_squares = []
        for row in range(Rows):
            for col in range(Columns):
                if self.is_square_empty(row, col):
                    available_empty_squares.append((row, col))
        
        return available_empty_squares

    #method to check if the board is full
    def is_board_full(self):
        return self.marked_squares == 9
    
    #method to check if the board is emtry
    def is_board_empty(self):
        return self.marked_squares == 0
    
    #method to check if the player has won or to get the final state of the game. Also returns the winner
    def check_winner(self, show_winner = False):

        #vertical Check
        for col in range(Columns):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show_winner:
                    start_point = (col * Square_Size + Square_Size // 2, 20)
                    end_point = (col * Square_Size + Square_Size // 2, Height - 20)
                    pygame.draw.line(screen, (0, 0, 0), start_point, end_point, 15)
                    win_sound.play()
                return self.squares[0][col]
        
        #Horizontal Check
        for row in range(Rows):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show_winner:
                    start_point = (20, row * Square_Size + Square_Size // 2)
                    end_point = (Width - 20, row * Square_Size + Square_Size // 2)
                    pygame.draw.line(screen, (0, 0, 0), start_point, end_point, 15)
                    win_sound.play()
                return self.squares[row][0]
            
        #Descending diagonal Check (\)
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show_winner:
                start_point = (20, 20)
                end_point = (Width - 20, Height - 20)
                pygame.draw.line(screen, (0, 0, 0), start_point, end_point, 15) 
                win_sound.play()
            return self.squares[0][0]
        
        #Ascending Diagonal (/)
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show_winner:
                start_point = (20, Height - 20)
                end_point = (Width - 20, 20)
                pygame.draw.line(screen, (0, 0, 0), start_point, end_point, 15)
                win_sound.play()
            return self.squares[2][0]

        #If there is no win yet
        return 0
    