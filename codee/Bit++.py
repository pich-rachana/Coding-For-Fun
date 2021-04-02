n = int(input())
ans = 0
for row in range(n):
    userInput = input()
    if userInput == '++X' or userInput == 'X++':
        ans += 1

    if userInput == '--X' or userInput == 'X--':
        ans -= 1
print(ans)