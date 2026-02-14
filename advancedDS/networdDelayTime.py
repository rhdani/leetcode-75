'''
Docstring for networdDelayTime
A network of n nodes labeled 1 to n is provided along with a 
list of travel times for directed edges represented as 
times[i] = (xi, yi, ti), where xi is the source node,
yi is the target node, and
t is the delay time from the source node to the target node.

Considering we have a starting node, k, we have to determine 
the minimum time required for all the remaining
n − 1 nodes to receive the signal. Return −1 if it’s not possible 
for all n − 1 nodes to receive the signal.

'''
import heapq
from collections import defaultdict

def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    min_heap = [(0, k)]
    visited = set()
    max_time = 0
    
    while min_heap:
        time, node = heapq.heappop(min_heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        max_time = max(max_time, time)
        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (time + weight, neighbor))
    
    return max_time if len(visited) == n else -1

# Driver code
def main():
    time = [
                [[2, 1, 1], [3, 2, 1], [3, 4, 2]],
                [[2, 1, 1], [1, 3, 1], [3, 4, 2], [5, 4, 2]],
                [[1, 2, 1], [2, 3, 1], [3, 4, 1]],
                [[1, 2, 1], [2, 3, 1], [3, 5, 2]],
                [[1, 2, 2]]
            ]

    n = [4, 5, 4, 5, 2]
    k = [3, 1, 1, 1, 2]

    for i in range(len(time)):
        print(i + 1, ".\t times = ", time[i], sep="")
        print("\t number of nodes 'n' = ", n[i], sep="")
        print("\t starting node 'k' = ", k[i], "\n", sep="")
        print("\t Minimum amount of time required = ", network_delay_time(time[i], n[i], k[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
