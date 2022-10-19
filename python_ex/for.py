# 기본구조
# for 조건 in 나열가능한 다수의 항목이 들어있는 자료형 :
#     pass

li = ["one", "two", "three"]

for i in li:
    print(i)


li = [(1,2), (3,4), (5,6)]

for (first, last) in li:
    print(first + last)


marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print(f"{number}번 학생 축하합니다. 합격입니다.")

add = 0 
for i in range(1,11):
    print(i)
    add = add + i

print(add)

# 구구단
for i in range(2,10):
    print(f'{i}단: ', end=" ")
    for j in range(1,10):
        print(i*j, end=" ")
    print('')

# 리스트 내포 사용하기
li = [1,2,3,4]
result = []
for num in li:
    result.append(num*3)
print('result: ', result)

# result.clear()
# result.extend([num*3 for num in li])

# 리스트에서 꺼낸 값에 3을 곱해 리스트에 담음
result = [num*3 for num in li]
print('result2: ', result)

# 2의 배수 값만 *3해서 리스트에 담음
result = [num*3 for num in li if num % 2 == 0]
print('result3: ', result)

result = [x*y for x in range(2,10) for y in range(1,10)]
print('result4: ', result)
