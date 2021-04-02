n = eval(input())
ans = 0

for i in range(n):
    a,b,c = map(int, input().split())
    count = 0
    if a == 1:
        count += 1
    if b == 1:
        count +=1
    if c == 1:
        count += 1
    if count >= 2:
        ans += 1
print(ans)