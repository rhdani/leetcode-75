'''
Docstring for taskScheduler
You are given an array of CPU tasks represented by uppercase letters (A to Z) 
and an integer n, which denotes the cooling period required between any 
two identical tasks. Each task takes exactly one CPU interval to execute. 
Therefore, each CPU interval can either perform a task or remain idle. 
Tasks can be executed in any order, but the same task must be separated by 
at least n intervals.

Determine the minimum number of CPU intervals required to complete all tasks.
'''
from collections import Counter
import heapq    

def least_interval(tasks, n):
    # If there is no cooling requirement, tasks can run back-to-back.
    # The minimum time is simply the number of tasks.
    if n == 0:
        return len(tasks)

    # Count how many times each task appears (e.g., {'A':3,'B':2}).
    # Counter gives a frequency map that we will use to schedule the most
    # frequent tasks first to minimize idle time.
    task_counts = Counter(tasks)

    # We want a max-heap to always pick the most frequent remaining task.
    # Python's heapq is a min-heap, so we store negative counts to simulate
    # a max-heap (larger original counts become smaller negative numbers).
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)

    # `time` accumulates the total CPU intervals (tasks + idle slots).
    time = 0

    # Continue scheduling until there are no tasks left in the heap.
    while max_heap:
        # `temp` will hold tasks (as negative remaining counts) that we
        # popped and still have remaining occurrences after executing once.
        temp = []

        # `intervals` counts how many actual intervals (task executions)
        # were used in this cycle of length `n + 1`.
        intervals = 0

        # We try to fill up to `n + 1` intervals in this block. This block
        # length enforces the cooling requirement between two identical tasks.
        for _ in range(n + 1):
            # If there is any task available, pick the one with highest
            # remaining count (most negative value in `max_heap`).
            if max_heap:
                # Pop the largest remaining count (stored as negative).
                count = heapq.heappop(max_heap)

                # We executed this task once, so increment its value by 1
                # (less negative). If it still has remaining occurrences
                # (i.e. count + 1 < 0), save it to `temp` to be pushed back
                # into the heap after this cooling block.
                if count + 1 < 0:
                    temp.append(count + 1)

                # We used one interval to run a task.
                intervals += 1

        # Push the tasks that still have remaining occurrences back
        # into the heap so they can be scheduled in future blocks.
        for item in temp:
            heapq.heappush(max_heap, item)

        # If heap is empty after this block, we only used `intervals` time
        # (no extra idle slots required at the end). Otherwise, the block
        # takes the full `n + 1` length (including idle slots) because we
        # couldn't fill all positions with distinct tasks and must wait
        # for the cooling period before repeating a task.
        time += intervals if not max_heap else n + 1

    # Total accumulated time is the minimum intervals required.
    return time

# driver code
def main():
    all_tasks = [['A', 'A', 'B', 'B'],
                 ['A', 'A', 'A', 'B', 'B', 'C', 'C'],
                 ['S', 'I', 'V', 'U', 'W', 'D', 'U', 'X'],
                 ['M', 'A', 'B', 'M', 'A', 'A', 'Y', 'B', 'M'],
                 ['A', 'K', 'X', 'M', 'W', 'D', 'X', 'B', 'D', 'C', 'O', 'Z', 'D', 'E', 'Q']]
    all_ns = [2, 1, 0, 3, 3]

    for i in range(len(all_tasks)):
        print(i+1, '.', '\tTasks: ', all_tasks[i], sep='')
        print('\tn: ', all_ns[i], sep='')
        min_time = least_interval(all_tasks[i], all_ns[i])
        print('\tMinimum CPUs required to execute the tasks: ', min_time)
        print('-' * 100)

if __name__ == '__main__':
    main()