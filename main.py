import pygame
import sys
from game import Game
from config import *
from player import Player
from board import Board
from ui import UI
from playerinfoui import PLAYERINFOUI
from button import Button

pygame.init()

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH+OFFSET, HEIGHT))
pygame.display.set_caption('Game Caro')

# Tạo các nút cho menu
button_height=50
button_spacing=20
start_y=HEIGHT//2-(button_height*3+button_spacing*2)//2

font = pygame.font.Font(None, 36)

play_button = Button("PLAY", font, (0, 0, 255), (0, 0, 200), ((WIDTH+OFFSET)//2-50, start_y)) 
help_button = Button("HELP", font, (0, 255, 0), (0, 200, 0), ((WIDTH+OFFSET)//2-50, start_y+button_height+button_spacing))
quit_button = Button("QUIT", font, (255, 0, 0), (200, 0, 0), ((WIDTH+OFFSET)//2-50 , start_y+2*(button_height+button_spacing)))

# tạo các nút cho game
play_again_button=Button("PLAY AGAIN",font,(0,0,255),(0,0,200),(WIDTH//2-50,HEIGHT//2))
exit_button=Button("EXIT",font,(255,0,0),(200,0,0),(WIDTH+20,HEIGHT//2+button_height+button_spacing))
pause_button=Button("PAUSE",font,(0,0,255),(0,0,200),(WIDTH+20,HEIGHT//2))
resume_button=Button("RESUME",font,(0,0,255),(0,0,200),(WIDTH//2-50,HEIGHT//2))

# Trạng thái của game
game_state = "menu"  # 'menu', 'playing', 'help', 'paused'


game = Game()
ui = UI(game)
player_info_ui = PLAYERINFOUI(game.players)

clock = pygame.time.Clock()
last_time = pygame.time.get_ticks()
running = True

def draw_menu():
    # Vẽ màn hình menu với các nút PLAY, HELP, QUIT
    screen.fill((0, 0, 0))
    play_button.draw(screen)
    help_button.draw(screen)
    quit_button.draw(screen)
    pygame.display.flip()

def draw_help():
    # Vẽ màn hình trợ giúp ( thông tin hướng dẫn game )
    screen.fill((0, 0, 0))
    help_text = font.render("DISPLAY THE RULE OF CARO GAME", True, (255, 255, 255))
    screen.blit(help_text, (100, 300))
    pygame.display.flip()

def draw_game():
    # Vẽ màn hình game với bảng chơi và thông tin người chơi 
    screen.fill(WHITE)
    ui.draw_board(screen)
    player_info_ui.draw(screen)
    if game_state=="playing":
        pause_button.draw(screen)
        exit_button.draw(screen)
    elif game_state=="paused":
        resume_button.draw(screen)
    if game.winner:
        font = pygame.font.Font(None, 36)
        text = font.render(f"{game.winner.name} wins!", True, (255, 0, 0))
        screen.blit(text, (WIDTH//2-50, HEIGHT//2-50))
        play_again_button.draw(screen)
    pygame.display.flip()

while running:
    # Xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state == "menu":
            if play_button.handle_event(event):
                game_state = "playing"
            elif help_button.handle_event(event):
                game_state = "help"
            elif quit_button.handle_event(event):
                running = False
        elif game_state == "help":
            if event.type == pygame.KEYDOWN:
                game_state = "menu"
        elif game_state == "playing":

            if game.winner and play_again_button.handle_event(event):
                game.reset()
                game_state = "playing"
                game.winner=None
            if exit_button.handle_event(event):
                game_state = "menu"
            if pause_button.handle_event(event):
                game_state="paused"

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = "menu"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= WIDTH:
                        player_info_ui.handle_click(pos)
                    else:
                        row = pos[1] // SQ_SIZE
                        col = pos[0] // SQ_SIZE
                        if game.handle_click(row, col,player_info_ui):
                            player_info_ui.reset_time(game.current_player_index)
        elif game_state=="paused":
            if resume_button.handle_event(event):
                game_state="playing"                     
    
    current_time = pygame.time.get_ticks()
    if current_time - last_time >= 1000 and game_state == "playing" and not game.winner:
        player_info_ui.update_time(game.current_player_index)
        if game.get_current_player().time == 0:
            game.switch_player(player_info_ui)
            player_info_ui.reset_time(game.current_player_index)
            
        last_time = current_time

    if game_state == "menu":
        draw_menu()
    elif game_state == "help":
        draw_help()
    elif game_state == "playing" or game_state=="paused":
        draw_game()
    

    clock.tick(60)

pygame.quit()
sys.exit()
