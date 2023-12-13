txtfile = open("input_7_2.txt","r")
txtfileByLine = []
for line in txtfile:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    txtfileByLine.append(list(line.upper()))
wholetxtfile = []
for line in txtfileByLine:
    wholetxtfile = wholetxtfile + line
#print(wholetxtfile)
aList = [chr(i) for i in range(ord('A'),ord('Z')+1)]
alfabetDict = {}
for alfabet in aList:
    alfabetCount = wholetxtfile.count(alfabet)
    if alfabetCount != 0:
        alfabetDict[alfabet] = alfabetCount
lst = alfabetDict.items()
lst2 = [] # 정렬된 수
lst3 = [] # 정렬안된 수 
lst4 = [] # 정렬안된 알파벳
realList = []
for i in lst:
    lst2.append(i[1])
for i in lst:
    lst3.append(i[1])
for i in lst:
    lst4.append(i[0])
lst2.sort(reverse=True)
for i in range(len(lst2)):
    for k in range(len(lst3)):
        if lst2[i] == lst3[k] and lst4[k] not in  realList:
            realList.append(lst4[k])
print(realList)


