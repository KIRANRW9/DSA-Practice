# Pattern 3: Triangle with Repeating Row Numbers
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
