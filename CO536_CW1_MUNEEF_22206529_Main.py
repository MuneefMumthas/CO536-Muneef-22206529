import sys
import pygame
import numpy as np
import time
import random
import copy

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
easy_button = pygame.Rect(Width // 2 - 225, Height // 2 - 56.25, 200, 75)
hard_button = pygame.Rect(Width // 2 + 25, Height // 2 - 56.25, 200, 75)
back_button_difficulty = pygame.Rect(Width // 2 - 100, Height // 2 + 75, 200, 75)

#font for button text
font = pygame.font.Font(None, 36)

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
    draw_button(hard_button, "Hard")
    draw_button(back_button_difficulty, "Back")




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
    

#AI class
class AI:
    def __init__(self):
        self.difficulty = "easy"
        self.player = 2

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

        elif self.difficulty == "hard":
            eval, move = self.minimax(main_board, True)
        
        #printing the move and evaluation for debugging
        print(f"AI chose to mark square {move} with evaluation {eval}")
  
        return move
    
        
    

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
    

#main method for the game
def main():
    global current_screen, bg_colour, Line_Colour
    game = Game()

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

                        elif hard_button.collidepoint(event.pos):    
                            click_sound.play()
                            current_screen = "game"
                            screen.fill(bg_colour)
                            game.game_mode = "ai_game"
                            game.restart()
                            game.ai.difficulty = "hard"
                            game.ai_difficulty = "hard"

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

                            elif bg_colour == Light_Red:
                                bg_colour = Light_Purple
                                Line_Colour = Line_Colour_Purple
    
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
        elif current_screen == "difficulty_selection":
            difficulty_selection_menu()

        #AI's turn in ai mode
        elif current_screen == "game" and game.game_mode == "ai_game" and game.player == game.ai.player:
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
                current_screen = "game_over"


        pygame.display.update()

main()