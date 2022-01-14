L = [2, 5, 131, 735, 12, 4, 46, 1, 52, 9]
print(L)

for i in range(len(L)):
    min_id = i

    for j in range(i+1, len(L)):
        if L[j] < L[min_id]:
            min_id = j

    L[min_id], L[i] = L[i], L[min_id]

    print(L)

print()
print(L)
