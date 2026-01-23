from collections import defaultdict

def permute_palindrome(st):
    myMap = defaultdict(int)
    if not st:
        return True
    for char in st:
        myMap[char] += 1
    
    counter = 0
    for key, value in myMap.items():
        if value%2 == 1:
            counter += 1
            if counter > 1:
                return False
    return True

# Driver Code
def main():
    str_array = ["baefeab", "abc", "xzz", "jjadd", "kllk"]
    for i in range(len(str_array)):
        print(i + 1, ".\tInput string: '", str_array[i], "'", sep="")
        result = permute_palindrome(str_array[i])
        if result:
            print("\n\tInput string has permutations that are palindromes.")
        else:
            print("\n\tInput string does not have a permutation that's a palindrome.")
        print("-"*100)


if __name__ == "__main__":
    main()
