
def matrix_chain(matrices, n):
    cost = lambda A, B: A[0] * A[1] * B[1]
    new_dimensions = lambda A, B: (A[0], B[1])

    dp = [new_dimensions(i, j) for i, j in zip(matrices, matrices[1:])]
    cost_dp = [cost(i, j) for i, j in zip(matrices, matrices[1:])]
    
    for length in range(3, n+1):
        print(cost_dp)
        print(dp)
        print()

        new = []
        new_cost = []
        for j in range(n-length+1):
            c = matrices[j]
            d = matrices[j+length-1]
            
            cost_a = cost(dp[j], d)
            cost_b = cost(c, dp[j+1])
            if cost_a < cost_b:
                new.append(new_dimensions(dp[j], d))
                new_cost.append(cost_a + cost_dp[j])
            else:
                new.append(new_dimensions(c, dp[j+1]))
                new_cost.append(cost_b + cost_dp[j+1])
        dp = new
        cost_dp = new_cost
    print(cost_dp)
    print(dp)
    return cost_dp

def solve():
    n = int(input())
    matrices = [tuple(map(int, input().split())) for i in range(n)]
    ans = matrix_chain(matrices, n)
    print(ans)

solve()
