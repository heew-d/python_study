import sys
from copy import deepcopy

# "finish" : "F"
# "start" : "S"
# "player" : "P"
# "road" : "o"
# "wall" : "x"

# map 출력, readlines 함수 사용하여 각 줄을 요소로 갖는 리스트로 반환
file = open('./MAZE_PY/level1.map', 'r', encoding='utf-8')
lines=file.readlines()
for line in lines:
    print(line, end='')
print("")

# 현재위치 저장
start = 'S'
# 현재위치 row, col 구하기
for i in range(len(lines)):
    if start in lines[i]:
        startRow = i
        startCol = lines[i].find(start)
    # startRow = [i for i in range(len(lines)) if "S" in lines[i]]

# 현재 플레이어 위치
row = startRow
col = startCol

print(f'현재 플레이어: ([P] row: {row}, col: {col})')

# prompt = '''
# 1. 동쪽으로 이동
# 2. 서쪽으로 이동
# 3. 남쪽으로 이동
# 4. 북쪽으로 이동
# '''
# print(prompt)

# # 입력받을 숫자
# keyInput = int(input("어느 방향으로 이동하시겠습니까? (숫자만 가능)"))
# if keyInput == 1:
#     pass
# elif keyInput == 2:
#     pass
# elif keyInput == 3:
#     pass
# elif keyInput == 4:
#     pass
# else:
#     print("1~4사이의 숫자만 입력하시오.")

# file.close()