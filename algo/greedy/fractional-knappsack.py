def solve():
    n, capacity = map(int, input().split())
    items = []

    for i in range(n):
        items.append(tuple(map(int, input().split())))
    
    ans = fractional_knappsack(n, m, items)

    print(ans)

solve()



def fractional_knappsack(n_items, capacity, items):
    cost_per_weight = lambda item: item.value / item.weight
    items.sort(key=cost_per_weight, reverse = True)

    ans = 0
    for item in items:
        taking = min(item.weight, capacity)
        capacity -= taking
        ans += taking * cost_per_weight(item)

    retur ans
