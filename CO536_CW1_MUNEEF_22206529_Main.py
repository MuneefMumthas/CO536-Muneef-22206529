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
settings_button = pygame.Rect(Width // 2 - 100, Height // 2 + 50, 200, 75)

#font for button text
font = pygame.font.Font(None, 36)

#Creating the main menu
def main_menu():
    
    #Play button
    pygame.draw.rect(screen, (0, 0, 0), play_button)
    play_text = font.render("Play", True, (255, 255, 255))
    screen.blit(play_text, (play_button.x + 70, play_button.y + 25))

    #Settings button
    pygame.draw.rect(screen, (0, 0, 0), settings_button)
    settings_text = font.render("Settings", True, (255, 255, 255))
    screen.blit(settings_text, (settings_button.x + 50, settings_button.y + 25))

#main method for the game
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    print("Play")
                elif settings_button.collidepoint(event.pos):
                    print("Settings")
        
        main_menu()
        pygame.display.update()

main()