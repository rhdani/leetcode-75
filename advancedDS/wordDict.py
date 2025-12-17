from Trie import TrieNode

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def get_words(self) -> list:
        result = []
        self._collect(self.root, "", result)
        return result

    def _collect(self, node: TrieNode, prefix:str, resultArr) -> None:
        letters = node.children.keys()
        for i, letter in enumerate(letters):
            child_node = node.children[letter]
            new_prefix = prefix + letter
            if child_node.is_word:
                resultArr.append(new_prefix)
                return
            self._collect(child_node, new_prefix, resultArr)

    def print_dict(self) -> None:
        print("--- Words ---")
        self._print_dict_dfs(self.root, "", "")
        print("----------------------")

    def _print_dict_dfs(self, node: TrieNode, prefix: str, indent: str) -> None:
        """
        A recursive Depth-First Search (DFS) function to print the Dict.

        :param node: The current TrieNode being processed.
        :param prefix: The string accumulated from the root to the current node.
        :param indent: The visual prefix (indentation lines) for the current level.
        """
        # Get the sorted characters to ensure consistent printing order
        sorted_chars = sorted(node.children.keys())

        # Determine if this is the last child of its parent (for drawing L or T)
        for i, char in enumerate(sorted_chars):
            child_node = node.children[char]
            is_last = (i == len(sorted_chars) - 1)

            # 1. Print the current character/node
            # Select the appropriate connector line for the tree visualization
            # '└── ' for the last child, '├── ' for others
            connector = indent + ("└── " if is_last else "├── ")

            # Build the character label
            char_label = f"'{char}'"
            if child_node.is_word:
                char_label += " (END)" # Indicate the end of a word

            print(f"{connector}{char_label}")

            # 2. Prepare for the recursive call (move to the next level)
            # The new indent must maintain the vertical line for non-last children.
            new_indent = indent + ("    " if is_last else "│   ")
            new_prefix = prefix + char

            # 3. Recursive call to print the child
            self._print_dict_dfs(child_node, new_prefix, new_indent)

    def add_word(self, word) -> None:
        n = len(word)
        node = self.root

        for i, val in enumerate(word):
            if val not in node.children:
                node.children[val] = TrieNode()
            node = node.children.get(val)
            if (i == n - 1):
                if (node.is_word):
                    return
                node.is_word = True


    def _search_helper(self, node, word, i) -> bool:
        if not node:
            return False
        if (len(word) == i):
            return node.is_word

        if (word[i] == '.'):
            return any(self._search_helper(child, word, i + 1)
                   for child in node.children.values())
        else:
            return self._search_helper(node.children.get(word[i]), word, i + 1)

    def search_word(self, word) -> bool:
        return self._search_helper(self.root, word, 0)

    def print_words(self) -> None:
        self.print_dict()

# Driver code
def main():
    obj = WordDictionary()
    words = ["add", "sky", "hello", "multi", "addition", "sky", "multiply", "table"]
    i = 1
    for w in words:
        print(i, ".\tAdding word: '", w, "'", sep="")
        obj.add_word(w)
        print("-" * 100, sep="")
        i += 1

    wordSearch = ["add", "sky", "hello", "helo", "multiple", "...le", "..llo", "..r"]
    for v in wordSearch:
        print(i, ".\tSearching word: '", v, "'", sep="")
        print("\t", obj.search_word(v), sep="")
        print("-" * 100, sep="")
        i += 1

    
    print(i, ".\tGetting all words: ", obj.get_words(), sep = "")
    print("-" * 100, sep="")

if __name__ == "__main__":
    main()
