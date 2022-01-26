def partition(arr, left, right):
    if right <= left: return
    
    pivot = arr[right]
    small = left-1
    for l in range(left, right):
        if arr[l] > pivot: continue
        else:
            small += 1
            arr[small], arr[l] = arr[l], arr[small]
    arr[small+1], arr[right] = arr[right], arr[small+1]
    
    print(*arr[left:small+1], "|", pivot, "|", *arr[small+2:right+1])

    partition(arr, left, small)
    partition(arr, small+2, right)


def solve():
    arr = list(map(int, input().split()))
    partition(arr, 0, len(arr)-1)
    print(*arr, sep=', ')

solve()

