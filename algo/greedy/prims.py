MAX = 10**9

def prims(graph, n):
    tree = []   # The minimum spanning tree edges will be stored
    tree_cost = 0    # Keeps track of the minimum cost of the spanning tree
    nearest_src = [None for i in range(n)]  # Keeps track of the nearest source from the formed tree
    
    min_edge, min_cost = None, MAX
    for src in range(1, n+1):
        for dest in range(1, n+1):
            if graph[src-1][dest-1] < min_cost:
                min_cost = graph[src-1][dest-1]
                min_edge = (src, dest)

    msrc, mdest = min_edge
    tree.append(min_edge)
    tree_cost += min_cost
    nearest_src[msrc-1] = 0
    nearest_src[mdest-1] = 0

    min_edge, min_cost = None, MAX
    for dest in range(1, n+1):
        if nearest_src[dest-1] == 0: continue
        
        if graph[msrc-1][dest-1] < graph[mdest-1][dest-1]: nearest_src[dest-1] = msrc
        else: nearest_src[dest-1] = mdest

        if graph[msrc-1][dest-1] < min_cost:
            min_cost = graph[msrc-1][dest-1]
            min_edge = (msrc, dest)

        if graph[mdest-1][dest-1] < min_cost:
            min_cost = graph[mdest-1][dest-1]
            min_edge = (mdest, dest)

    for _ in range(n-2):
        msrc, mdest = min_edge
        tree.append(min_edge)
        tree_cost += min_cost
        nearest_src[mdest-1] = 0

        min_edge, min_cost = None, MAX
        for dest in range(1, n+1):
            if nearest_src[dest-1] == 0: continue

            if graph[mdest-1][dest-1] < graph[nearest_src[dest-1]-1][dest-1]:
                nearest_src[dest-1] = mdest

            if graph[msrc-1][dest-1] < min_cost:
                min_cost = graph[msrc-1][dest-1]
                min_edge = (msrc, dest)

            if graph[mdest-1][dest-1] < min_cost:
                min_cost = graph[mdest-1][dest-1]
                min_edge = (mdest, dest)

    return tree


def solve():
    n, m = map(int, input().split())
    graph = [[MAX for j in range(n)] for i in range(n)]

    for _ in range(m):
        src, dest, wt = map(int, input().split())
        graph[src-1][dest-1] = wt
        graph[dest-1][src-1] = wt

    min_span_tree = prims(graph, n)
    
    for src, dest in min_span_tree:
        print(src, dest, graph[src-1][dest-1])

solve()
