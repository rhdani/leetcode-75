import heapq

def k_smallest_number(lists, k):
    minHeap = []
    for i in range(len(lists)):
        if (len(lists[i]) > 0):
            heapq.heappush(minHeap, (lists[i][0], i, 0))
    
    numMerged = 0
    result = 0
    while (len(minHeap) > 0 and numMerged < k):
        (result, listIndex, elementIndex) = heapq.heappop(minHeap)
        numMerged += 1
        
        if (elementIndex + 1 < len(lists[listIndex])):
            heapq.heappush(minHeap, (lists[listIndex][elementIndex + 1], listIndex, elementIndex + 1))
    
    return result

# driver code
def main():
    lists = [[[2, 6, 8], [3,6,10], [5, 8, 11]],
             [[1, 2, 3], [4, 5], [6, 7, 8, 15], [10, 11, 12, 13], [5, 10]],
             [[], [], []],
             [[1, 1, 3, 8], [5, 5, 7, 9], [3, 5, 8, 12]],
             [[5, 8, 9, 17], [], [8, 17, 23, 24]]]

    k = [5, 50, 7, 4, 8]

    for i in range(len(k)):
        print(i + 1, ".\t Input lists: ", lists[i],
              f"\n\t K = {k[i]}",
              f"\n\t {k[i]}th smallest number from the given lists is: ",
              k_smallest_number(lists[i], k[i]), sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()
