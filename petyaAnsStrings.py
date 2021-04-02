Str1 = input().lower()
Str2 = input().lower()
output = 0
for i in range(len(Str1)):
    if Str1[i] != Str2[i]:
        if ord(Str1[i]) > ord(Str2[i]):
            output = 1
        elif ord(Str1[i]) < ord(Str2[i]):
            output = -1
        break
    else:
        continue
print(output)
