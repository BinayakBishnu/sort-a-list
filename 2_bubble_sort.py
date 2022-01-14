L = [2, 5, 131, 735, 12, 4, 46, 1, 52, 9]
print(L)

for i in range(len(L)):

    for j in range(len(L)-i-1):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]

print(L)