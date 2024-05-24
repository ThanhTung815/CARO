from board import Board
from game import Game
from config import *

class UI:
    def __init__(self,game):
        '''
        Khởi tạo giao diện người dùng với game đã được truyền vào
        '''
        self.game=game

    def draw_board(self,screen):
        '''
        Vẽ bảng chơi và các ô thắng lên màn hình
        '''
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
        '''
        Xử lý sự kiện click chuột lên bảng chơi
        '''
        x,y=pos
        if x>=WIDTH:
            self.game.handle_click(pos)
           

