import os
import time
import random

class MazeMap():

    # 속성, 지도 행렬
    # 함수, 파일에서 지도를 불러오기
    # 함수, 유효성 확인

    # 함수, 지도 표시

    def __init__(self, filePath = '') -> None:
        self.map:list = []
        self.maxCol = 0
        self.maxRow = 0
        self.startPos = MazePosition(0,0,"S")
        self.finishPos = MazePosition(0,0,"F")

        self.loadMap(filePath)

        pass

    def getTile(self, y, x):
        return self.map[y][x]

    def getLine(self, y):
        return self.map[y]

    # 함수, 파일에서 지도를 불러오기
    def loadMap(self, filePath):

        try:
            # 형렬, 매트릭스
            # with open('./MAZE_PY/level1.map', 'r') as f:
            with open(filePath, 'r') as f:

                self.map.clear()
                # for in  #명확한 제한이 존재할때
                y=0
                while True:
                    line = f.readline().replace('\n','').replace(' ','')

                    # None 일땐 종료
                    if not line:
                        break

                    self.map.append(line)
                    # 해당 문자열안에 S나 F가 있는지 파악하고, 해당 문자의 위치가 어딘지 파악
                    # 알아낸 위치가 곧 x축의 위치
                    # str.find() 해당 문자가 있으면 문자의 위치(인덱스)를 리턴하고, 없으면 -1을 리턴

                    findedIndex = line.find('S')
                    if -1 < findedIndex: 
                        # 시작위치 파악, 기억
                        self.startPos.setPosition(y, findedIndex) #값을 설정
                        pass
                    
                    findedIndex = line.find('F')
                    if -1 < findedIndex:
                        # 종료위치 파악, 기억
                        self.finishPos.setPosition(y, findedIndex) #값을 설정
                        pass

                    self.maxCol = len(line)
                    y = y + 1
                    pass
                
                self.maxRow = y
                pass

        except FileNotFoundError as e:
            print("FileNotFoundError error: ", e)
            pass
        except:
            print("알 수 없는 error")
            pass


    # 갈 수 있는 길인지 검사
    def validation(self, y, x):

        valid = True
        # 해당 위치(y,x)의 타일 값을 읽어옴
        # 1참 -> y가 유요한 범위인지
        valid = valid and (y >= 0 and y < self.maxRow)
        # 2참 -> x가 유효한 범위인지
        valid = valid and (x >= 0 and x < self.maxCol)
        
        if not valid:
            return False

        # tile = mazeMap.map[yIndex][xIndex]
        tile = mazeMap.getTile(y, x)
    
        # 3참 -> 유효한 타일인지
        # valid = valid and (tile == 'o' or tile == 'S' or tile == 'F')
        valid = valid and (tile in 'oSF')
        
        return valid
    pass

# 2차원 좌표값 저장, 아이콘
class MazePosition():
    def __init__(self, y, x, icon) -> None:
        self.y = y
        self.x = x
        self.icon = icon
        pass

    def __str__(self) -> str:
        return f'[{self.icon}] (y: {self.y}, x: {self.x})'

    def __eq__(self, __o: object) -> bool:
        if type(self) != type(__o):
            return False
        return self.y == __o.y and self.x == __o.x

    def setPosition(self,y,x):
        self.y = y
        self.x = x

    def move(self, offset):
        self.y = self.y + offset.y
        self.x = self.x + offset.x
    pass

class MazeOffset():
    def __init__(self,y,x, name) -> None:
        self.y = y
        self.x = x
        self.name = name
        pass

mazeMap = MazeMap()
playerPos = MazePosition(0,0,"P")

# 지도 표시
def display():

    # 지도 및 플레이어의 현재위치
    for y in range(mazeMap.maxRow):
        for x in range(mazeMap.maxCol):

            tile = mazeMap.getTile(y,x)
            if playerPos.y == y and playerPos.x == x:
                # 현재타일은 플레이어의 위치
                print(playerPos.icon, end=' ')
            else:
                # 플레이어 위치가 아닌 일반 타일
                print(tile, end=' ')
        print()

    print("플레이어: ",playerPos)
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
    mazeMap.loadMap('./MAZE_PY/level1.map')

    # mapLevel2 = MazeMap('./level2.map')
    # mapLevel3 = MazeMap('./level3.map')
    startPos = mazeMap.startPos
    
    #플레이어의 현재위치를 지도의 시작위치로 설정 (표시x, 기록만)
    playerPos.setPosition(startPos.y, startPos.x)

    pass



# offsets = ((-1,0), (0,1), (1,0), (0,-1))

northOffset = MazeOffset(-1, 0, '북')
eastOffset = MazeOffset(0, 1, '동')
southOffset = MazeOffset(1, 0, '남')
westOffset = MazeOffset(0, -1, '서')

OFFSETS = (
    northOffset,
    eastOffset, 
    southOffset,
    westOffset
)

# 다수의 값을 넣을 수 있는 자료형
# 리스트, 튜플, 딕셔너리

def checkValidDirection(selection):
    valid = False

    offset = OFFSETS[selection - 1]

    yIndex = playerPos.y + offset.y
    xIndex = playerPos.x + offset.x
    valid = mazeMap.validation(yIndex, xIndex)

    resultDict = {
        'valid' : valid,
        'offset' : offset,
    }
    return resultDict

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
        # isFinish = playerPos.y == finishPos.y and playerPos.x == finishPos.x
        # if isFinish:
        if playerPos == mazeMap.finishPos:
            print("탈출 성공!!")
            break    
        # 플레이어가 이동할 수 있는 방향을 파악하고 선택지를 표시 (4개의 선택지를 항상 표시)
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
        offset = validDict['offset']
        directionName = offset.name
        # errorMessage = ''

        if not valid:
            print(f"갈 수 없는 방향({directionName})")
            time.sleep(2)
            continue       
        
        # --- 플레이어가 선택한 방향으로 플레이어 이동 (상태를 변경) (플레이어를 어떻게 이동시킬지)
        playerPos.move(offset)
        
        pass
    pass
