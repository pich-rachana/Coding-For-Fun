userInput = input()
ListOfUserInput = list(map(int, userInput.split('+')))
ListOfUserInput.sort()
ans = ''
for number in ListOfUserInput:
    ans += str(number) + '+'
print(ans[:-1])