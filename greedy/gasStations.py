'''
Docstring for gasStations
There are n gas stations along a circular route, where the amount of gas at the ith
station is gas[i].  We have a car with an unlimited gas tank, 
and it costs cost[i] of gas to travel from the ith
 station to the next (i+1) th station. We begin the journey 
with an empty tank at one of the gas stations.

Find the index of the gas station in the integer array gas such that if we start from that index we may return to the same index by traversing through all the elements, collecting gas[i] and consuming cost[i].

If it is not possible, return -1.

If there exists such index, it is guaranteed to be unique.
'''
def validateRoute(gas, cost, start):
    curIndex = start
    nextIndex = start + 1
    if nextIndex == len(gas):
        nextIndex = 0
    currentGas = 0
    while (nextIndex != start):
        currentGas += gas[curIndex] - cost[curIndex]
        if currentGas < 0:
            return False
        curIndex = nextIndex
        if nextIndex == len(gas) - 1:
            nextIndex = 0
        else:
            nextIndex += 1
    return True
        
        
def gas_station_journey(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    total = 0
    cur_tank = 0
    start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        cur_tank += diff
        if cur_tank < 0:
            start = i + 1
            cur_tank = 0
    return start if total >= 0 else -1

def main():
    gas = [
        [1, 2, 3, 4, 5],
        [2, 3, 4],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 10],
        [1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5],
        [3, 4, 5],
        [1, 2, 3, 4]
    ]
    cost = [
        [3, 4, 5, 1, 2],
        [3, 4, 3],
        [1, 2, 3, 4, 5],
        [2, 2, 1, 3, 1],
        [1, 0, 1, 2, 3],
        [1, 2, 3, 4, 5],
        [4, 5, 6],
        [2, 3, 4, 5]
    ]

    for i in range(len(gas)):
        print(i + 1, ".\tGas stations: ", gas[i], sep="")
        print("\tCost to travel: ", cost[i], sep="")
        result = gas_station_journey(gas[i], cost[i])
        if (result == -1):
            print("\tNo valid starting point exists.")
        else:
            print("\tStarting point index: ", result)
        print("-" * 100)

if __name__ == '__main__':
    main()