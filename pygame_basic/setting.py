import os
import pygame
from pygame import transform
from pygame.locals import RESIZABLE, RLEACCEL


# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름
FPS = 60 # FPS
# 이동 속도 FPS 때문에 변수로 설정
character_speed = 0.6
# 총 시간
total_time = 10

# 게임 내 image를 넣을 때 쓰는 함수
def load_image(name, sizex=-1, sizey=-1, color_key=None):
    full_name = os.path.join('sprites', name)
    img = pygame.image.load(full_name)
    img = img.convert()
    if color_key is not None:
        if color_key == -1:
            color_key = img.get_at((0, 0))
        img.set_colorkey(color_key, RLEACCEL)
    if sizex != -1 or sizey != -1:
        img = transform.scale(img, (sizex, sizey))
    return (img, img.get_rect())