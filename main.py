import pygame,sys
from game import Game
from config import *
from player import Player
from board import Board
from ui import UI
pygame.init()


screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Game Caro')

game=Game()
ui=UI(game)
running =True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                ui.handle_click(pygame.mouse.get_pos())


    
    screen.fill(WHITE)
    ui.draw(screen)
    pygame.display.update()

pygame.quit()
sys.exit()