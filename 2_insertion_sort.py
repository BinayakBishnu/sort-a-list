L = [2, 5, 131, 735, 12, 4, 46, 1, 52, 9]
print(L)

for i in range(1, len(L)):
    min_ = L[i]

    j = i-1
    while min_ < L[j]:
        L[j+1] = L[j]
        j -= 1
        if j < 0:
            break

    L[j+1] = min_

    print(L)

print(L)
