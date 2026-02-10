'''
Docstring for refueling
A car travels from a starting position to a destination which is 
target miles east of the starting position. Along the way, 
there are gas stations. Each station[i] represents a 
gas station that is station[i][0] miles east of the
 starting position and has station[i][1] liters of gas.
The car starts with an infinite tank of gas, which initially has 
startFuel liters of fuel in it.
The car uses 1 liter of gas per 1 mile that it drives. When the car
reaches a gas station, it may stop and refuel, transferring all the
gas from the station into the car.
Return the minimum number of refueling stops the car must make in order
to reach its destination. If it cannot reach the destination, return -1.
'''

import heapq

def min_refuel_stops(target, start_fuel, stations): 
    stops = 0
    num_stations = len(stations)
    fuel_capacity = start_fuel
    if (fuel_capacity >= target):
        return 0
    
    maxHeap = []
    index = 0
    while index < num_stations:
        if fuel_capacity >= target:
            return stops
        if (fuel_capacity >= stations[index][0]):
            heapq.heappush(maxHeap, -stations[index][1])
            index += 1
        else:
            if (len(maxHeap) == 0):
                return -1
            fuel = heapq.heappop(maxHeap)
            fuel_capacity += -fuel
            stops += 1
            if fuel_capacity >= target:
                return stops

    while fuel_capacity < target:
        if len(maxHeap) == 0:
            return -1
        fuel = heapq.heappop(maxHeap)
        fuel_capacity += -fuel
        stops += 1
    return stops

# Driver Code
def main():
    input = (
              (3, 3, []),
              (59, 14, [[9, 12], [11, 7], [13, 16], [21, 18], [47, 6]]),
              (15, 3, [[2, 5], [3, 1], [6, 3], [12, 6]]),
              (570, 140, [[140, 200], [160, 130], [310, 200], [330, 250]]),
              (1360, 380, [[310, 160], [380, 620], [700, 89], [850, 190],
               [990, 360]])
    )
    num = 1
    for i in input:
        print(num, ".\tStations : ", i[2], sep="")
        print("\tTarget : ", i[0])
        print("\tStarting fuel : ", i[1])
        print("\n\tMinimum number of refueling stops :",
              min_refuel_stops(i[0], i[1], i[2]))
        num += 1
        print("-" * 100, "\n")

if __name__ == "__main__":
    main()