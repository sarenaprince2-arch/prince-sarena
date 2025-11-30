for i in range(1, 6):
    # Increasing numbers
    for j in range(i, i + i):
        print(j, end="")
    # Decreasing numbers
    for j in range(i + i - 2, i - 1, -1):
        print(j, end="")
    print()