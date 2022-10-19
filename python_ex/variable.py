
from copy import copy, deepcopy

#int a = 1;
a = 1
print('a: ', a)
a = 'a'
print('a: ', a)
a = {'k':'v'}
a = (1,2,3)
a = {1,2,3}
a = 3.14
a = [1,2,3]
print('a: ', a)

#참조(레퍼런스)
b = a 
print('b: ',b)

print('id(a): ', id(a))
print('id(b): ', id(b))

print('a is b: ', a is b)

c = [1,2,3]
print('a is c: ', a is c)
print('a == c: ', a == c)

b[0] = 5
print('b: ', b)
print('a: ', a)

# 복사 (얕은복사)
d = a[:]
print('id(a): ', id(a))
print('id(d): ', id(d))

# 복사 (얕은복사)
e = copy(a)
print('id(a): ', id(a))
print('id(e): ', id(e))

# 깊은복사
#deepcopy()

v1, v2 = (1, 2)
(v1, v2) = 1, 2
v1, v2 = [1, 2]
[v1, v2] = 1, 2

v1 = v2 = 'a'
print('id(v1): ', id(v1))
print('id(v2): ', id(v2))

var1 = [1,2,3]
var2 = [1,2,3]
print('id(var1): ', id(var1))
print('id(var2): ', id(var2))

tup1 = (1,2,3)
tup2 = (1,2,3)
print('id(tup1): ', id(tup1))
print('id(tup2): ', id(tup2))

li = [100,[10,20,30]]
li2 = li #참조
licp = li[:] #복사
licp2 = copy(li) # 복사
lidcp = deepcopy(li) #깊은복사

print('id(li) 원본: ', id(li)) #원본
print('id(li2) 참조: ', id(li2)) #참조
print('id(licp) 복사: ', id(licp)) #복사
print('id(licp2) 복사: ', id(licp2)) #복사
print('id(lidcp) 깊은복사: ', id(lidcp)) #깊은복사

print('id(li) 원본: ', id(li[1])) #원본
print('id(li2) 참조: ', id(li2[1])) #참조
print('id(licp) 복사: ', id(licp[1])) #복사
print('id(licp2) 복사: ', id(licp2[1])) #복사
print('id(lidcp) 깊은복사: ', id(lidcp[1])) #깊은복사