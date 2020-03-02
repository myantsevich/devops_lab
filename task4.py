number_of_commands = int(input())
array = []

for i in range(number_of_commands):
    command = input()
    command = command.split()
    args = [] if len(command) == 1 else [int(x) for x in command[1:]]
    command = command[0]
    if command == 'print':
        print(array)
    else:
        func = getattr(array, command)
        func(*args)
