from player import Player
from board import Board
from playerinfoui import PLAYERINFOUI

class Game:
    def __init__(self):
        self.board=Board()
        self.players=[Player('Player 1','X'),Player('Player 2','O')]
        self.current_player_index=0
    

    def switch_player(self):
        self.current_player_index=1-self.current_player_index


    def get_current_player(self):
        return self.players[self.current_player_index]
    # def check_winner(self):
    #     if self.board.check_win():
    #         return True
    #     return False

    def handle_click(self,row,col,player_info_ui):
        player=self.get_current_player()
        if self.board.temp_mark==(row,col):
            if self.board.update(row,col,player.symbol):
                self.board.temp_mark=None
                if self.board.check_win():
                    print(f'{player.name} wins')
                    
                    return True
                self.switch_player()
                self.get_current_player().time=30
                player_info_ui.update_current_player_index(self.current_player_index)
        else:
            self.board.temp_mark=(row,col)
        return False
    def reset(self):
        self.board=Board()
        self.current_player_index=0
        for player in self.players:
            player.time=30