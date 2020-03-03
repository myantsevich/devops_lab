# enter 2 numbers to one line
border = input().split()
left = int(border[0])
right = int(border[1])
result = [
    x for x in range(left, right + 1)
    if '0' not in str(x) and all((x % int(char) == 0 for char in str(x)))
]
print(result)

