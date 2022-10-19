import time
import os
prompt = "문구를 입력하세요(최대 9자)"

print(prompt)
text = input()

if len(text)<9:
    text = "{0:#^9}".format(text)
else:
    text = text[0:9]

    
textList = list(text)
direction = 1
n = 0
while True:
    os.system('clear')
    print(''.join(textList))

    #버블정렬
    #Swap(교환)
    nextIdx = n+direction
    temp1, temp2 = (textList[n], textList[nextIdx])
    textList[n], textList[nextIdx] = (temp2, temp1)

    n = nextIdx % (len(textList) - 1)

    time.sleep(1)

    
    # textList[index],textList[index+1] = textList[index+1], textList[index]
    # print(''.join(textList))
    # time.sleep(1) 
    # index = index + 1