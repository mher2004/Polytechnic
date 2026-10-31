from random import randint
a = [randint(0,500) for i in range(10)]
print(a)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertion_sort(a)
print(a)
