import os
import time

map = []
# map = ['oxxoooxx','oxxoooxx']
# map = [[0,0,0,0,1,0,1],[0,0,0,0,1,0,1]]]
POSITION_Y = 0
POSITION_X = 1
startPos = (0,0) # 2차원 좌표로 사용, 그래서 항목이 2개인 튜플
finishPos = (0,0) # 2차원 좌표로 사용, 그래서 항목이 2개인 튜플
playerPos = [0,0]

def loadMap():

    global startPos
    global finishPos
    # global map

    # 형렬, 매트릭스
    with open('./MAZE_PY/level1.map', 'r') as f:
        # for in  #명확한 제한이 존재할때
        y=0
        while True:
            # line = f.readline()
            # line = line.replace('\n', '')
            # line = line.replace(' ', '')
            line = f.readline().replace('\n','').replace(' ','')

            # None 일땐 종료
            if not line:
                break

            map.append(line) # 됨
            # map = [] # 안됨

            # 해당 문자열안에 S나 F가 있는지 파악하고, 해당 문자의 위치가 어딘지 파악
            # 알아낸 위치가 곧 x축의 위치
            # str.find() 해당 문자가 있으면 문자의 위치(인덱스)를 리턴하고, 없으면 -1을 리턴

            findedIndex = line.find('S')
            if -1 < findedIndex: 
                # 시작위치 파악, 기억
                # (y,findedIndex)
                # print(f'({y},{findedIndex}) 시작지점')
                startPos = (y,findedIndex) #값을 설정
                pass
            
            findedIndex = line.find('F')
            if -1 < findedIndex:
                # 종료위치 파악, 기억
                # (y,findedIndex)
                # print(f'({y},{findedIndex}) 도착지점')
                finishPos = (y,findedIndex) #값을 설정
                pass

            y = y + 1

            # print(line, end='')
            pass

         #'oxoooxxxo\n'
        print(map)
        # print(f'startPos: {startPos}')
        # print(f'finishPos: {finishPos}')
    
    pass

def display():
    # 지도 표시
    # for line in map:
    #     # print(line)
    #     for item in line:
    #         print(item, end=' ')
    #     print()

    for y in range(len(map)):
        line = map[y]
        for x in range(len(line)):
            item = line[x]
            # print(f'({y},{x}) {item}', end=' ')
            if playerPos[POSITION_Y] == y and playerPos[POSITION_X] == x:
                # 현재타일은 플레이어의 위치
                print('P', end=' ')
            else:
                # 플레이어 위치가 아닌 일반 타일
                print(item, end=' ')
            # time.sleep(0.1)
        print()
    # 플레이어의 현재위치*

    pass

def checkValidDirection():
    global move

    selection = input("어느 방향으로 이동하시겠습니까?(숫자만 가능)")
    if selection.isdigit():
       '''
        1. 동쪽으로 이동
        2. 서쪽으로 이동
        3. 남쪽으로 이동
        4. 북쪽으로 이동
        '''
    # (-1,0), (0,1), (1,0), (0,-1)
    
    offset = [[-1,0],[0,1],[1,0],[0,-1]]

    if selection == 4:
        move = playerPos.append([x+y for x,y in zip(playerPos, offset[0])])
    print(move)

    pass

def prepares():
    # 초기 구동시 세팅해야할 처리들

    #지도불러오기
    #시작위치와 종료위치 파악 (표시x, 기록만)
    loadMap()
    
    #플레이어의 현재위치를 지도의 시작위치로 설정 (표시x, 기록만)
    playerPos[POSITION_Y] = startPos[POSITION_Y]
    playerPos[POSITION_X] = startPos[POSITION_X]
    # playerPos = list(startPos[:])

    pass


if __name__ == "__main__":

    #지도불러오기*
    #시작위치와 종료위치 파악 (표시x, 기록만)
    #플레이어의 현재위치를 지도의 시작위치로 설정 (표시x, 기록만)
    prepares()
    # display()
    # checkValidDirection()
    #         0        1      2      3 
    # offset ((-1,0), (0,1), (1,0), (0,-1))
    # 북 P(5,5) + O(-1,0) = M(4,5)
    # 동 P(5,5) + O(0,1) = M(5,6)
    # 남 P(5,5) + O(1,0) = M(6,5)
    # 서 P(5,5) + O(0,-1) = M(5,4)

    # 플레이 (runloop)
    while True:
        # 지도와 플레이어의 위치표시*
        os.system('clear')
        display()
        checkValidDirection()

        # 플레이어가 이동할 수 있는 방향을 파악하고 선택지를 표시 
        # 플레이어가 선택한 방향으로 플레이어 이동 (상태를 변경) (플레이어를 어떻게 이동시킬지)
        # 플레이어의 현재위치가 종료위치인지 확인 (확인된 결과에 따라 계속진행할지 종료할지 선택)
        pass

    pass