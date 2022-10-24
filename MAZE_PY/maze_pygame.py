import pygame
import sys

# 게임 화면 크기 설정
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

white = (255,255,255)
black = (0,0,0)

pygame.init() # 초기화
pygame.display.set_caption("maze") # 화면 타이틀 설정

# FPS 설정
clock = pygame.time.Clock() # 프레임 설정
    
# 캐릭터 불러오기
character = pygame.image.load("/home/aa/python_study/python_study/MAZE_PY/robot.png")
character_size = character.get_rect().size # 캐릭터 이미지 사이즈 구하기
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_pos_x = (SCREEN_WIDTH/2) - (character_width / 2)
character_pos_y = SCREEN_HEIGHT - character_height

# 이동할 좌표
pos_x = 0
pos_y = 0

# 이동 속도
character_speed = 1

# 이벤트 루프
running = True # 게임이 진행중인지
while running:
    clock.tick(60) # 프레임 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # 방향키 입력
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        character_pos_x -= character_speed

    if key_event[pygame.K_RIGHT]:
        character_pos_x += character_speed

    if key_event[pygame.K_UP]:
        character_pos_y -= character_speed
    
    if key_event[pygame.K_DOWN]:
        character_pos_y += character_speed


    # 왼쪽, 오른쪽 경계 정하기
    if character_pos_x < 0:
        character_pos_x = 0
    elif character_pos_x > SCREEN_WIDTH - character_width:
        character_pos_x = SCREEN_WIDTH - character_width
    # 위, 아래쪽 경계 정하기
    if character_pos_y < 0:
        character_pos_y = 0
    elif character_pos_y > SCREEN_HEIGHT - character_height:
        character_pos_y = SCREEN_HEIGHT - character_height


    screen.fill(black) # 배경색 채우기
    screen.blit(character, (character_pos_x, character_pos_y)) # 배경에 이미지 그려주고 위치 지정
    
    # 게임 화면 다시 그리기
    pygame.display.update()
