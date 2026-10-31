def naive_match(T, P):
    n = len(T)
    m = len(P)
    shifts = []

    for s in range(n - m + 1):
        j = 0

        while j < m and T[s + j] == P[j]:
            j += 1

        if j == m:
            shifts.append(s)

    return shifts

text = input("text: ")
ptrn = input("pattern: ")

result = boyer_moore(text, ptrn)
print(ptrn)
print(text)
print(result)