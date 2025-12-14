def swap_letters(word: str, i: int, j: int) -> str:
    """
    Swaps the letters at position i and position j in a given word.

    :param word: The input string (word).
    :param i: The index of the first character to swap.
    :param j: The index of the second character to swap.
    :return: A new string with the characters at i and j swapped.
    :raises IndexError: If i or j are out of bounds for the word.
    """
    n = len(word)

    # 1. Input Validation: Check if indices are valid
    if not (0 <= i < n and 0 <= j < n):
        raise IndexError(f"Indices {i} and {j} are out of bounds for word of length {n}.")

    # 2. Conversion: Convert the string to a mutable list of characters
    char_list = list(word)

    # 3. Swap: Perform the swap using tuple assignment (Pythonic way)
    # This is equivalent to:
    # temp = char_list[i]
    # char_list[i] = char_list[j]
    # char_list[j] = temp
    char_list[i], char_list[j] = char_list[j], char_list[i]

    # 4. Conversion Back: Join the list of characters back into a string
    new_word = "".join(char_list)

    return new_word

def helper(inputWord, index):
    retVal = []
    if not inputWord:
        return retVal
    n = len(inputWord)
    if n == 1:
        retVal.append(inputWord)
        return retVal
    if index < 0 or index >= n:
        return retVal
    if index == n - 2:
        word1 = inputWord[:index] + inputWord[n-1] + inputWord[index]
        word2 = inputWord[:index] + inputWord[index] + inputWord[index + 1:]
        retVal.append(word1)
        retVal.append(word2)
        return retVal
    for i in range(index, n):
        myWord = swap_letters(inputWord, index, i)
        temp = helper(myWord, index + 1)
        retVal.extend(temp)

    return retVal

def permute_word(word):
    result = []

    if not word or len(word) == 0:
        return result
    if len(word) == 1:
        result.append(word)
        return result

    result = helper(word, 0)

    return result

# Driver code
def main():
    input_word = ["ab", "bad", "abcd"]

    for index in range(len(input_word)):
        permuted_words = permute_word(input_word[index])

        print(index + 1, ".\t Input string: '", input_word[index], "'", sep="")
        print("\t All possible permutations are: ",
              "[", ', '.join(permuted_words), "]", sep="")
        print('-' * 100)


if __name__ == '__main__':
    main()

