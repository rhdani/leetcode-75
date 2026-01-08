"""twoStonesRemoval

Solution for the "Most Stones Removed with Same Row or Column" problem.

Approach:
- Treat each stone's row and column as nodes in a union-find (disjoint set).
- For a stone at (r, c) connect the node representing row r and the node
  representing column c. Stones that share a row or column become part of
  the same connected component.
- The maximum number of removable stones = total stones - number_of_components

Performance:
- Let N be the number of stones. We perform ~2N find/union operations.
- With path compression and union by rank the amortized time is
  approximately O(N * alpha(N)) where alpha is the inverse Ackermann
  function (practically constant). Space is O(N).

Improvements suggested (implemented here):
- Use union-by-rank to keep tree depths small (reduces worst-case find time).
- Optionally, encode rows and columns as integers if memory or hashing cost
  becomes a measurable bottleneck for very large inputs.
"""

class UnionFind:
  """Union-Find (Disjoint Set Union) with path compression and rank."""

  def __init__(self):
    # parent map: node -> parent
    self.parent = {}
    # rank map: node -> tree rank (approximate depth)
    self.rank = {}

  def find(self, x):
    """Find representative of x with path compression."""
    if x not in self.parent:
      # initialize new node: parent to itself and rank 0
      self.parent[x] = x
      self.rank[x] = 0
      return x
    if self.parent[x] != x:
      # path compression: flatten the tree
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    """Union the sets containing x and y using rank heuristic."""
    px = self.find(x)
    py = self.find(y)
    if px == py:
      return
    # attach smaller rank tree under larger rank tree
    if self.rank[px] < self.rank[py]:
      self.parent[px] = py
    elif self.rank[px] > self.rank[py]:
      self.parent[py] = px
    else:
      self.parent[py] = px
      self.rank[px] += 1


def remove_stones(stones):
  """Return maximum number of stones that can be removed.

  stones: iterable of (r, c) pairs (lists or tuples).
  """
  uf = UnionFind()

  # Union the row node and column node for each stone.
  # We prefix row and column keys so they live in separate namespaces.
  for r, c in stones:
    uf.union(('r', r), ('c', c))

  # Count distinct connected components by collecting unique roots
  roots = set()
  for r, c in stones:
    roots.add(uf.find(('r', r)))

  # Maximum removable = total stones - number of connected components
  return len(stones) - len(roots)


def main():
  # Test cases (covers typical and edge cases)
  test_cases = [
    # Provided examples from original file
    {
      'name': 'example1',
      'stones': [[0, 0], [0, 1], [1, 2], [2, 2], [3, 3]],
    },
    {
      'name': 'example2',
      'stones': [[0, 0], [2, 2], [3, 3]],
    },
    # Additional cases
    {'name': 'empty', 'stones': []},
    {'name': 'single', 'stones': [[0, 0]]},
    {'name': 'two_disconnected', 'stones': [[0, 0], [1, 1]]},
    {'name': 'two_same_row', 'stones': [[0, 0], [0, 1]]},
    {'name': 'all_same_row', 'stones': [[0, 0], [0, 1], [0, 2], [0, 3]]},
    {'name': 'chain_connected', 'stones': [[0, 0], [0, 1], [1, 1], [2, 1], [2, 2]]},
  ]

  for tc in test_cases:
    stones = tc['stones']
    # normalize input (ensure list of tuples) and compute
    norm = [tuple(s) for s in stones]
    removed = remove_stones(norm)
    print(f"{tc['name']}: stones={stones} -> max removed = {removed}")


if __name__ == '__main__':
  main()
