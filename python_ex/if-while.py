# if (조건이 참이라면){
#     몸통의 로직을 처리
# }

import os
import time

money = 9000
health = 50

if money >= 10000 or (health <= 50 and money>=5000):
    print("택시를 타고 가라")
else:
    print("걸어 가라")

if money >= 10000:
    print("택시를 타고 가라")
elif health <= 50:
    print("힘드니까 택시를 타고 가라")
else:
    print("걸어 가라")


if 1 in [1,2,3]:
    print("[1,2,3] 안에 1이 포함")

if 4 not in [1,2,3]:
    print("[1,2,3] 안에 4가 미포함")

print("="*50)

# while문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다.")
    # if treeHit == 10:
    #     print("나무 넘어갑니다.")
if treeHit == 10:
    print("나무 넘어갑니다.")

os.system('clear')

prompt = "다음 행동을 선택해주세요(1~4)"
selection = """
1. Add
2. Del
3. List
4. Quit
"""

number = 0
while number != 4:
    # os.system('clear')
    print(selection)
    print(prompt)
    number = int(input())
    if number < 0 or number > 4:
        print("허용되지 않는 입력입니다.")
        time.sleep(1)
        continue

print("종료되었습니다")