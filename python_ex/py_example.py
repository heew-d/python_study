import time
import os

prompt = "문구를 입력하세요(최대 9자)"

print(prompt)
text = input()

if len(text)<9:
    text = "{0:#^9}".format(text)
else:
    text = text[0:9]

while True:
    print(text)
    text = text[1:] + text[:1]
    time.sleep(1)
    os.system('clear')
    
# textList = list(text)
# index=0
# while True:
#     os.system('clear')
#     print(''.join(textList))

#     temp = textList.pop(0)
#     textList.append(temp)
#     time.sleep(1) 
