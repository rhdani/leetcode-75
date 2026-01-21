def next_greater_element(nums1, nums2):
    
    myStack = []
    myMap = {}
    for num in nums2:
        if len(myStack) == 0:
            myStack.append(num)
            continue
        while len(myStack) > 0 and num > myStack[-1]:
            key = myStack.pop()
            myMap[key] = num
        
        myStack.append(num)
        
    result = []            
    for num in nums1:
        if num in myMap:
            result.append(myMap[num])
        else:
            result.append(-1)
    return result
def main():
    A = [[2, 4], [3, 2, 5], [14, 45, 52], [1, 3, 2], [4, 2], [0]]
    B = [[1, 2, 3, 4], [2, 3, 5, 1], [52, 14, 45, 65], [1, 3, 2, 4, 5],
         [1, 2, 4, 3], [0]]
    x = 1
    for i in range(len(A)):
        print(x, ".\tNums 1 = ", A[i], sep="")
        print("\tNums 2 = ", B[i], sep="")
        print("")
        print("\tThe Next Greater Element Array = ",
              next_greater_element(A[i], B[i]))
        print(100 * '-')
        x += 1


if __name__ == '__main__':
    main()
