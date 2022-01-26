def jobs_sceduling(jobs):
    jobs.sort(key=lambda job: job[0])

    n_jobs = len(jobs)
max_deadline = max(job[1] for job in jobs)

    req_time = min(n_jobs, max_deadline)

    profit = 0
    schedule = [0 for i in range(req_time)]
    
    for job in jobs:
        time = min(job[1], req_time)-1
        while time > -1:
            if not schedule[time]:
                schedule[time] = 1
                ans += job[0]






def solve():
    n = int(input())

    jobs = []
    for _ in range(n): jobs.append(tuple(map(int, input().split())))
    
    profit = jobs_scheduling(jobs)
    print(profit)


solve()

