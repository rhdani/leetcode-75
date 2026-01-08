"""
⬅️ We have provided a union_find.py file under the "Files" tab 
of this widget. You can use this file to build your solution.
"""
import collections
from collections import defaultdict

class UnionFind:
  def __init__(self):
    self.parent = {}

  def find(self, x):
    if x not in self.parent:
        self.parent[x] = x
    if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    px, py = self.find(x), self.find(y)
    if px != py:
      self.parent[py] = px


def remove_stones(stones):
  uf = UnionFind()

  # Union row and column for each stone
  for r, c in stones:
    uf.union(('r', r), ('c', c))

  # Count unique connected components
  roots = set()
  for r, c in stones:
    roots.add(uf.find(('r', r)))

  return len(stones) - len(roots)

# driver code
def main():
    stones = [[[0, 0], [0, 1], [1, 2], [2, 2], [3, 3]],
        [[0, 0], [2, 2], [3, 3]],
        [[0, 1], [2, 1], [3, 0]],
        [[1, 0], [2, 1], [2, 3], [3, 1], [3, 3]],
        [[1, 2], [2, 0], [2, 2], [3, 3]]]

    for i in range(len(stones)):
        print(str(i+1)+".\tMaximum stones which can be removed from "+str(stones[i]) + " are: ", remove_stones(stones[i]))
        print("-" * 100)
  
if __name__ == '__main__':
    main()
