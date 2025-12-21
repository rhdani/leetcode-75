from AdjacencyMatrix import *
from queue import *

def estimate_water_flow(heights):

    numRows = 0
    numCols = 0
    retVal = []
    if not heights:
        return retVal
    numRows = len(heights)
    numCols = len(heights[0])
    numNodes = numRows * numCols #each cell in the grid is a node in the graph
    # Adding two nodes to represent PAC and ATL, numNodes + 1 is PAC, numNodes + 2 is ATL
    pacIndex = numNodes #Account for start from 0
    atlIndex = numNodes + 1

    myGraph = AdjacencyMatrix(numNodes + 2, True)
    def northFlowAllowed(row, col)->bool:
        if (row <= 0):
            return False
        if (heights[row-1][col] <= heights[row][col]):
            return True
        return False

    def southFlowAllowed(row, col)->bool:
        if (row >= numRows - 1):
            return False
        if (heights[row+1][col] <= heights[row][col]):
            return True
        return False

    def westFlowAllowed(row, col)->bool:
        if (col >= numCols - 1):
            return False
        if (heights[row][col + 1] <= heights[row][col]):
            return True
        return False

    def eastFlowAllowed(row, col)->bool:
        if (col <= 0):
            return False
        if (heights[row][col - 1] <= heights[row][col]):
            return True
        return False

    #Node indexed by row so node i represents rowNum*numCols + colNum
    #Edges are representing reverse flow, so bfs from pacIndex and atlIndex
    #will uncover spanning tree rooted at pacIndex or atlIndex and all nodes
    #visited will show the set of nodes from which water can reach the respective
    #ocean
    for i in range(numCols):
        myGraph.add_edge(pacIndex, i)
        myGraph.add_edge(atlIndex, numCols*(numRows - 1)+ i)
    for i in range(numRows):
        myGraph.add_edge(pacIndex, i*numCols)
        myGraph.add_edge(atlIndex, (i*numCols) + (numCols - 1))

    #Construct graph
    for i in range(numRows):
        for j in range(numCols):
            nodeIndex = numCols*i + j
            if (northFlowAllowed(i, j)):
                connectedNodeIndex = numCols*(i-1) + j
                myGraph.add_edge(connectedNodeIndex, nodeIndex)
            if (southFlowAllowed(i, j)):
                connectedNodeIndex = numCols*(i+1) + j
                myGraph.add_edge(connectedNodeIndex, nodeIndex)
            if (eastFlowAllowed(i, j)):
                connectedNodeIndex = numCols*i + j - 1
                myGraph.add_edge(connectedNodeIndex, nodeIndex)
            if (westFlowAllowed(i, j)):
                connectedNodeIndex = numCols*i + j + 1
                myGraph.add_edge(connectedNodeIndex, nodeIndex)

    pacificSet = set()
    atlanticSet = set()

    #BFS for pacific
    stack = [pacIndex]

    while (stack):
        current = stack.pop()
        if current not in pacificSet:
            pacificSet.add(current)

            for neighbor in myGraph.getNeighbors(current):
                if neighbor not in pacificSet:
                    stack.append(neighbor)
    #BFS for atlantic
    stack = [atlIndex]
    while (stack):
        current = stack.pop()
        if current not in atlanticSet:
            atlanticSet.add(current)
            for neighbor in myGraph.getNeighbors(current):
                if neighbor not in atlanticSet:
                    stack.append(neighbor)

    #print("Pacific Set is ", pacificSet)
    #print("Atlantic Set is ", atlanticSet)
    common = pacificSet & atlanticSet
    #print("Common set is", common)

    for item in common:
        row, col = divmod(item, numCols)
        retVal.append((row, col))
    #myGraph.display()
    #retVal = list(common)

    return retVal

# Driver code
def main():
    matrices = [
        [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
        [[4, 4, 4, 3, 1], [1, 5, 3, 7, 7], [3, 1, 3, 7, 5], [1, 2, 4, 4, 7], [4, 3, 1, 7, 1]],
        [[7, 3, 5, 2, 8], [2, 3, 4, 5, 6], [3, 9, 6, 8, 4]],
        [[1, 1], [0, 1], [0, 0]],
        [[1, 0, 1], [1, 1, 0], [1, 1, 1]],
        [[2, 3, 4, 5, 6, 7, 8], [2, 9, 3, 8, 4, 5, 6],[3, 4, 6, 7, 8, 5, 4], [9, 1, 5, 6, 7, 5, 5]]
    ]

    for i in range(len(matrices)):
        #print(i + 1, ".\t Input heights: ", sep="")
        #print_matrix(matrices[i])
        print("\n\t Common coordinates: ", estimate_water_flow(matrices[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()

