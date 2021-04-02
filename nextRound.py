
n, k = map(int, input().split())
scoreList = list(map(int, input().split()))
countContestants = 0
for i in scoreList:
    if i >= scoreList[k-1] and i != 0:
        countContestants += 1

print(countContestants)