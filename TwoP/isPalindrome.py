def is_palindrome(s):
  left, right = 0, len(s) - 1

  while left < right:
      if not s[left].isalnum():
        left += 1
        continue

      if not s[right].isalnum():
        right -= 1
        continue

      if s[left].lower() != s[right].lower():
        return False
      
      left += 1
      right -= 1

  return True

def main():
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "1A@2!3 23!2@a1",
        "No 'x' in Nixon",
        "12321",
    ]

    for i in test_cases:
        print("\n\tString:", i,"\n")
        print(is_palindrome(i))
        print("-" * 100)


if __name__ == "__main__":
    main()
