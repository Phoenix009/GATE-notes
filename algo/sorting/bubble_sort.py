def bubble_sort(arr):
    for i in range(len(arr)):
        print(*arr)
        swap_flg = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]: 
                swap_flg = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swap_flg: break

def solve():
    arr = list(map(int, input().split()))
    bubble_sort(arr)

solve()



