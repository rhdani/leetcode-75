def is_valid(s):
    stack = []

    parenthesis_map = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'  # Optional: for angle brackets
    }

    for i in range(len(s)):
        if ((s[i] == "(") or (s[i] == "[") or (s[i] == "{")):
            stack.append(s[i])

        if ((s[i] == ")") or (s[i] == "]") or (s[i] == "}")) :
            if not stack:
                return False
            if (s[i] == parenthesis_map.get(stack[-1])):
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False

# Driver code
def main():
    inputs = ["(){}[]", "{}[]{}[{}])", "(){[{()}]}", "))){{}}}]]", "{[()}"]

    for i in range(len(inputs)):
        print(i + 1, ". Input string = ", inputs[i], sep="")
        print("   Valid parentheses = ", is_valid(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()

