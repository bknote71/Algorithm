s = input()

insertions = 0

for i, char in enumerate(s):
    if (i + insertions) & 1 == 0 and char != "i":
        insertions += 1
    elif (i + insertions) & 1 == 1 and char != "o":
        insertions += 1


if (len(s) + insertions) & 1 == 1:
    insertions += 1

print(insertions)
