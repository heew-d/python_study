# f = open('newfile.txt', 'w')
# f.close()

# f = open('c:/doit/newfile.txt', 'w')
# f.close()

# 파일 쓰기
# f = open('newfile.txt','w')
# for i in range(1,11):
#     data = f'{i}번째 출력입니다.\n'
#     f.write(data)
# f.close()

# 파일 읽기(첫 번째 줄)
# f = open('newfile.txt', 'r')
# line = f.readline()
# print(line)
# f.close()


# 파일 읽기 (모든 줄)
# f = open('newfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     # if not f.readable: break
#     print(line, end='')
# f.close()

# 모든 줄을 읽어 각 줄을 요소로 갖는 리스트로 반환
# f = open('newfile.txt', 'r')
# lines = f.readlines()
# for line in lines:
#     print(line, end='')
# f.close()


# 파일 내용 전체를 문자열로 반환
# f = open('newfile.txt', 'r')
# data = f.read()
# print(data)
# f.close()

# 추가
# f = open('newfile.txt', 'a')
# for i in range(11,20):
#     data = f'{i}번째 출력입니다.\n'
#     f.write(data)
# f.close()


# f = open('newfile2.txt', 'r')
# f.close()

try:
    with open('newfile2.txt', 'w') as f:
        f.write("Life is too short, you need python")
    with open('newfile2.txt', 'r') as f:
        print('with as문 open file', f.read())
except:
    print('error')


# file = open(path, 'r', encoding='utf-8')