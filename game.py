
from player import Player
from board import Board
from playerinfoui import PLAYERINFOUI

class Game:
    def __init__(self):
        self.board=Board()
        self.players=[Player('Player 1','X'),Player('Player 2','O')]
        self.current_player_index=0
        self.winner=None

    def switch_player(self,player_info_ui):
        self.players[self.current_player_index].time=5
        self.current_player_index=1-self.current_player_index
        player_info_ui.update_current_player_index(self.current_player_index)

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
                    self.winner=player                  
                    return True
                self.switch_player(player_info_ui)
                self.get_current_player().time=5
                
        else:
            self.board.temp_mark=(row,col)
        return False
    def reset(self):
        self.board=Board()
        self.current_player_index=0
        for player in self.players:
            player.time=5