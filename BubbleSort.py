def bubblesort(l):
    for index in range(len(l)-1,0,-1):
        for low in range(index):
            if l[low] > l[low+1]:
                tmp = l[low+1]
                l[low+1] = l[low]
                l[low] = temp
    return l

if __name__ == '__main__':
    from random import shuffle
    l = range(15)
    lcopy = l[:]
    shuffle(l)
    print('Unsorted')
    print(l)
    assert l != lcopy
    print('Sorted')
    print (bubblesort(l))
    assert l == lcopy
