
def add(a,b):
    return a+b

sum = add(10,20)
print(sum)

i1, i2 = (300, 400)
sum = add(i1,i2)
print(sum)

func1 = add # func1 변수에 add 함수의 설계를 대입
sum = func1(i1*10, i2*10) # func1을 호출하여 add 함수를 호출한 효과를 갖는다
print(sum)

def act1():
    print('act1')
    pass
def act2():
    print('act2')
    pass
def act3():
    print('act3')
    pass
def action(action, actions):
    actions[action]()

actions = [act1, act2, act3]
actionIndex = 2
action(actionIndex, actions)


#여러 개의 입력값을 받는 함수
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

sum = add_many(1,2,3,4,5,6,7,8,9,10)
print(sum)



def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    if choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

resultAdd = add_mul('add', 1,2,3,4,5,6,7,8,9,10)
resultMul = add_mul('mul', 1,2,3,4,5,6,7,8,9,10)

print(resultAdd)
print(resultMul)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name='foo', age=3)
print_kwargs(a=1)

def print_kwargs2(p1,**kwargs):
    print(kwargs)

print_kwargs2('p1', name='foo', age=3)
print_kwargs2(name='foo', age=3, p1='p1')

def print_kwargs3(p1, *args, **kwargs):
    print(f'p1:{p1}, args: {args}, kwargs: {kwargs}')

print_kwargs3(1, 'hello', 'world', name='jk', age=999)
print_kwargs3(name='jk', age=999, p1=1, args=('hello', 'world'))


def say_myself(name, old, man=True):
    print(f"나의 이름은 {name} 입니다.")
    print(f"나이는 {old}살입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)


#글로벌 변수의 효력 범위
a = 1

# def vartest(a):
#     a = a+1
#     print('vartest a: ', a)
# vartest(a)
# print('a:',a)

#글로벌 a변수를 가져와서 값을 변경하는 것이 목적
# def vartestGlobal():
#     global a
#     a = a+1

# vartestGlobal()
# print('a: ',a)


def vartestReturn():
    b = a+1
    return b
    
a = vartestReturn()
print('a: ',a)