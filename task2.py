# enter numbers separeted by spaces
input_string = input()
List1 = input_string.split()

input_string = input()
List2 = input_string.split()

Set1 = set(List1)
Set2 = set(List2)

Outputlist = [int(x) for x in Set1 & Set2]
Outputlist.sort()
print(" ".join(str(x) for x in Outputlist))
