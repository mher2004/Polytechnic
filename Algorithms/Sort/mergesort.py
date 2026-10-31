from random import randint
a = [randint(0,500) for i in range(10)]
print(a)

def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    l1 = a[p : q + 1]
    l2 = a[q + 1 : r + 1]
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            a[k] = l1[i]
            i += 1
        else:
            a[k] = l2[j]
            j += 1
        k += 1
    while i < n1:
        a[k] = l1[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = l2[j]
        j += 1
        k += 1

merge_sort(a, 0, len(a)-1)
print(a)