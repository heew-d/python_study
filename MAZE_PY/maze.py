import os
import sys
from copy import deepcopy
import time

# 불러올 파일 담을 리스트 초기화
map = []
# player 위치 초기화
player_x = 0
player_y = 0
# 상태값 저장
legend = {
    "start" : "S",
    "finish" : "F",
    "player" : "P",
    "road" : "o",
    "wall" : "x"
}

# map 파일 불러오기
def leadMap():
    with open('./MAZE_PY/level1.map', 'r', encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            data_list = list(line.split())
            map.append(data_list)
    return map
map = leadMap()

map2 = deepcopy(map) # 원본파일 복사

# 시작위치 저장
def start():
    global player_x
    global player_y
    start = 'S'
    # 처음 시작 player 위치 구하기
    for i in range(len(map)):
        if start in map[i]:
            player_x = i
            player_y = map[i].index(start)

# 화면에 map 출력
def display():
    global player_x
    global player_y
    print()

    # 복사본에 player 위치 저장
    map2[player_x][player_y] = legend["player"]

    # map 출력 (복사본)
    for row in map2:
        print(" ".join(row))
    print()
    # 현재 플레이어 위치 출력
    print(f'현재 플레이어: ([P] row: {player_x}, col: {player_y})')  

# 사용자가 갈 수 있는 방향 체크
def checkValidDirection():
    global player_x
    global player_y
    global map2
    # 입력받을 숫자
    keyInput = int(input("어느 방향으로 이동하시겠습니까?(숫자만 가능)"))

    # 원본을 다시 복사해놓고 키 입력을 받으면 새롭게 출력
    map2 = deepcopy(map)
                
    if keyInput == 1:
        if map2[player_x][player_y+1] == legend["wall"]:
            print("벽으로 막혀 있습니다.")
        elif map2[player_x][player_y+1] == legend["road"]:
            player_y = player_y+1
            map2[player_x][player_y] = legend["player"]
        elif map2[player_x][player_y+1] == legend["finish"]:
            player_y = player_y+1
            map2[player_x][player_y] = legend["player"]
            print("미로 탈출!!!")

    elif keyInput == 2:
        if map2[player_x][player_y-1] == legend["wall"]:
            print("벽으로 막혀 있습니다.")
        elif map2[player_x][player_y-1] == legend["road"]:
            player_y = player_y-1
            map2[player_x][player_y] = legend["player"] 
        elif map2[player_x][player_y-1] == legend["finish"]:
            player_y = player_y-1
            map2[player_x][player_y] = legend["player"]
            print("미로 탈출!!!")

    elif keyInput == 3:
        if map2[player_x+1][player_y] == legend["wall"]:
            print("벽으로 막혀 있습니다.")
        elif map2[player_x+1][player_y] == legend["road"]:
            player_x = player_x+1
            map2[player_x][player_y] = legend["player"]
        elif map2[player_x+1][player_y] == legend["finish"]:
            player_x = player_x+1
            map2[player_x][player_y] = legend["player"]
            print("미로 탈출!!!")

    elif keyInput == 4:
        if map2[player_x-1][player_y] == legend["wall"]:
            print("벽으로 막혀 있습니다.")
        elif map2[player_x-1][player_y] == legend["road"]:
            player_x = player_x-1
            map2[player_x][player_y] = legend["player"]
        elif map2[player_x-1][player_y] == legend["finish"]:
            player_x = player_x-1
            map2[player_x][player_y] = legend["player"]
            print("미로 탈출!!!")
    else:
        print("1~4사이의 숫자만 입력하시오.")   
    

# 초기 준비 
def prepares():
    global player_x
    global player_y
    prompt = '''
    1. 동쪽으로 이동
    2. 서쪽으로 이동
    3. 남쪽으로 이동
    4. 북쪽으로 이동
    '''

    # 시작위치 저장
    start()
    while True:
        display() # 화면에 map 출력
        print(prompt) # prompt 출력
        checkValidDirection() # 사용자가 갈 수 있는 방향 체크
        
        time.sleep(1)
        os.system('clear') # 화면 지우기
        
if __name__ =="__main__":

    # 지도 불러오기
    # 시작위치와 종료위치 파악(표시x, 기록만)
    # 플레이어의 현재위치를 지도의 시작위치로 설정 (표시x, 기록만)
    prepares()

    # 플레이 (runloop)
    # 지도와 플레이어의 위치표시
    # 플레이어가 이동할 수 있는 방향을 파악하고 선택지를 표시
    # 플레이어가 선택한 방향으로 플레이어 이동(상태 변경)
    # 플레이어의 현재위치가 종료위치인지 확인(확인된 결과에 따라 계속 진행할지 종료할지 선택)

    pass