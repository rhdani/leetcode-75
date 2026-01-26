import heapq
def k_closest(points, k):
    result = []
    numPoints = len(points)
    myHeap = []
    for i in range(k):
        px = points[i][0]
        py = points[i][1]
        dist = px*px + py*py
        heapq.heappush(myHeap, (-dist, points[i]))
    
    for j in range(k, numPoints):
        new_x = points[j][0]
        new_y = points[j][1]
        cur_min_dist, cur_point = myHeap[0]
        new_dist = new_x * new_x + new_y * new_y
        if (-new_dist) > cur_min_dist:
            heapq.heapreplace(myHeap, (-new_dist, points[j]))

    result = [heapq.heappop(myHeap)[1] for _ in range(len(myHeap))]
    return result

# Driver code
def main():
    points_arr = [
        [[1, 3], [3, 4], [2, -1]],
        [[1, 3], [2, 4], [2, -1], [-2, 2], [5, 3], [3, -2]],
        [[1, 3], [5, 3], [3, -2], [-2, 2]],
        [[2, -1], [-2, 2], [1, 3], [2, 4]],
        [[1, 3], [2, 4], [2, -1], [-2, 2], [5, 3], [3, -2], [5, 3], [3, -2]]
    ]

    k_arr = [2, 3, 1, 4, 5]

    for i in range(len(points_arr)):
        print(f"{i + 1}.\tpoints: [{', '.join(str(p) for p in points_arr[i])}]")
        print(f"\tk: {k_arr[i]}\n")
        result = k_closest(points_arr[i], k_arr[i])
        print(f"\t{k_arr[i]} closest point(s) to origin: [{', '.join(str(p) for p in result)}]")
        print('-' * 100)

    # Additional edge-case tests
    print("\nEdge-case tests:")
    edge_tests = [
        ([], 1, "empty points, k=1"),
        ([[1, 2]], 0, "single point, k=0"),
        ([[1, 2]], 2, "k > n"),
        ([[0, 0], [0, 0], [1, 1]], 2, "repeated points"),
        ([[-3, -4], [0, 0], [5, 12]], 2, "negative coords"),
        ([[1, 3], [2, 4]], 2, "k == n"),
    ]

    for pts, kk, desc in edge_tests:
        print(f"\nTest: {desc} -> points: [{', '.join(str(p) for p in pts)}], k: {kk}")
        try:
            res = k_closest(pts, kk)
            print(f"\tResult: [{', '.join(str(p) for p in res)}]")
        except Exception as e:
            print(f"\tRaised {type(e).__name__}: {e}")
        print('-' * 60)

if __name__ == "__main__":
    main()
