userInput = input()
if len(userInput) == 1:
    print(userInput.upper())
else:
    print(userInput[0].upper()+userInput[1:-1] + userInput[-1])
