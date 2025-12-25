from collections import defaultdict, deque

def alien_order(words):

    alphabet_graph = {char: set() for word in words for char in word}
    indegree = {node: 0 for node in alphabet_graph}
    
    for i in range(len(words)):
        if i == 0:
            continue
        currentWord, previousWord = words[i], words[i-1]
        if (currentWord.startswith(previousWord)):
            if len(currentWord) < len(previousWord):
                return ""
            else:
                continue
        if (previousWord.startswith(currentWord) and previousWord != currentWord):
            return ""
        j = 0
        curChar = currentWord[j]
        prevChar = previousWord[j]
        minLength = min(len(currentWord), len(previousWord))
        for j in range(minLength):
            curChar = currentWord[j]
            prevChar = previousWord[j]
            if curChar != prevChar:
                if curChar not in alphabet_graph[prevChar]:
                    alphabet_graph[prevChar].add(curChar)
                    indegree[curChar] += 1
                break

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
    #If topo_order doesn't contain all characters, there was a cycle
    if (len(topo_order) != len(alphabet_graph)):
        return ""
    return "".join(topo_order)

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

