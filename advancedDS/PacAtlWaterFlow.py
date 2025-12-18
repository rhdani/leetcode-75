from AdjacencyMatrix import *

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
    #Initialize edges to PAC
    for i in range(numCols):
        myGraph.add_edge(i, pacIndex)
        myGraph.add_edge(numCols*(numRows - 1)+ i, atlIndex)
    for i in range(numRows):
        myGraph.add_edge(i*numCols, pacIndex)
        myGraph.add_edge((i*numCols) + (numCols - 1), atlIndex)

    #Construct graph
    for i in range(numRows):
        for j in range(numCols):
            nodeIndex = numCols*i + j
            if (northFlowAllowed(i, j)):
                connectedNodeIndex = numCols*(i-1) + j
                myGraph.add_edge(nodeIndex, connectedNodeIndex)
            if (southFlowAllowed(i, j)):
                connectedNodeIndex = numCols*(i+1) + j
                myGraph.add_edge(nodeIndex, connectedNodeIndex)
            if (eastFlowAllowed(i, j)):
                connectedNodeIndex = numCols*i + j - 1
                myGraph.add_edge(nodeIndex, connectedNodeIndex)
            if (westFlowAllowed(i, j)):
                connectedNodeIndex = numCols*i + j + 1
                myGraph.add_edge(nodeIndex, connectedNodeIndex)

    pacificSet = set()
    atlanticSet = set()

    for i in range(numRows):
        for j in range(numCols):
            nodeIndex = numCols*i + j
            if (myGraph.is_connected(nodeIndex, pacIndex)):
                pacificSet.add((i,j))
            if (myGraph.is_connected(nodeIndex, atlIndex)):
                atlanticSet.add((i,j))

    #print("Pacific Set is ", pacificSet)
    #print("Atlantic Set is ", atlanticSet)
    common = pacificSet & atlanticSet
    #print("Common set is", common)
    #myGraph.display()
    retVal = list(common)

    return retVal

# Driver code
def main():
    matrices = [
        [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
        [[4, 4, 4, 3, 1], [1, 5, 3, 7, 7], [3, 1, 3, 7, 5], [1, 2, 4, 4, 7], [4, 3, 1, 7, 1]],
        [[7, 3, 5, 2, 8], [2, 3, 4, 5, 6], [3, 9, 6, 8, 4]],
        #[[1, 1], [0, 1], [0, 0]]
        [[1, 0, 1], [1, 1, 0], [1, 1, 1]],
        [[2, 3, 4, 5, 6, 7, 8], [2, 9, 3, 8, 4, 5, 6],[3, 4, 6, 7, 8, 5, 4], [9, 1, 5, 6, 7, 5, 5]]
    ]

    for i in range(len(matrices)):
        print(i + 1, ".\t Input heights: ", sep="")
        #print_matrix(matrices[i])
        print("\n\t Common coordinates: ", estimate_water_flow(matrices[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()

