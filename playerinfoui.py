import pygame
from config import *


class PLAYERINFOUI:
    def __init__(self, players):
        '''
        Khởi tạo giao diện thông tin người chơi với danh sách người chơi và các thuộc tính cần thiết
        '''
        self.players = players
        self.font = pygame.font.SysFont(None, 36)
        self.time_font = pygame.font.SysFont(None, 28)
        self.current_player_index = 0  

    def handle_click(self, pos):
        '''
        Xử lý sự kiện click cho phần thông tin người chơi (nếu có)
        '''
        pass

    def draw(self, screen):
        '''
        Vẽ thông tin người chơi lên màn hình
        '''
        x_offset = WIDTH+10
        for i, player in enumerate(self.players):
            y_offset = 20+i * 100

            # Tên người chơi
            name_text = self.font.render(f"{player.name}", True, (0, 0, 0))
            screen.blit(name_text, (x_offset, y_offset))

            # Ký hiệu người chơi
            symbol_text = self.font.render(f"Symbol: {player.symbol}", True, (0, 0, 0))
            screen.blit(symbol_text, (x_offset, y_offset + 30))

            # Thời gian còn lại
            time_text = self.time_font.render(f"Time: {player.time}s", True, (0, 0, 0))
            screen.blit(time_text, (x_offset, y_offset + 60))

            # Highlight cho người chơi hiện tại
            if i == self.current_player_index:
                pygame.draw.rect(screen, (255, 0, 0), (x_offset-5, y_offset-5, OFFSET-30, 95), 2)

    def update_current_player_index(self, current_player_index):
        '''
        Cập nhật chỉ số người chơi hiện tại
        '''
        self.current_player_index = current_player_index


    def update_time(self, current_player_index):
        '''
        Cập nhật thời gian còn lại của người chơi hiện tại
        '''
        self.players[current_player_index].time -= 1

    def reset_time(self, current_player_index):
        '''
        Reset thời gian còn lại của người chơi hiện tại
        '''
        self.players[current_player_index].time = 5
