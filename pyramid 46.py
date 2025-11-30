nums = [5, 3, 1]

for i in range(1, 6):
    idx = 0
    for j in range(i):
        if j % 2 == 0:
            print(nums[idx], end="")
            idx += 1
        else:
            print("#", end="")
    print()