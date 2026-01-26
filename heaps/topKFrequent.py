import heapq
import collections
from collections import defaultdict
def top_k_frequent(arr, k):

    my_map = defaultdict(int)
    minHeap = []
    
    my_map = collections.Counter(arr)

    for element, freq in my_map.items():

        heapq.heappush(minHeap, (freq, element))
        
        # If the heap size exceeds k, pop the smallest element (least frequent)
        if len(minHeap) > k:
            heapq.heappop(minHeap)

    retVal = [item[1] for item in minHeap]
    return retVal
    
# Driver code
def main():
    arr = [[1, 3, 5, 12, 11, 12, 11, 12, 5], [1, 3, 5, 14, 18, 14, 5],
           [2, 3, 4, 5, 6, 7, 7], [9, 8, 7, 6, 6, 5, 4, 3, 2, 1], 
           [2, 4, 3, 2, 3, 4, 5, 4, 4, 4], [1, 1, 1, 1, 1, 1], [2, 3]]
    k = [3, 2, 1, 1, 3, 1, 2]

    for i in range(len(k)):
        print(i+1, ". \t Input: (", arr[i], ", ", k[i], ")", sep="")
        print("\t Top", k[i], "frequent Elements: ",
              top_k_frequent(arr[i], k[i]))
        print("-"*100)

if __name__ == '__main__':
    main()
