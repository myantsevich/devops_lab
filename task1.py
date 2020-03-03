# enter a year without spaces and letters
year = int(input())
print('True' if year % 4 == 0 and (year % 100 != 0 or year % 100 and year % 400) else 'False')
