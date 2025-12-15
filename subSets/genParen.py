def generate_combinations(n):

    result = []

    def backtrack(inputStr, openCount, closeCount):
        if (openCount == n and closeCount == n):
            result.append(inputStr)
        if (openCount < n):
            newStr = inputStr + "("
            backtrack(newStr, openCount + 1, closeCount)
        if (closeCount < n and closeCount < openCount):
            newStr = inputStr + ")"
            backtrack(newStr, openCount, closeCount + 1)

    aStr = ""
    backtrack(aStr, 0, 0)
    return result

def print_result(result):
    for rs in result:
        print("\t\t ", rs)

# Driver code
def main():
    n = [1, 2, 3, 4, 5]

    for i in range(len(n)):
        print(i + 1, ".\t n = ", n[i], sep="")
        print("\t All combinations of valid balanced parentheses: ")

        result = generate_combinations(n[i])
        print_result(result)

        print("-" * 100)


if __name__ == '__main__':
    main()

