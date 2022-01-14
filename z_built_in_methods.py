L1 = [1, 4, 2, 6, 8, 2, 5, 74, 42, 252, 57, 2, 632, 743, 15]

print('Integers ascending')
L1.sort()
print(L1)
print('Integers descending')
L1.sort(reverse=True)
print(L1)


print()
L2 = ['abc', 'fweg', 'f', 'yjbrfs']

print('Strings ascending')
L2.sort()
print(L2)

print('String length ascending')
L2.sort(key=len)
print(L2)

print('String 2nd letter ascending')
L2.sort(key=lambda a: a[1] if len(a) >1 else a[0])
print(L2)
