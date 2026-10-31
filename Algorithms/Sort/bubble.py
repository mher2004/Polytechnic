from random import randint
a = [randint(0,500) for i in range(10)]
print(a)

def bubble(a):
    for i in range(1,len(a)-1):
        for j in range(len(a)-i):
                if a[j] > a[j+1]:
                        a[j], a[j+1] = a[j+1],a[j]

bubble(a)
print(a)
