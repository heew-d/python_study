import os
import time
import random

map:list = []
# map = ['oxxoooxx','oxxoooxx']
# map = [[0,0,0,0,1,0,1],[0,0,0,0,1,0,1]]]
POSITION_Y = 0
POSITION_X = 1

startPos = (0,0) # 2차원 좌표로 사용, 그래서 항목이 2개인 튜플
finishPos = (0,0) # 2차원 좌표로 사용, 그래서 항목이 2개인 튜플
playerPos = [0,0]

maxRow = 0
maxCol = 0

# map 불러오기
def loadMap():
    global startPos, finishPos, maxRow, maxCol

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

            maxCol = len(line)
            y = y + 1
            # print(line, end='')
            pass

        #'oxoooxxxo\n'
        # print(map)
        # print(f'startPos: {startPos}')
        # print(f'finishPos: {finishPos}')
        maxRow = y

    pass

# 지도 표시
def display():
    # for line in map:
    #     # print(line)
    #     for item in line:
    #         print(item, end=' ')
    #     print()

    # 지도 및 플레이어의 현재위치
    for y in range(len(map)):
        line = map[y] # 한줄 단위로 읽어옴
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
    pass

def displaySelection() -> int:
    
    prompt = '''
    1. 북쪽으로 이동
    2. 동쪽으로 이동
    3. 남쪽으로 이동
    4. 서쪽으로 이동
    0. 게임에서 탈출
    행동을 선택해 주세요(1~4, 0)'''
    print(prompt, end="")

    try:
        # 사용자의 입력을 기다리며 프로그램의 진행은 블록
        # 사용자가 입력을 하고 엔터를 입력해야 진행
        choice = input()
        
        if not choice.isdigit(): # 입력된 값이 숫자인지 파악
            return -1
            
        return int(choice) # 문자열(str)을 정수형(int)으로 변환
    except:
        return -1


# 초기 구동시 세팅해야할 처리들
def prepares():

    #지도불러오기
    #시작위치와 종료위치 파악 (표시x, 기록만)
    loadMap()
    
    #플레이어의 현재위치를 지도의 시작위치로 설정 (표시x, 기록만)
    playerPos[POSITION_Y] = startPos[POSITION_Y]
    playerPos[POSITION_X] = startPos[POSITION_X]
    # playerPos = list(startPos[:])

    pass

# 갈 수 있는 길인지 검사
def validation(yIndex, xIndex):

    valid = True
    # 해당 위치(y,x)의 타일 값을 읽어옴
    # 1참 -> y가 유요한 범위인지
    valid = valid and (yIndex >= 0 and yIndex < maxRow)
    # 2참 -> x가 유효한 범위인지
    valid = valid and (xIndex >= 0 and xIndex < maxCol)
    
    if not valid:
        return False

    tile = map[yIndex][xIndex]
   
    # 1참 -> 유효한 타일인지
    valid = tile == 'o' or tile == 'S' or tile == 'F'
    
    return valid

offsets = ((-1,0), (0,1), (1,0), (0,-1))
directionDicts = (
    {
        'offset':(-1,0),
        'directionName':'북'
    },
    {
        'offset':(0,1),
        'directionName':'동'
    },
    {
        'offset':(1,0),
        'directionName':'남'
    },
    {
        'offset':(0,-1),
        'directionName':'서'
    }
)
# 다수의 값을 넣을 수 있는 자료형
# 리스트, 튜플, 딕셔너리

def checkValidDirection(selection):
    valid = False
    # directionName = ''

    dict = directionDicts[selection - 1]
    offset = dict['offset']
    directionName = dict['directionName']
    yIndex = playerPos[POSITION_Y] + offset[POSITION_Y]
    xIndex = playerPos[POSITION_X] + offset[POSITION_X]

    # if selection == 1:
    #     # 플레이어 기준 북쪽 한칸 방향이 갈 수 있는지 파악
    #     yIndex = playerPos[POSITION_Y] + -1
    #     xIndex = playerPos[POSITION_X] + 0
    #     valid = validation(yIndex, xIndex)
    #     directionName = '북'

    # if selection == 2:
    #     # 플레이어 기준 동쪽 한칸 방향이 갈 수 있는지 파악
    #     yIndex = playerPos[POSITION_Y] + 0
    #     xIndex = playerPos[POSITION_X] + 1
    #     valid = validation(yIndex, xIndex)
    #     directionName = '동'
            
    # if selection == 3:
    #     # 플레이어 기준 남쪽 한칸 방향이 갈 수 있는지 파악
    #     yIndex = playerPos[POSITION_Y] + 1
    #     xIndex = playerPos[POSITION_X] + 0
    #     valid = validation(yIndex, xIndex)
    #     directionName = '남'

    # if selection == 4:
    #     # 플레이어 기준 서쪽 한칸 방향이 갈 수 있는지 파악
    #     yIndex = playerPos[POSITION_Y] + 0
    #     xIndex = playerPos[POSITION_X] + -1
    #     valid = validation(yIndex, xIndex)
    #     directionName = '서'

    resultDict = {
        'valid' : valid,
        'directionName' : directionName,
        'offset' : offset,
    }
    # resultTup = (valid, directionName)
    return resultDict


def makePlayerOffsetWithSelection(selection):
    # offset ((-1,0), (0,1), (1,0), (0,-1))

    if selection <= 0 or selection > 4:
        # return None
        return (0,0)
    
    return offsets[selection - 1]

    # if selection == 1:
    #     return (-1,0)
    # if selection == 2:
    #     return (0,1)    
    # if selection == 3:
    #     return (1,0)
    # if selection == 4:
    #     return (0,-1)

    pass

if __name__ == "__main__":

    #지도불러오기*
    #시작위치와 종료위치 파악 (표시x, 기록만)
    #플레이어의 현재위치를 지도의 시작위치로 설정 (표시x, 기록만)
    prepares()
    # display()

    # 플레이 (runloop)
    while True:
        # 지도와 플레이어의 위치표시*
        os.system('clear') # 화면 지우기
        display()
        
        # 플레이어의 현재위치가 종료위치인지 확인 (확인된 결과에 따라 계속진행할지 종료할지 선택)
        # 플레이어의 y축 값과 종료의 y축 값이 같고, 플레이어의 x축 값과 종료의 x축 값이 같으면 도착
        isFinish = playerPos[POSITION_Y] == finishPos[POSITION_Y] and playerPos[POSITION_X] == finishPos[POSITION_X]

        if isFinish:
            print("탈출 성공!!")
            break    
        # 플레이어가 이동할 수 있는 방향을 파악하고 선택지를 표시 (4개의 선택지를 항상 표시)
        # selection = 1
        # selection = random.randrange(1,5)
        selection = displaySelection()

        # 사용자 선택의 유효성 파악
        # 1 ~ 4번은 유효, 0은 종료, -1 포함 나머지 숫자는 잘못 입력

        if selection < 0 or selection > 4:
            print("잘못 입력했습니다. 1~4까지의 숫자만 입력하세요.")
            time.sleep(2)
            continue

        if selection == 0:
            print("종료합니다")
            break

        # --- 사용자가 선택한 방향이 올바른 방향인지 확인 ----------
        # print("maxRow: ", maxRow)
        # print("maxCol: ", maxCol)

        validDict = checkValidDirection(selection)

        valid = validDict['valid']
        directionName = validDict['directionName']
        offset = validDict['offset']
        # errorMessage = ''

        if not valid:
            print(f"갈 수 없는 방향({directionName})")
            time.sleep(2)
            continue       
        
        # --- 플레이어가 선택한 방향으로 플레이어 이동 (상태를 변경) (플레이어를 어떻게 이동시킬지)
        playerPos[POSITION_Y] = playerPos[POSITION_Y] + offset[POSITION_Y]
        playerPos[POSITION_X] = playerPos[POSITION_X] + offset[POSITION_X]

        # playerPos는 두개의 항목을 갖는 리스트, 0번 인덱스는 y축 값, 1번 인덱스는 x축 값, [y,x]
        # 해당 좌표의 위치는 지도(map:[])의 좌표로 동기되어 있음
        
        # nextOffset = makePlayerOffsetWithSelection(selection)
        # playerPos[POSITION_Y] = playerPos[POSITION_Y] + nextOffset[POSITION_Y]
        # playerPos[POSITION_X] = playerPos[POSITION_X] + nextOffset[POSITION_X]
        # ---------------------------

        # 1 == 북 , 2 == 동 , 3 == 남, 4 == 서
        # if selection == 1:
        #     #북
        #     playerPos[POSITION_Y] = playerPos[POSITION_Y] + -1
        #     pass
        # elif selection == 2:
        #     # 동
        #     playerPos[POSITION_X] = playerPos[POSITION_X] + 1
        #     pass
        # elif selection == 3:
        #     # 남
        #     playerPos[POSITION_Y] = playerPos[POSITION_Y] + 1
        #     pass
        # elif selection == 4:
        #     # 서
        #     playerPos[POSITION_X] = playerPos[POSITION_X] + -1
        #     pass
        # elif selection == 0:
        #     print("종료합니다")
        #     break
        # else:
        #     print("잘못 입력했습니다. 1~4까지의 숫자만 입력하세요.")
        #     time.sleep(2)


        # playerPos[POSITION_Y] = playerPos[POSITION_Y] + -1
        # playerPos[POSITION_X] = playerPos[POSITION_X] + 0 

        # time.sleep(1)
        pass
    pass

    #         0        1      2      3 
    # offset ((-1,0), (0,1), (1,0), (0,-1))
    # 북 P(5,5) + O(-1,0) = M(4,5)
    # 동 P(5,5) + O(0,1) = M(5,6)
    # 남 P(5,5) + O(1,0) = M(6,5)
    # 서 P(5,5) + O(0,-1) = M(5,4)