class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    # A function to insert a word in trie.
    def insert(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children.get(c)

        node.is_word = True

    # A function to search for a word in the trie.
    def search(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children.get(c)

        return node.is_word

    # A function to search for a prefix of a word in the trie.
    def search_prefix(self, prefix):
        node = self.root

        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)

        return True

    def print_trie(self) -> None:
        """
        Public method to start the recursive printing process.
        """
        print("--- Trie Structure ---")
        # Start DFS from the root node
        self._print_trie_dfs(self.root, "", "")
        print("----------------------")

    def _print_trie_dfs(self, node: TrieNode, prefix: str, indent: str) -> None:
        """
        A recursive Depth-First Search (DFS) function to print the Trie.

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
            self._print_trie_dfs(child_node, new_prefix, new_indent)

# Driver Code
def main():
    keys = ["the", "a", "there", "answer"]
    trie_for_keys = Trie()
    num = 1
    for x in keys:
        print(num, ".\tInsert key: '", x, "'", sep="")
        trie_for_keys.insert(x)
        num += 1
        print("-" * 100)
    trie_for_keys.print_trie()

    search = ["a", "answer", "xyz", "an"]
    for y in search:
        print(num, ".\tSearch key: '", y, "'", sep="")
        print("\tKey found? ", trie_for_keys.search(y), sep="")
        num += 1
        print("-" * 100)

    searchPrefix = ["b", "an"]
    for z in searchPrefix:
        print(num, ".\tSearch prefix: '", z, "'", sep="")
        print("\tPrefix found? ", trie_for_keys.search_prefix(z), sep="")
        num += 1
        print("-" * 100)


if __name__ == "__main__":
    main()

