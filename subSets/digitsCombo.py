def letter_combinations(digits):

    result = []
    if not digits or len(digits) == 0:
        return result
    numbers_map = {
        '1': "",
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    def letter_combo_rec(index, fragment):
        if index == len(digits):
            result.append(fragment)
            return

        for ch in numbers_map[digits[index]]:
            letter_combo_rec(index + 1, fragment + ch)

    letter_combo_rec(0, "")
    return result

# driver code
def main():
    digits_array = ["23", "73", "426", "78", "925", "2345"]
    counter = 1
    for digits in digits_array:
        print(counter, ".\t All letter combinations for '",
              digits, "': ", letter_combinations(digits), sep="")
        counter += 1
        print("-" * 100)


if __name__ == "__main__":
    main()

