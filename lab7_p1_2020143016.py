import re
txtfile = open("input_7_1.txt","r")
txtfileByLine = []
for line in txtfile:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    txtfileByLine.append(line)
txtfile.close()
#print(txtfileByLine)
lineContain_a = []
lineContain_b = []
lineContain_123 = []
lineDefa = 0
lineDefb = 0
lineDefd = 0
for lineNumber in range(len(txtfileByLine)):
    if re.search("def a",txtfileByLine[lineNumber]) != None:
        lineDefa = lineNumber+1

for lineNumber in range(len(txtfileByLine)):
    if re.search("def b",txtfileByLine[lineNumber]) != None:
        lineDefb = lineNumber+1

for lineNumber in range(len(txtfileByLine)):
    if re.search("def define123",txtfileByLine[lineNumber]) != None:
        lineDefd = lineNumber+1

for lineNumber in range(len(txtfileByLine)):
    if re.search("a\(.*\)",txtfileByLine[lineNumber]) != None:
        if lineNumber+1 != lineDefa:
            lineContain_a.append(lineNumber+1)
            
for lineNumber in range(len(txtfileByLine)):
    if re.search("b\(.*\)",txtfileByLine[lineNumber]) != None:
        if lineNumber+1 != lineDefb:
            lineContain_b.append(lineNumber+1)

for lineNumber in range(len(txtfileByLine)):
    if re.search("define123\(\)",txtfileByLine[lineNumber]) != None:
        if lineNumber+1 != lineDefd:
            lineContain_123.append(lineNumber+1)

print("a: def in "+str(lineDefa)+", calls in "+str(lineContain_a))
print("b: def in "+str(lineDefb)+", calls in "+str(lineContain_b))
print("define123: def in "+str(lineDefd)+", calls in "+str(lineContain_123))