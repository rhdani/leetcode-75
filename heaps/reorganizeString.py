# importing libraries
from collections import defaultdict
import heapq

def reorganize_string(str):

    result = []
    freqMap = defaultdict(int)
    if not str or len(str) == 0:
        return ""
    if len(str) == 1:
        return str
    for item in str:
        freqMap[item] += 1
    myHeap = []
    for key,val in freqMap.items():
        heapq.heappush(myHeap, (-val, key))
    prevChar = ""
    prevCount = 0
    while len(myHeap) > 0:
        val, char = heapq.heappop(myHeap)
        result.append(char)
        if (prevChar != "" and abs(prevCount) > 0):
            heapq.heappush(myHeap, (prevCount, prevChar))
            prevCount = 0
            prevChar = ""
        if abs(val) > 1:
            freqMap[char] -= 1
            prevChar = char
            prevCount = val + 1
            
    #Result string should be same length as input string
    if (len(result) != len(str)):
        return ""

    return "".join(result)

# Driver code
def main():
    # Primary test cases + additional edge cases
    test_cases = [
        "programming",
        "hello",
        "fofjjb",
        "abbacdde",
        "aba",
        "awesome",
        "aaab",
        # Edge cases
        "",         # empty string
        "a",        # single character
        "aa",       # two same characters -> impossible
        "aab",      # simple reorganizable
        "aaabb",    # multiple frequencies
        "aaaaab",   # high-frequency impossible
        "😊😊abc",   # unicode / emoji
    ]
    for i in range(len(test_cases)):
        print(i+1, '. \tInput string: "', test_cases[i], '"', sep="")
        temp = reorganize_string(test_cases[i])
        print('\tReorganized string: "', temp + '"' if temp else '"', sep="")
        print("-"*100)


if __name__ == '__main__':
    main()
        