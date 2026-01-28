'''
An investor is looking to maximize their capital by undertaking a set of profitable projects. 
Due to limited time and resources, they can complete at most k distinct projects.

There are n available projects. Each project i has:

A profit of profits[i] earned upon completion.

A minimum capital requirement of capital[i] needed to start the project.

The investor starts with an initial capital of c. 
After completing a project, its profit is immediately added to the investor's current capital.

The goal is to choose up to k different projects in a way that maximizes the investor’s final capital. Return the maximum capital achievable after completing these projects.

It is guaranteed that the answer fits within a 32-bit signed integer.
'''
import heapq
from MaxHeap import MaxHeap
    
def maximum_capital(c, k, capitals, profits):
  currentCapital = c

  # Build min-heap of (requiredCapital, index)
  capitalsMinHeap = []
  for i, cap in enumerate(capitals):
    heapq.heappush(capitalsMinHeap, (cap, i))

  profitsMaxHeap = MaxHeap()

  # Up to k projects
  for _ in range(k):
    # Move all projects we can currently afford into the max-profit heap
    while capitalsMinHeap and capitalsMinHeap[0][0] <= currentCapital:
      required, idx = heapq.heappop(capitalsMinHeap)
      profitsMaxHeap.push(profits[idx])

    # If no affordable projects are available, stop early
    if len(profitsMaxHeap) == 0:
      break

    # Select the most profitable available project
    currentCapital += profitsMaxHeap.pop()

  return currentCapital

def main():
    input = (
              (0, 1, [1, 1, 2], [1 ,2, 3]),
              (1, 2, [1, 2, 2, 3], [2, 4, 6, 8]),
              (2, 3, [1, 3, 4, 5, 6], [1, 2, 3, 4, 5]),
              (1, 3, [1, 2, 3, 4], [1, 3, 5, 7]),
              (7, 2, [6, 7, 8, 10], [4, 8, 12, 14]),
              (2, 4, [2, 3, 5, 6, 8, 12], [1, 2, 5, 6, 8, 9])
            )
    num = 1
    for i in input:
        print(f"{num}.\tProject capital requirements:  {i[2]}")
        print(f"\tProject expected profits:      {i[3]}")
        print(f"\tNumber of projects:            {i[1]}")
        print(f"\tStart-up capital:              {i[0]}")
        print("\n\tMaximum capital earned: ",
              maximum_capital(i[0], i[1], i[2], i[3]))
        print("-" * 100, "\n")
        num += 1


if __name__ == "__main__":
    main()
