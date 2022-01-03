#Tic Tac Toe Game-two players take turns to complete a row, a column, or a diagonal 
import pygame
import sys
import NumPy

print(pygame.ver)

pygame.init()

pygame.display.set_caption("Tic Tac Toe")
window_surface = pygame.display.set_mode((1000, 800))

background = pygame.Surface((1000, 800))
background.fill(pygame.Color("#000000"))
scoreboard = pygame.image.load('C:/Users/debbi/OneDrive/Documents/GitHub/100-Days-of-Python/tictactoe game/scoreboard.png')
board = pygame.image.load('C:/Users/debbi/OneDrive/Documents/GitHub/100-Days-of-Python/tictactoe game/Tic-tac-toe.png')
circle = pygame.image.load('C:/Users/debbi/OneDrive/Documents/GitHub/100-Days-of-Python/tictactoe game/circleo.png')
xMark = pygame.image.load('C:/Users/debbi/OneDrive/Documents/GitHub/100-Days-of-Python/tictactoe game/xmark.png')


is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             is_running = False

    window_surface.blit(board, (0, 0))
    window_surface.blit(scoreboard, (600,10))
    window_surface.blit(circle, (800,600))
    



    pygame.display.update()

