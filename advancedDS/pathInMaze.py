'''
Docstring for pathInMaze
A maze consists of n rooms numbered from 1 − n, and some rooms are
connected by corridors. You are given a 2D integer array, corridors, where
corridors[i]=[room1,room2]
indicates that there is a corridor connecting room1 and room2, 
allowing a person in the maze to go from room1 to room2 and vice versa.

The designer of the maze wants to know how confusing the maze is. 
The confusion score of the maze is the number of different 
cycles of length 3.

For example,
1→2→3→1 is a cycle of length 3, but 
1→2→3→4 and 1→2→3→2→1 are not.

Two cycles are considered to be different if one or 
more of the rooms visited in the first cycle is 
not in the second cycle.

Return the confusion score of the maze.
'''
from collections import defaultdict

def number_of_paths(n, corridors):
    adj = defaultdict(set)
    count = 0
    for u, v in corridors:
        # ignore self-loops
        if u == v:
            continue
        # ignore duplicate edges
        if v in adj[u]:
            continue

        # any common neighbor forms a triangle (u, v, w)
        common = adj[u] & adj[v]
        count += len(common)

        # add the undirected edge
        adj[u].add(v)
        adj[v].add(u)

    return count

# Driver code
def main():
    n_list = [5, 4, 5, 5, 4]
    corridors_list= [[[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]],
                      [[1,2],[3,4]],
                      [[1,2],[5,2],[4,1], [3,1],[3,4]],
                      [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4],[1,5]],
                      [[1,2], [2,3], [3,4]] 
                    ]

    # additional tests
    n_list += [3, 5, 4, 4, 3]
    corridors_list += [
        # single triangle
        [[1,2],[2,3],[3,1]],
        # two triangles sharing an edge: (1,2,3) and (1,2,4)
        [[1,2],[2,3],[3,1],[2,4],[4,1]],
        # complete graph K4 has 4 triangles
        [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]],
        # duplicate edges and self-loop should be ignored; triangle 1-2-3
        [[1,2],[2,1],[1,1],[2,3],[3,1]],
        # no cycles
        [[1,2]]
    ]

    for i in range(len(n_list)):
        print(i + 1, ".\tn: ", n_list[i], sep = "")
        print("\tcorridors: ", corridors_list[i], sep = "")
        print("\tcycles :", number_of_paths(n_list[i], corridors_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()