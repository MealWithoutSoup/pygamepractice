import pygame
from pygame.image import load
from setting import*

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height),RESIZABLE)

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background, background_rect = load_image('background.png', screen_width, screen_height) # rect = rectangle

# 캐릭터(스프라이트) 불러오기
character, character_rect = load_image('character.png') # rect = rectangle
character_size = character_rect.size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
# 이미지의 기준점은 항상 좌측상단이기 때문에 이미지의 크기를 고려해서 숫자 조정이 필요함
# 세로의 경우 화면크기 - 캐릭터 크기, 가로의 경우 : 화면 절반에서 캐릭터 절반을 뺌
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    #screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면을 매 프레임마다 다시 그리기!

# pygame 종료
pygame.quit()