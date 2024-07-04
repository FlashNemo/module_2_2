first = 1
second = 2
third = 3
if first == second and first == third :
    print(3)
elif second == first or second == third:
    print(2)
elif first == second or first == third:
    print(2)
else:
    print(0)