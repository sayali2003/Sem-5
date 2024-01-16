def get_profit(job):
    return job[2]

def get_deadline(job):
    return job[1]

def job_scheduling(arr):
    arr.sort(key=get_profit, reverse=True)
    max_deadline = max(arr, key=get_deadline)[1]
    gantt_chart = ['-1'] * (max_deadline + 1)
    total_profit = 0

    for job in arr:
        deadline = job[1]
        for slot in range(min(max_deadline, deadline), 0, -1):
            if gantt_chart[slot] == '-1':
                gantt_chart[slot] = job[0]
                total_profit += job[2]
                break

    return gantt_chart[1:], total_profit

def input_array():
    n = int(input("Enter the number of jobs: "))
    arr = []

    for i in range(n):
        job_id = input(f"Enter job {i + 1} id: ")
        deadline = int(input(f"Enter deadline for job {i + 1}: "))
        profit = int(input(f"Enter profit for job {i + 1}: "))
        arr.append((job_id, deadline, profit))

    return arr

if __name__ == "__main__":
    arr = input_array()
    result, total_profit = job_scheduling(arr)
    print("Optimized job sequence on Gantt chart:", result)
    print("Total Profit:", total_profit)

