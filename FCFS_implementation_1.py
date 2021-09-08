def FindWaitingTime(processes, n, burst_time):
    waiting_time = [None] * n
    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

    return waiting_time

def FindTurnAroundTime(processes, n, waiting_time, burst_time):
    tat = [None] * n

    for i in range(n):
        tat[i] = waiting_time[i] + burst_time[i]

    return tat

def FindAverageWaitingTime(n, wt):
    total_wt = 0

    for i in range(n):
        total_wt = total_wt + wt[i]

    return total_wt / n

def FindAverageTATTime(n, tat):
    total_tat = 0

    for i in range(n):
        total_tat = total_tat + tat[i]

    return total_tat / n

if __name__ =="__main__":
    # Processes with same arrival times
    processes = [1, 2, 3]
    burst_time = [10, 5, 8]

    n = len(processes)

    waiting_time = FindWaitingTime(processes, n, burst_time)
    print("Waiting Time: ", waiting_time)

    tat_time = FindTurnAroundTime(processes, n, waiting_time, burst_time)
    print("Turn Around Time: ", tat_time)

    average_wt = FindAverageWaitingTime(n, waiting_time)
    print("Average Waiting Time: ", average_wt)

    average_tat = FindAverageTATTime(n, tat_time)
    print("Average TAT Time: ", average_tat)
