def word_break(s, word_dict):

    dp = [False]*(len(s) + 1)
    dp[0] = True
    word_set = set(word_dict)
    for i in range(1,(len(s)+1)):
        #print("Checking for i index ", i)
        for j in range(i):
            subseq=s[j:i]
            #print("Checking for j index ", j, s[j:i])
            if (subseq in word_set and dp[j] == True):
                #print("Is true")
                dp[i] = True
                break

    return dp[-1]

# Driver Code
def main():

    s = ["vegancookbook", "catsanddog", "highwaycrash",
         "pineapplepenapple", "screamicecream", "educativecourse"]
    word_dict = ["ncoo", "kboo", "inea", "icec", "ghway", "and", "anco", "hi", "way", "wa",
                 "amic", "ed", "cecre", "ena", "tsa", "ami", "lepen", "highway", "ples",
                 "ookb", "epe", "nea", "cra", "lepe", "ycras", "dog", "nddo", "hway",
                 "ecrea", "apple", "shp", "kbo", "yc", "cat", "tsan", "ganco", "lescr",
                 "ep", "penapple", "pine", "book", "cats", "andd", "vegan", "cookbook"]

    print("The list of words we can use to break down the strings are:\n\n", word_dict, "\n")
    print("-" * 100)
    for i in range(len(s)):
        print("Test Case #", i+1, "\n\nInput: '" + str(s[i])+"'\n")
        print("\nOutput: " + str(word_break(str(s[i]), word_dict)))
        print("-" * 100)

if __name__ == '__main__':
    main()

