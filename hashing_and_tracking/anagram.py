from collections import defaultdict
def is_anagram(str1, str2):

    if (not str1 and not str2):
        return True
    if (not str1 or not str2):
        return False
    if (len(str1) != len(str2)):
        return False
    letter_map = defaultdict(int)
    for i in range(len(str1)):
        letter_map[str1[i]]+=1
    for i in range(len(str2)):
        letter_map[str2[i]]-=1
    for key,value in letter_map.items():
        if (value):
            return False
    return True

def main():

  str1_list = ["listen", "race", "elbow", "cat", "inch"]
  str2_list = ["silent", "cares", "below", "act", "chin"]

  for i in range(len(str1_list)):
    print(i + 1, ".\tstr1: \"", str1_list[i], "\"", sep = "")
    print("\tstr2: \"", str2_list[i], "\"", sep = "")
    print('\t"', str2_list[i], '" is anagram of "', str1_list[i], '": ',is_anagram(str1_list[i],str2_list[i]), sep = "")
    print("-" * 100)

if __name__ == '__main__':
  main()
