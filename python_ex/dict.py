# K:V

dic = {
    'name':'재권', 
    'lastName':"이", 
    'phone':'01099070317', 
    'year': 2022, 
    'day': 17, 
    'month':10,
    'date': [2022,10,17]
}

print("name: ", dic['name'])
print(f'date: {dic["date"][0]}-{dic["date"][1]}-{dic["date"][2]}')

dic['phone'] = '010xxxx####'
print("dic[phone]: ", dic['phone'])

dic['add'] = 'addItem'
print("dic[add]: ", dic['add'])

print("dic.keys: ", dic.keys())
print("dic.keys list: ", list(dic.keys()))

print("dic.values: ", dic.values())

# dic.clear()

# dic["empty"]
empty = dic.get("empty")
print("dic empty: ", empty)

if empty == None:
    dic["empty"] = "비었네"

empty = dic.get("empty")
print("after dic empty: ", empty)

print('address in dic.keys', 'address' in dic)
print('empty in dic.keys', 'empty' in dic)


print('"text" in "google drive nice"', ' ' in "google drive nice")
print('item in []', 'goo' in ["google", "drive", "nice"])

# for i in ["google", "drive", "nice"]:
#     print(i)

# for c in "google drive nice":
#     print(c)

# set은 집합이고, 집합의 특징으로 순서가없다, 중복을 허용하지 않음
set([])
set(())
set("")

s1 = set([1,2,3])
s2 = set([2,3,4,5,6])
print('s1: ', s1)
print('list(s1): ', list(s1))
print('tup(s1): ', tuple(s1))

print("s1 & s2", s1 & s2)
print("s1.intersection(s2)", s1.intersection(s2))
print("s1 | s2", s1 | s2)
print("s1.union(s2)", s1.union(s2))
print("s1 - s2", s1 - s2)
print("s2 - s1", s2 - s1)
print("s2.difference(s1)", s2.difference(s1))
print("s1.difference(s2)", s1.difference(s2))

s1.add(10)
print("s1.add(10)", s1)

s1.update((20,30,40))
print("s1.update((20,30,40))", s1)

s1.remove(40)
print("s1.remove(40)", s1)

boolTrue = True
boolFalse = False

name = ""

if name.strip():
    # upload
    pass


num = -1

if num:
    pass


todo = ["work", "rest", "sleep", "wakeup"]
print(todo)

while todo:
    act = todo.pop(0)
    print("act:", act)
    pass

print(todo)

# ""
# ''
