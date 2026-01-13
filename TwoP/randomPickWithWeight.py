'''
Docstring for randomPickWithWeight
You’re given an array of positive integers, weights, 
where weights[i] is the weight of the ithindex.

Write a function, Pick Index(), which performs weighted random selection to 
return an index from the weights array. The larger the value of weights[i], 
the heavier the weight is, and the higher the chances of its index being picked.

Suppose that the array consists of the weights 
[12, 84, 35]. In this case, the probabilities of picking the indexes 
will be as follows:

Index 0: 
12/(12+84+35)=9.2%


Index 1: 
84/(12+84+35)=64.1%

Index 2: 
35/(12+84+35)=26.7%
'''


import random

class RandomPickWithWeight:

    def __init__(self, weights):
        self.total = 0
        self.maxSum = [0] * len(weights)
        self.maxSum[0] = weights[0]
        for i in range (len(weights)):
            self.total += weights[i]
            if (i > 0):
                self.maxSum[i] = self.maxSum[i-1] + weights[i]
        #print("Total, sum weights ", self.total, self.maxSum)

    def pick_index(self):
        x = random.randint(1, self.total)
        start = 0
        end = len(self.maxSum) - 1
        while (start <= end):
            #print("Start and end rand", start, end, x)
            mid = (start + end)//2
            #print("Mid ", mid)
            if (x == self.maxSum[mid]):
                return mid
            if (x > self.maxSum[mid]):
                start = mid + 1
            else:
                end = mid - 1
        return start

# Driver code
def main():
    counter = 900

    weights = [[1, 2, 3, 4, 5],
                [1, 12, 23, 34, 45, 56, 67, 78, 89, 90],
                [10, 20, 30, 40, 50],
                [1, 10, 23, 32, 41, 56, 62, 75, 87, 90],
                [12, 20, 35, 42, 55],
                [10, 10, 10, 10, 10],
                [10, 10, 20, 20, 20, 30],
                [1, 2, 3],
                [10, 20, 30, 40],
                [5, 10, 15, 20, 25, 30]]

    dict = {}
    for i in range(len(weights)):
        print(i + 1, ".\tList of weights: ", weights[i], ", pick_index() called ", counter, " times", "\n", sep="")
        [dict.setdefault(l, 0) for l in range(len(weights[i]))]
        sol = RandomPickWithWeight(weights[i])
        for j in range(counter):
            index = sol.pick_index()
            dict[index] += 1
        print("-"*105)
        print("\t{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<20}{:<5}{:<15}".format( \
            "Indexes", "|", "Weights", "|", "Occurences", "|", "Actual Frequency", "|", "Expected Frequency"))
        print("-"*105)
        for key, value in dict.items():

            print("\t{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<20}{:<5}{:<15}".format(key, "|", weights[i][key], "|", value, "|", \
                str(round((value/counter)*100, 2)) + "%", "|", str(round(weights[i][key]/sum(weights[i])*100, 2))+"%"))
        dict = {}
        print("\n", "-"*105, "\n", sep="")


if __name__ == '__main__':
    main()

