import pygame
from config import *



class Board:
    def __init__(self,size=15):
        self.size=size
        self.grid=[['' for _ in range(size)] for _ in range(size)]
        self.temp_mark=None
        self.last_mark=None
    def draw(self,screen):

        #vẽ ô vuông viền đen
        screen.fill(WHITE)
        for row in range(self.size):
            for col in range(self.size):
                rect=pygame.Rect(col*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE)
                pygame.draw.rect(screen,(159,161,165),rect,1)
                if self.temp_mark==(row,col):
                    row,col=self.temp_mark
                    pygame.draw.rect(screen,HIGHTLIGHT_COLOR,(col*SQ_SIZE+1,row*SQ_SIZE+1,SQ_SIZE-2,SQ_SIZE-2),0)
                elif self.last_mark==(row,col):
                    pygame.draw.rect(screen,HIGHTLIGHT_COLOR,(col*SQ_SIZE+1,row*SQ_SIZE+1,SQ_SIZE-2,SQ_SIZE-2),0)
                if self.grid[row][col]=='X':
                    screen.blit(X_image,(col*SQ_SIZE+SQ_SIZE//2-X_image.get_width()//2,row*SQ_SIZE+SQ_SIZE//2-X_image.get_height()//2))
                elif self.grid[row][col]=='O':
                    screen.blit(O_image,(col*SQ_SIZE+SQ_SIZE//2-O_image.get_width()//2,row*SQ_SIZE+SQ_SIZE//2-O_image.get_height()//2))



    def update(self,row,col,player_symbol):
        if self.grid[row][col]=='':
            self.grid[row][col]=player_symbol
            self.last_mark=(row,col)
            return True
        return False
    
    def check_win(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col]!='':
                    winning_squares=self.check_five(row,col)
                    if winning_squares:
                        return winning_squares
                    
        return []
        

    def count_direction(self,row,col,direction):
        count=1
        winning_squares=[(row,col)]
        for i in range(1,self.size):
            new_row=row+i*direction[0]
            new_col=col+i*direction[1]
            if 0<=new_row<self.size and 0<=new_col<self.size and self.grid[new_row][new_col]==self.grid[row][col]:
                count+=1
                winning_squares.append((new_row,new_col))
            else:
                break
        for i in range(1,self.size):
            new_row=row-i*direction[0]
            new_col=col-i*direction[1]
            if 0<=new_row<self.size and 0<=new_col<self.size and self.grid[new_row][new_col]==self.grid[row][col]:
                count+=1
                winning_squares.append((new_row,new_col))
            else:
                break
        return count,winning_squares
    def check_five(self,row,col):
        directions=[(0,1),(1,0),(1,1),(1,-1)]
        for d in directions:
            count,winning_squares=self.count_direction(row,col,d)
            if count>=5:
                return winning_squares
        return []