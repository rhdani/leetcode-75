'''
Docstring for kthSmallestPairs
You are given two integer arrays, list1 and list2, 
sorted in non-decreasing order, and an integer, k.

A pair (u, v)is defined as one element u chosen from list1 and one element 
v chosen from list2.

Your task is to return the k pairs 
(u1, v1), (u2, v2), ..., (uk, vk)
 whose sums u1 + v1, u2 + v2, ..., uk + vk
 are the smallest among all possible such pairs.
'''
import heapq

def k_smallest_pairs(list1, list2, k):
        minHeap = []
        for i in range(min(k, len(list1))):
            heapq.heappush(minHeap, (list1[i] + list2[0], i, 0))
        
        numMerged = 0
        result = []
        while (len(minHeap) > 0 and numMerged < k):
            (sum, list1Index, list2Index) = heapq.heappop(minHeap)
            result.append((list1[list1Index], list2[list2Index]))
            numMerged += 1
            
            if (list2Index + 1 < len(list2)):
                heapq.heappush(minHeap, (list1[list1Index] + list2[list2Index + 1], list1Index, list2Index + 1))
        
        return result

# Driver code
def main():
    list1 = [[2, 8, 9],
             [1, 2, 300],
             [1, 1, 2],
             [4, 6],
             [4, 7, 9],
             [1, 1, 2]]

    list2 = [[1, 3, 6],
             [1, 11, 20, 35, 300],
             [1, 2, 3],
             [2, 3],
             [4, 7, 9],
             [1]]

    k = [9, 30, 1, 2, 5, 4]

    for i in range(len(k)):
        print(i + 1, ".\t Input pairs: ", list1[i], ", ", list2[i],
              f"\n\t k = {k[i]}", sep="")
        print("\t Pairs with the smallest sum are: ",
              k_smallest_pairs(list1[i], list2[i], k[i]), sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()

