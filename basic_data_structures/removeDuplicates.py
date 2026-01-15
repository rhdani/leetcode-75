def remove_duplicates(s):

    myStack = []
    stackSize = 0
    for i in range(len(s)):
        if len(myStack) == 0:
            myStack.append(s[i])
            stackSize += 1
            continue
        top = stackSize - 1
        if top < 0:
            continue
        if (s[i] == myStack[top]):
            myStack.pop()
            stackSize = stackSize - 1
        else:
            myStack.append(s[i])
            stackSize = stackSize + 1
    
    return "".join(myStack)

# Driver code
def main():
    inputs = ["g", 
        "ggaabcdeb", 
        "abbddaccaaabcd",
        "aannkwwwkkkwna", 
        "abbabccblkklu"
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tRemove duplicates from string: '", inputs[i], "'", sep = "")
        resulting_string = remove_duplicates(inputs[i])
        print("\tString after removing duplicates: ", resulting_string, sep = "")
        print('-'*100)


if __name__ == "__main__":
    main()
