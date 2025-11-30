letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = 1
idx = 0

for i in range(1, 6):
    for j in range(i):
        if j % 2 == 0:
            print(letters[idx], end="")
            idx += 1
        else:
            print(num, end="")
            num += 1
    print()