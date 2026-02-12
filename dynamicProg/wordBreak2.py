'''
Docstring for wordBreak2
You are given a string, s, and an array of strings, word_dict, 
representing a dictionary. Your task is to add spaces to s 
to break it up into a sequence of valid words from word_dict. 
We are required to return an array of all possible sequences 
of words (sentences). The order in which the sentences are 
listed is not significant.
'''
def word_break(s, word_dict):
    memo = {}
    
    def dp(start):
        # If already computed, return from memo
        if start in memo:
            return memo[start]
        
        # Base case: reached end of string
        if start == len(s):
            return [[]]
        
        result = []
        
        # Try all possible words starting from 'start'
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_dict:
                # Get all solutions from the rest of the string
                rest_solutions = dp(end)
                # Prepend current word to each solution from the rest
                for solution in rest_solutions:
                    result.append([word] + solution)
        
        memo[start] = result
        return result
    
    # Get all solutions and join them as strings
    solutions = dp(0)
    return [' '.join(sentence) for sentence in solutions]

# Driver Code
def main():

    s = ["vegancookbook", "catsanddog", "highwaycrash",
         "pineapplepenapple", "screamicecream", "educativecourse"]

    word_dict = ["oghi", "ncoo", "kboo", "inea",
        "icec", "ghway", "tsand", "anco", "eame", "ghigh", "hi", "way", "wa",
        "amic", "mi", "ed", "cecre", "pple", "reamicecreamed", "ena", "tsa", "ami", "hwaycrashpineapplepenapplescreamicecreamed", "lepen", "okca", "highway", "ples", "atsa", "oghig", "ookb", "epe", "ookca", "nea", "cra", "lepe", "vegancookbookcatsandd",
        "kc", "ra", "le", "ay", "crashpineapple", "ycras", "vegancookbookcatsanddoghighwaycrashpineapplepenapplescre", "doghi", "nddo", "hway", "vegancookbookcatsanddoghi", "vegancookbookcatsanddoghighwaycr", "at", "mice", "nc", "d", "enapplescreamicecreamed", "h",
        "ecrea", "nappl", "shp", "kbo", "yc", "vegancookbookcatsanddoghighwaycrashpineapplepenapplescream", "cat", "waycrashpineapplepenapplescreamicecreamed", "tsan", "vegancookbookcatsanddoghighwaycrashpineap", "ganco", "lescr", "sand", "applescreamicecreamed", "vegancookbookcatsanddoghig", "pi", "vegancookbookcatsanddoghighwaycrashpineapp", "cookb", "okcat", "neap", "nap", "oghighwaycrashpineapplepenapplescreamicecreamed", "crashpineapplepenapplescreamicecreamed",
        "ashpi", "ega", "escreamicecreamed", "hwa", "rash", "cre", "micecreamed", "plepe", "coo", "epen", "napp", "wayc", "vegancookbookcatsanddoghighwaycrashpinea", "vegancookbookcatsanddogh", "plep", "ice", "ple", "gh", "ghw", "cook", "pl", "app", "ic", "pinea", "hello", "dog", "vegancookbookcat", "eamed", "ook", "lesc", "ddog", "ca", "vegancookbookcatsanddoghighwaycrashpineapplepenapplescreamice", "c", "escr", "penap", "boo", "eami", "ecreamed", "vegancookbookcatsanddoghighwaycrashpi", "igh", "mic", "ganc", "vegancookbookcatsanddoghighwaycrashpineapplepenap",
        "eappl", "vegancookbookcatsanddoghighway", "ep", "penapple", "b", "ycrashpineapplepenapplescreamicecreamed", "pin", "book", "p", "sa", "okb", "andd", "ayc", "sh", "vegan", "cookbook"]

    print("The list of words we can use to break down the strings are:\n\n", word_dict, "\n")
    print("-" * 100)
    for i in range(len(s)):
        print("Test Case #", i+1, "\n\nThe possible strings from the string '" +
              str(s[i]) + "' are the following combinations:", sep="")
        print("\n" + str(word_break(str(s[i]), word_dict)))
        print("-" * 100)

if __name__ == '__main__':
    main()
