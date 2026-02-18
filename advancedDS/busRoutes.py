'''
Docstring for busRoutes
You are given an array routes representing bus routes where routes[i] 
is a bus route that the ith bus repeats forever.
For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels
in the sequence 1 → 5 → 7 → 1 → 5 → 7 → ... forever.   
You will start at the bus stop source (You are not on any bus initially), 
and you want to go to the bus stop target. You can travel between bus 
stops by buses only
'''
from collections import defaultdict, deque
def minimum_buses(routes, source, target):
    if source == target:
        return 0

    # Map each stop to the buses that go through it
    stop_to_buses = defaultdict(set)
    for bus_index, route in enumerate(routes):
        for stop in route:
            stop_to_buses[stop].add(bus_index)

    # BFS initialization
    visited_buses = set()
    visited_stops = set([source])
    queue = deque([(source, 0)])  # (current_stop, buses_taken)

    while queue:
        current_stop, buses_taken = queue.popleft()

        # Check all buses that go through the current stop
        for bus in stop_to_buses[current_stop]:
            if bus in visited_buses:
                continue
            visited_buses.add(bus)

            # Check all stops on this bus route
            for next_stop in routes[bus]:
                if next_stop == target:
                    return buses_taken + 1
                if next_stop not in visited_stops:
                    visited_stops.add(next_stop)
                    queue.append((next_stop, buses_taken + 1))

    return -1  # Target is unreachable  

# Driver code
def main():
  routes = [[[2, 5, 7], [4, 6, 7]], [[1, 12], [4, 5, 9], [9, 19], [10, 12, 13]], [[1, 12], [10, 5, 9], [4, 19], [10, 12, 13]], [[1, 9, 7, 8], [3, 6, 7], [4, 9], [8, 2, 3, 7], [2, 4, 5]], [[1, 2, 3], [4, 5, 6],[7, 8, 9]]]
  src = [2, 9, 1, 1, 4]
  dest = [6, 12, 9, 5, 6]
  
  for i, bus in enumerate(routes):
    print(i+1, ".\tBus Routes: ", bus, sep ="")
    print("\tSource: ", src[i])
    print("\tDestination: ", dest[i])
    print("\n\tMinimum Buses Required: ", minimum_buses(bus, src[i], dest[i]))
    print("-"*100)

if __name__ == '__main__':
    main()