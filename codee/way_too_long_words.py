n = eval(input())
for i in range(n):
    userInput = input()
    if len(userInput) > 10:
        ans = userInput[0] + str(len(userInput)-2) + userInput[-1]
        print(ans)
    else:
        print(userInput)