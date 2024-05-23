from board import Board
from game import Game
from config import *

class UI:
    def __init__(self,game):
        self.game=game
    def draw(self,screen):
        self.game.board.draw(screen)
        winning_squares=self.game.board.check_win()
        for row,col in winning_squares:
            if self.game.get_current_player().symbol=='X':
                pygame.draw.rect(screen,X_COLOR_WIN,(col*SQ_SIZE+1,row*SQ_SIZE+1,SQ_SIZE-2,SQ_SIZE-2))
                screen.blit(X_image_win,(col*SQ_SIZE+SQ_SIZE//2-X_image.get_width()//2,row*SQ_SIZE+SQ_SIZE//2-X_image.get_height()//2))
            else:
                pygame.draw.rect(screen,O_COLOR_WIN,(col*SQ_SIZE+1,row*SQ_SIZE+1,SQ_SIZE-2,SQ_SIZE-2))
                screen.blit(O_image_win,(col*SQ_SIZE+SQ_SIZE//2-O_image.get_width()//2,row*SQ_SIZE+SQ_SIZE//2-O_image.get_height()//2))
    def handle_click(self,pos):
        row,col=pos[1]//SQ_SIZE,pos[0]//SQ_SIZE
        if self.game.handle_click(row,col):
            pass

