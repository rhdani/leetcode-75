from Stack import *

def remove_duplicates(s):

    myStack = Stack()
    for i in range(len(s)):
        if myStack.is_empty():
            myStack.push(s[i])
            continue
        if (s[i] == myStack.top()):
            myStack.pop()
        else:
            myStack.push(s[i])
    return myStack.getString()

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
