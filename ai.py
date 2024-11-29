import sys
import pygame
import numpy as np
import time
import random
import copy

#AI class
class AI:
    def __init__(self):
        self.difficulty = "easy"
        self.player = 2
        self.ai_mode = random.choice(["random", "minimax"])

        #Random AI - Method to select a random empty square
    def random_ai(self, board):
        empty_squares = board.get_empty_squares()
        Chosen_Index = random.randrange(0, len(empty_squares))

        return empty_squares[Chosen_Index]
    
        #Minimax AI - Method to select the best move based on the minimax algorithm
    def minimax(self, board, maximizing):
        #Returns the evaluation and the best move
        
        #Base case to check the final state of the game
        case = board.check_winner()

        # AI (player 2) wins
        if case == 2:
            return 1, None #
        
        # player 1 wins
        elif case == 1:
            return -1, None
        
        # Draw
        elif board.is_board_full():
            return 0, None
        
        #Maximizing player (AI)
        if maximizing:
            max_eval = -1000
            best_move = None
            empty_squares = board.get_empty_squares()

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                eval = self.minimax(temp_board, False)[0]

                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
                
            return max_eval, best_move

        #Minimizing player - player 1
        elif not maximizing:
            min_eval = 1000
            best_move = None
            empty_squares = board.get_empty_squares()

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 1)
                eval = self.minimax(temp_board, True)[0]

                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
            
            return min_eval, best_move

    def evaluate(self, main_board):

        #Easy Mode - Random Ai
        if self.difficulty == "easy":
            eval = "Random"
            move = self.random_ai(main_board)

        elif self.difficulty == "impossible":
            eval, move = self.minimax(main_board, True)

        elif self.difficulty == "medium":
            #random choice between random and minimax at the start and then switch between them after each turn.
            if self.ai_mode == "random":
                eval = "Random"
                move = self.random_ai(main_board)
                self.ai_mode = "minimax"

            elif self.ai_mode == "minimax":
                eval, move = self.minimax(main_board, True)
                self.ai_mode = "random"
            
        
        #printing the move and evaluation for debugging
        print(f"AI chose to mark square {move} with evaluation {eval}")
  
        return move
    