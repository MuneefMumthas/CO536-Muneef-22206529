import sys
import pygame

#initialising the variables
Width = 900
Height = 900

#initialising pygame and setting up the screen
pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("TIC TAC TOE  (CO536_CW1_Muneef_22206529)")
screen.fill((163,163,205))

#Creating the buttons
play_button = pygame.Rect(Width // 2 - 100, Height // 2 - 75, 200, 75)
settings_button = pygame.Rect(Width // 2 - 100, Height // 2 + 37.5, 200, 75)

pvplayer_button = pygame.Rect(Width // 2 - 150, Height // 2 - 150, 300, 75)
pvcomputer_button = pygame.Rect(Width // 2 - 150, Height // 2 - 37.5, 300, 75)
back_button = pygame.Rect(Width // 2 - 100, Height // 2 + 75, 200, 75)

#font for button text
font = pygame.font.Font(None, 36)

#game state
current_screen = "main_menu"

#Creating the main menu
def main_menu():
    screen.fill((163,163,205))

    #Play button
    pygame.draw.rect(screen, (0, 0, 0), play_button)
    play_text = font.render("Play", True, (255, 255, 255))
    screen.blit(play_text, (play_button.centerx - play_text.get_width() // 2, play_button.centery - play_text.get_height() // 2))

    #Settings button
    pygame.draw.rect(screen, (0, 0, 0), settings_button)
    settings_text = font.render("Settings", True, (255, 255, 255))
    screen.blit(settings_text, (settings_button.centerx - settings_text.get_width() // 2, settings_button.centery - settings_text.get_height() // 2))

def game_mode_menu():
    screen.fill((163,163,205))

    #Player vs Player button
    pygame.draw.rect(screen, (0, 0, 0), pvplayer_button)
    pvplayer_text = font.render("Player vs Player", True, (255, 255, 255))
    screen.blit(pvplayer_text, (pvplayer_button.centerx - pvplayer_text.get_width() // 2, pvplayer_button.centery - pvplayer_text.get_height() // 2))

    #Player vs Computer button
    pygame.draw.rect(screen, (0, 0, 0), pvcomputer_button)
    pvcomputer_text = font.render("Player vs Computer", True, (255, 255, 255))
    screen.blit(pvcomputer_text, (pvcomputer_button.centerx - pvcomputer_text.get_width() // 2, pvcomputer_button.centery - pvcomputer_text.get_height() // 2))

    #Back button
    pygame.draw.rect(screen, (0, 0, 0), back_button)
    back_text = font.render("Back", True, (255, 255, 255))
    screen.blit(back_text, (back_button.centerx - back_text.get_width() // 2, back_button.centery - back_text.get_height() // 2))

#main method for the game
def main():
    global current_screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                
                    if current_screen == "main_menu":
                    
                        if play_button.collidepoint(event.pos):
                            current_screen = "game_mode_selection"

                        elif settings_button.collidepoint(event.pos):
                            print("Settings")

                    elif current_screen == "game_mode_selection":

                        if pvplayer_button.collidepoint(event.pos):
                        
                            print("Player vs Player")
                    
                        elif pvcomputer_button.collidepoint(event.pos):
                        
                            print("Player vs Computer")

                        elif back_button.collidepoint(event.pos):
                            current_screen = "main_menu"
        
        if current_screen == "main_menu":
            main_menu()
        elif current_screen == "game_mode_selection":
            game_mode_menu()

        pygame.display.update()

main()