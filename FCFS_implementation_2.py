def FindWaitingTime(n, burst_time, arrival_time):
    waiting_time = [0] * n
    service_time = [0] * n
    waiting_time[0] = 0

    for i in range(1, n):
        service_time[i] = service_time[i-1] + burst_time[i-1]

        waiting_time[i] = service_time[i] - arrival_time[i]
    
    return waiting_time

def FindTurnAroundTime(n, burst_time, waiting_time):
    ta_time = [0] * n

    for i in range(0, n):
        ta_time[i] = burst_time[i] + waiting_time[i]

    return ta_time

def FindAverageWaitingTime(n, waiting_time):
    avg_waiting_time = [0] * n
    for i in range(0, n):
        avg_waiting_time[i] = waiting_time[i] / n

    return avg_waiting_time

def FindAverageTurnAroundTime(n, ta_time):
    avg_ta_time = [0] * n
    for i in range(0, n):
        avg_ta_time[i] = ta_time[i] / n

    return avg_ta_time


if __name__ == "__main__":
    # Processes with different arrival times
    processes = [1, 2, 3]
    burst_time = [5, 9, 6]
    arrival_time = [0, 3, 6]
    n = len(processes)

    waiting_time = FindWaitingTime(n, burst_time, arrival_time)
    ta_time = FindTurnAroundTime(n, burst_time, waiting_time)

    print("Average waiting time = %.2f", FindAverageWaitingTime(n, waiting_time))
    print("Average turn around time = %.2f", FindAverageTurnAroundTime(n, ta_time))
