def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j > -1 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

def solve():
    arr = list(map(int, input().split()))
    insertion_sort(arr)
    print(*arr, sep=', ')

solve()
