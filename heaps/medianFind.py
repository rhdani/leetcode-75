import heapq
from MaxHeap import *

class MedianOfStream:
  def __init__(self):
    self.minHeap = []
    self.maxHeap = MaxHeap()
    self.count = 0

  # This function should take a number and store it
  def insert_num(self, num):
    if len(self.maxHeap) == 0:
      self.maxHeap.push(num)
      self.count += 1
      return
    if (num <= self.maxHeap.peek()):
      self.maxHeap.push(num)
    else:
      heapq.heappush(self.minHeap, num)
    self.count += 1
    if ((len(self.minHeap) - len(self.maxHeap)) > 1):
      val = heapq.heappop(self.minHeap)
      self.maxHeap.push(val)
      return
    if ((len(self.maxHeap) - len(self.minHeap)) > 1):
      val = self.maxHeap.pop()
      heapq.heappush(self.minHeap, val)
    return
    
  # This function should return the median of the stored numbers
  def find_median(self):
    # Empty stream
    if self.count == 0:
      return None

    if self.count%2 == 0:
      return (self.maxHeap.peek() + self.minHeap[0])/2
    else:
      if len(self.minHeap) > len(self.maxHeap):
        return self.minHeap[0]
      else:
        return self.maxHeap.peek()
    return 0.0

def main():
  median_num = MedianOfStream()
  # Test: empty stream
  print("1. Empty stream median:", median_num.find_median())

  # Test: single element
  median_num.insert_num(10)
  print("2. Single element [10] median:", median_num.find_median())

  # Test: even number of elements
  median_num.insert_num(20)
  print("3. After inserting 20 -> [10,20] median:", median_num.find_median())

  # Test: duplicates
  for v in [20, 20, 10]:
    median_num.insert_num(v)
  print("4. After inserting duplicates [10,20,20,20,10] median:", median_num.find_median())

  # Test: negative numbers and descending insertion
  median_num2 = MedianOfStream()
  seq = [5, 4, 3, 2, 1, -1, -5]
  for v in seq:
    median_num2.insert_num(v)
  print("5. Descending stream with negatives median:", median_num2.find_median())

  # Test: ascending insertion
  median_num3 = MedianOfStream()
  for v in [1,2,3,4,5,6]:
    median_num3.insert_num(v)
  print("6. Ascending stream [1..6] median:", median_num3.find_median())

  # Test: interleaved insertions
  median_num4 = MedianOfStream()
  inter = [2, 1, 5, 4, 3]
  for idx, v in enumerate(inter, start=1):
    median_num4.insert_num(v)
    print(f"6.{idx} Interleaved insert {v} -> median:", median_num4.find_median())


if __name__ == "__main__":
    main()
