# use pattern 2+3=5 for input
import re
hometask = input()
r = re.search(r'(\d+)(\s+)?([+|/|-|*])(\s+)?(\d+)(\s+)?=(\s+)?(\d+)', hometask)

if not r:
    print('ERROR')
else:
    expected = eval(f'{r.group(1)}{r.group(3)}{r.group(5)}')
    if expected == int(r.group(8)):
        print('YES')
    else:
        print('NO')
