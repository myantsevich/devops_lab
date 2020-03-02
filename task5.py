# enter 2 numbers, every from new line
left = int(input())
right = int(input())
result = [
    x for x in range(left, right + 1)
    if '0' not in str(x) and all((x % int(char) == 0 for char in str(x)))
]
print(result)
