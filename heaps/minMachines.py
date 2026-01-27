import heapq

def minimum_machines(tasks):
    if not tasks or len(tasks) == 0:
        return 0
    if len(tasks) == 1:
        return 1
    tasks.sort(key=lambda x: x[0])
    
    print(tasks)
    myHeap = []
    for i in range(len(tasks)):
        if len(myHeap) == 0:
            heapq.heappush(myHeap, tasks[i][1])
            continue
        if myHeap[0] <= tasks[i][0]:
            heapq.heappop(myHeap)
        heapq.heappush(myHeap, tasks[i][1])
    
    return len(myHeap)

# Driver code
def main():
    input_tasks_list = [
        [[1, 1], [5, 5], [8, 8], [4, 4], [6, 6], [10, 10], [7, 7]],
        [[1, 7], [1, 7], [1, 7], [1, 7], [1, 7], [1, 7]],
        [[1, 7], [8, 13], [5, 6], [10, 14], [6, 7]],
        [[1, 3], [3, 5], [5, 9], [9, 12], [12, 13], [13, 16], [16, 17]],
        [[12, 13], [13, 15], [17, 20], [13, 14], [19, 21], [18, 20]]
    ]

    for i, tasks_list in enumerate(input_tasks_list, 1):
        print(f"{i}.\t Tasks: [", end="")
        for j, task in enumerate(tasks_list):
            print(f"[{task[0]}, {task[1]}]", end="")
            if j < len(tasks_list) - 1:
                print(", ", end="")
        print("]")
        print(f"\t Minimum number of machines: {minimum_machines(tasks_list)}")
        print("-" * 100)

if __name__ == "__main__":
    main()
