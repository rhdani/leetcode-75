from typing import List, Tuple

def do_intervals_overlap(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
  """Return True if closed intervals `a` and `b` overlap or touch.

  Intervals are treated as closed [start, end]. They overlap if
  a.start <= b.end and b.start <= a.end.
  """
  return not (a[1] < b[0] or b[1] < a[0])


def merge_intervals(a: Tuple[int, int], b: Tuple[int, int]) -> List[int]:
  """Return the merged interval covering both `a` and `b`.

  Caller should ensure the intervals overlap/touch before merging.
  """
  return [min(a[0], b[0]), max(a[1], b[1])]


def insert_interval(existing_intervals: List[Tuple[int, int]], new_interval: Tuple[int, int]) -> List[List[int]]:
  """Insert `new_interval` into `existing_intervals` and return a new
  sorted, non-overlapping list of intervals.

  Assumes `existing_intervals` is sorted by start and contains no overlaps.
  This implementation merges intervals that overlap or touch (i.e., end >= next.start).
  """
  result: List[List[int]] = []
  i = 0
  n = len(existing_intervals)

  # Add all intervals that end before the new interval starts
  while i < n and existing_intervals[i][1] < new_interval[0]:
    result.append(list(existing_intervals[i]))
    i += 1

  # Merge all overlapping (or touching) intervals into `new_interval`
  merged = [new_interval[0], new_interval[1]]
  while i < n and existing_intervals[i][0] <= merged[1]:
    merged[0] = min(merged[0], existing_intervals[i][0])
    merged[1] = max(merged[1], existing_intervals[i][1])
    i += 1

  result.append(merged)

  # Append the remaining intervals
  while i < n:
    result.append(list(existing_intervals[i]))
    i += 1

  return result


if __name__ == "__main__":
  # Simple self-checks / examples
  examples = [
    ([(1, 3), (6, 9)], (2, 5), [[1, 5], [6, 9]]),
    ([(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)], (4, 8), [[1, 2], [3, 10], [12, 16]]),
    ([], (5, 7), [[5, 7]]),
    ([(1, 5)], (2, 3), [[1, 5]]),
    ([(1, 5)], (6, 8), [[1, 5], [6, 8]]),
    ([(1, 2), (3, 4)], (2, 3), [[1, 4]]),
  ]

  for inputs, new_int, expected in examples:
    out = insert_interval(inputs, new_int)
    assert out == expected, f"failed for {inputs} + {new_int}: got {out}, want {expected}"

  print("All basic tests passed.")
