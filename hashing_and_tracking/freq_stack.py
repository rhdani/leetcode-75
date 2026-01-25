from Stack import *
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.itemFreqMap = defaultdict(int)
        self.freqStackMap = defaultdict(Stack)
        self.maxFreqCounter = 0

    def push(self, value):
        oldFreq = self.itemFreqMap[value]
        newFreq = oldFreq + 1
        self.itemFreqMap[value] = newFreq
        self.freqStackMap[newFreq].push(value)
        self.maxFreqCounter = max(self.maxFreqCounter, newFreq)

    def pop(self):
        st1 = self.freqStackMap[self.maxFreqCounter]
        retVal = st1.pop()
        if st1.is_empty():
            self.maxFreqCounter -= 1
        self.itemFreqMap[retVal] -= 1
        return retVal

# Driver code
def main():
    inputs = [5, 7, 7, 7, 4, 5, 3]
    obj = FreqStack()
    print("\t Input Stack: ", inputs, "\n", sep="")

    for i in inputs:
        obj.push(i)

    for i in range(len(inputs)):
        print(i + 1, ".\t Popping out the most frequent value... ", sep="")
        print("\t Value removed from stack is: ", obj.pop(), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
