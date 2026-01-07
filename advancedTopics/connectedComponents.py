from UnionFindSequence import UnionFindSequence as UnionFind

def count_components(n, edges):

    union = UnionFind(n)
    
    for item in edges:
        u, v = item[0], item[1]
        if union.find(u) != union.find(v):
            union.union(u, v)
    
    mySet = set()        
    for i in range(n):
        if union.find(i) not in mySet:
            mySet.add(union.find(i))
            
    # Replace this placeholder return statement with your code
    return len(mySet)

# Driver code
def main():
    n = [5, 6, 7, 8, 10, 10]

    edges = [
        [[0, 1], [2, 3], [3, 4], [1, 2]],
        [[0, 1], [3, 4], [4, 5]],
        [[0, 1], [2, 3], [3, 4], [1, 2], [4, 5], [5, 6]],
        [[0, 1], [1, 2], [4, 5], [6, 7]],
        [[0, 2], [2, 3], [4, 5], [5, 6], [7, 8], [8, 9]],
        [[0, 1], [2, 3], [6, 7], [7, 8], [8, 9]]
    ]

    for i in range(len(edges)):
        print(i + 1, "\t n = ", n[i], sep="")
        print("\t edges = ", edges[i], sep="")
        
        result = count_components(n[i], edges[i])
        print("\t Number of connected components are: ", result, sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()