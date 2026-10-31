def last_occurrence(P):
    L = {}

    for i in range(len(P)):
        L[P[i]] = i

    return L


def boyer_moore(T, P):
    n = len(T)
    m = len(P)

    L = last_occurrence(P)
    positions = []
    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0 and T[i + j] == P[j]:
            j -= 1

        if j == -1:
            positions.append(i)
            i += 1
        else:
            i += max(1, j - L.get(T[i + j], -1))

    return positions

text = input("text: ")
ptrn = input("pattern: ")

result = boyer_moore(text, ptrn)
print(ptrn)
print(text)
print(result)