from lib2to3.pytree import type_repr
from os import sep


print("hello")

integer = 10
double = 10.10
integer2 = -10
double2 = -10.10

print("숫자 integer:", integer)
print("숫자 double:", double)
print("숫자 integer2:", integer2)
print("숫자 double2:", double2)


# 문자 : 단 하나의 문자만, 문자열 : 하나의 문자가 다수의 문자열로 나열된 것

print("쌍따옴표를 표시하는 방법으로 \"서식문자\"")
print("줄내림 역시도 서식문자로\n표현이 가능합니다")

print('''
이렇게 줄내림을 해두면
명시적으로 우리 눈에서 이해가 쉽기에
사용하면 가독성에 도움을 줄 수 있다.
''')

print("="*50)
print("하나의 문자열"*2)
print("="*50)

print("이 문장의 길이는 몇일까? len :", len("이 문장의 길이는 몇일까?"))

text = "문자열로써 인덱싱을 하는데 사용할 문자열"

# str = text[0:4]
# print("str:",str)

format = "%10s" % "12345"
print("format: ", format, sep="")

format = "%010.2f" % 3.14
print("format: ", format, sep="")

print("1: 점프 투 {0}{1} 프로그래밍".format("파", "이썬"))
print("2: 점프 투 {0}{name} 프로그래밍".format("파", name="이썬"))

print("{0:#<10}끝".format("12345"))

print("{0:10.2f}끝".format(3.14))

print("{{}}".format())

name = "희원"
lastname = "두"
print(f'{name},{lastname}, {{}}')

print(f'{name:>10}')

print(f'{12345.14:010.5f}')

a = "aaabbbccc"
b = 'aaabbbccc'
c = str('aaabbbccc')

print("a의 개수: ", a.count('a'))
print("b의 개수: ", b.count('b'))
print("c의 개수: ", c.count('c'))

# print("type a: ", type(a))
# print("type b: ", type(b))
# print("type c: ", type(c))

print("b값의 인덱스:", a.find('b'))
print("b값의 인덱스:", a.index('b'))

try:
    print("b값의 인덱스:", a.index('z'))
except: 
    print("오류:")

print("계속진행")

print("join: ", "#".join("asdf"))
print("join: ", "-".join(['010','1234','5678']))

print("upper: ", "a".upper())
print("lower: ", "B".lower())

print("lower: ", "google@GMAIL.COM".lower())

print("lstrip:", "  google@GMAIL.COM".lower().lstrip(), sep="")
print("rstrip:", "google@GMAIL.COM         ".lower().rstrip()+"끝", sep="")
print("strip:", "            google@GMAIL.COM         ".lower().strip()+"끝", sep="")
print("replace:", "            google@GMAIL.COM         끝".replace(" ", ""), sep="")

print("replace : ", "asdfasdf".replace("s", "w"), sep="")
print("replace : ", "asdfasdf".replace("s", "w",1), sep="")

print("join: ", "".join(["0","1","2"]))
print("split: ", "0,1,2".split(","))

split = "google@gmail.com".split("@")
id = split[0]
domain = split[1]

print("id: ",id,sep="")
print("domain: ",domain,sep="")