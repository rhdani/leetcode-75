from collections import defaultdict, Counter, deque

def alien_order(words):

    alphabet_graph = defaultdict(list)
    for item in words:
        for char in item:
            if char not in alphabet_graph:
                alphabet_graph[char] = []

    indegree = {node: 0 for node in alphabet_graph}
    
    for i in range(len(words)):
        if i == 0:
            continue
        currentWord = words[i]
        previousWord = words[i-1]
        if (currentWord.startswith(previousWord)):
            if len(currentWord) < len(previousWord):
                return ""
            else:
                continue
        if (previousWord.startswith(currentWord) and previousWord != currentWord):
            return ""
        j = 0;
        curChar = currentWord[j]
        prevChar = previousWord[j]
        minLength = min(len(currentWord), len(previousWord))
        while curChar == prevChar:
            j = j + 1
            curChar = currentWord[j]
            prevChar = previousWord[j]

        alphabet_graph[prevChar].append(curChar)
        indegree[curChar] += 1
    # Add nodes with 0 in-degree to the queue
    queue = deque()
    for item in indegree:
        if indegree[item] == 0:
            queue.append(item)
    
    topo_order = []
    while queue:
        # Step 2: Remove a node from the queue
        u = queue.popleft()
        topo_order.append(u)

        # Step 3: For each neighbor, decrement indegree
        for v in alphabet_graph[u]:
            indegree[v] -= 1
            # If indegree becomes 0, it's ready to be processed
            if indegree[v] == 0:
                queue.append(v)
        
    #print(alphabet_graph)
    #print(indegree)
    #print(topo_order)
    
    retVal = ""
    if (len(topo_order) != len(alphabet_graph)):
        return retVal
    for item in topo_order:
        retVal = retVal + item

    return retVal

# Driver code
def main():
    words = [
        ["mzosr", "mqov", "xxsvq", "xazv", "xazau", "xaqu",
            "suvzu", "suvxq", "suam", "suax", "rom", "rwx", "rwv"],
        ["vanilla", "alpine", "algor", "port",
            "norm", "nylon", "ophellia", "hidden"],
        ["passengers", "to", "the", "unknown"],
        ["alpha", "bravo", "charlie", "delta"],
        ["jupyter", "ascending"]]

    for i in range(len(words)):
        print(i + 1, ".\twords = ", words[i], sep="")
        print("\tDictionary = \"", alien_order(words[i]), "\"", sep="")
        print("-"*100)


if __name__ == "__main__":
    main()

