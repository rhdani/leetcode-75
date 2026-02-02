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
    lists = [
        [[2, 6, 8], [3,6,10], [5, 8, 11]],
        [[1, 2, 3], [4, 5], [6, 7, 8, 15], [10, 11, 12, 13], [5, 10]],
        [[], [], []],
        [[1, 1, 3, 8], [5, 5, 7, 9], [3, 5, 8, 12]],
        [[5, 8, 9, 17], [], [8, 17, 23, 24]],
        # edge cases
        [[]],                                # single empty list
        [[1,2,3]],                           # single non-empty list
        [[1,2], [3]],                        # k greater than total elements
        [[-5, -1], [-3, 0]],                 # negatives
        [[2,2], [2,2]],                      # duplicates across lists
        [[10,20], [30], []]                  # k = 0 case will be tested
    ]

    k = [
        5, 50, 7, 4, 8,
        1,    # for [[]]
        1,    # for [[1,2,3]]
        5,    # for [[1,2],[3]] (k > total)
        2,    # for negatives
        4,    # duplicates
        0     # k = 0
    ]

    expected = [
        6, 15, 0, 3, 24,
        0,    # single empty list -> function returns 0
        1,    # first element
        3,    # last element when k > total elements
        -3,   # second smallest among negatives
        2,    # fourth duplicate
        0     # k=0 -> returns initial 0
    ]

    for i in range(len(k)):
        # compute result (keep original print output format)
        res = k_smallest_number(lists[i], k[i])
        print(i + 1, ".\t Input lists: ", lists[i],
              f"\n\t K = {k[i]}",
              f"\n\t {k[i]}th smallest number from the given lists is: ",
              res, sep="")

        # validate using assert and report Pass/Fail
        try:
            assert res == expected[i]
            print("\tTest Result: Pass")
        except AssertionError:
            print("\tTest Result: Fail")

        print("-" * 100)

if __name__ == '__main__':
    main()
