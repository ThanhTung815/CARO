from player import Player
from board import Board


class Game:
    def __init__(self):
        self.board=Board()
        self.players=[Player('Player 1','X'),Player('Player 2','O')]
        self.current_player_index=0
    def switch_player(self):
        self.current_player_index=1-self.current_player_index


    def get_current_player(self):
        return self.players[self.current_player_index]
    def handle_click(self,row,col):
        player=self.get_current_player()
        if self.board.temp_mark==(row,col):
            if self.board.update(row,col,player.symbol):
                self.board.temp_mark=None
                if self.board.check_win():
                    print(f'{player.name} wins')
                    return True
                self.switch_player()
        else:
            self.board.temp_mark=(row,col)
        return False
    def reset(self):
        self.board=Board()
        self.current_player_index=0
