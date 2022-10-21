# 키보드 이용하여 도형 움직이기
import pygame # pygame 선언
import sys

# pygame에 사용되는 전역변수 선언
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# 컬러 세팅
white = (255,255,255)
black = (0,0,0)

pygame.init() # pygame 초기화
pygame.display.set_caption("Simple PyGame Example") # 창 이름 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 창 크기 설정

pos_x = 200
pos_y = 200

clock = pygame.time.Clock()

# pygame 무한루프
while True:
    clock.tick(60) # 초당 프레임 단위
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 1

    if key_event[pygame.K_RIGHT]:
        pos_x += 1

    if key_event[pygame.K_UP]:
        pos_y -= 1
    
    if key_event[pygame.K_DOWN]:
        pos_y += 1

    screen.fill(black)
    pygame.draw.circle(screen, white, (pos_x, pos_y), 20) # 원 그리기
    pygame.display.update()