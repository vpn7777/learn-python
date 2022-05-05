myList = list(map(int, input().split()))
minN = []
for i in range(len(myList)):
    if myList[i] > 0:
        minN.append(myList[i])
print(min(minN))
