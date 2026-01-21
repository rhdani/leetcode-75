from collections import deque

def word_ladder(src, dest, words):
    def differ_by_one(a: str, b: str) -> bool:
        if len(a) != len(b):
            return False

        diff = 0
        for c1, c2 in zip(a, b):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return False

        return diff == 1
    myq = deque()
    mySet = set(words)
    myq.append((src, 1))              # store (word, distance)
    if src in mySet:
        mySet.remove(src)

    while myq:
        currWord, dist = myq.popleft()
        if currWord == dest:
            return dist
        for word in list(mySet):      # iterate over snapshot so we can remove safely
            if differ_by_one(currWord, word):
                myq.append((word, dist + 1))
                mySet.remove(word)    # mark visited when enqueued
    return 0

if __name__ == '__main__':
    words_list = [["hog", "dot", "pot", "pop", "mop", "map", "cap", "cat"],
                  ["hot", "dot", "lot", "log", "cog"],
                  ["hot", "not", "dot", "lot", "cog"],
                  ["hog", "dot", "pot", "pop", "mop", "map", "cap", "cat"],
                  ["hot", "dot", "lot", "log", "cog", "com", "cam", "frog"]]
    src_list = ["dog", "hit", "hat", "dog", "dog"]
    dest_list = ["cat", "cog", "log", "cat", "frog"]

    # Additional edge-case tests added below
    # 6: empty words list (no path)
    # 7: src == dest
    # 8: direct neighbor single-letter words
    # 9: differing word lengths (no valid transitions)
    # 10: extra valid multi-step path

    # append edge cases
    words_list.append([])
    src_list.append("a")
    dest_list.append("b")

    words_list.append(["hit"])
    src_list.append("hit")
    dest_list.append("hit")

    words_list.append(["a", "b"])
    src_list.append("a")
    dest_list.append("b")

    words_list.append(["ab", "abc", "bbc"])
    src_list.append("ab")
    dest_list.append("bbc")

    words_list.append(["hot", "dot", "dog", "cog", "lot", "log", "hit"])
    src_list.append("hit")
    dest_list.append("cog")

    for i in range(len(src_list)):
        print(i + 1, ".\tsrc: \"", src_list[i], "\"", sep = "")
        print("\tdest: \"", dest_list[i], "\"", sep = "")
        print("\tAvailable words: ", words_list[i], "\n", sep = "")
        print("\tLength of shortest chain is: ", word_ladder(src_list[i], dest_list[i], words_list[i]))
        print("-" * 100)