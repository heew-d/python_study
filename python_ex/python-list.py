arr = [0,"1",2,"3"]
print(arr)

# print(arr[0] + arr[2])
# print(arr[1] + arr[0])

# print("join:", ''.join(arr))

# f'{arr[1]}{arr[0]}'


arr2 = [0,"1",2,[100,200,300]]
print(arr2)
print(arr2[3][1])


arr3 = ["h","e","l","l","o"]
arr4 = ["w","o","r","l","d"]

# print(arr3[:])
print(arr3 + arr4)
print(len(arr3 + arr4))
print(str(arr2[0]) == 0)
print(type(str(arr2[0])))

arr3[2] = "w"
print("edit:", arr3)

del arr3[2]
print("del:", arr3)

arr3.append("w")
print("append:", arr3)

arr3.insert(2, "r")
print("insert:", arr3)

# 클리어 모두 삭제 []
# arr3.clear()
# v = arr3.pop(0)

sorting = [0,1,2,2,2,2,3,4,5,6,7,8,9]
sorting.sort()
print("sorting:", sorting)

sorting.sort(reverse=True)
print("sorting:", sorting)

sorting.sort(reverse=False)
print("sorting:", sorting)

sorting.reverse()
print("sorting:", sorting)

# 없는 인덱스 참조시 예외발생 (try로 잡아줘야함)
# sorting.index(10)

# print("sorting111:", sorting)

# 해당 인덱스를 삭제
del sorting[2]
# 값이 동일한 항목을 삭제 (낮은 인덱스의 값만 제거)
sorting.remove(2)
print("remove:", sorting)

p = sorting.pop(2)
print("pop:", sorting)
print("p:", p)

sorting.extend([100,200])
print("sorting extend:", sorting)

tup = (0,1,2,3,4,5)
# list(tup)[2] = 10

# 6x6
# [ 
# [0,0,0,0,0,0]
# [0,0,1,0,0,0]
# [0,1,0,1,0,0]
# [0,1,0,1,0,0]
# [0,1,0,1,0,0]
# [0,0,1,0,0,0]
# ]

# 6x6 
# [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
