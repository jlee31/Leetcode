# ============================================================
# TRIES (PREFIX TREES)
# ============================================================
# When to use:
#   - "starts with" / prefix search
#   - autocomplete / suggest words
#   - check if any word in a dictionary matches a pattern
#   - problem says: "starts with", "search suggestion", "all/any words"
#
# Key idea:
#   - each node = one character
#   - path from root = prefix of a stored word
#   - is_end marks where a complete word ends


# ── TRIE IMPLEMENTATION ─────────────────────────────────────

class TrieNode:
    def __init__(self):
        self.children = {}   # char → TrieNode
        self.is_end = False  # True if a word ends here


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end   # must end here — "car" ≠ "cart"

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True   # just need to reach the end of prefix

    def find_all_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        self._dfs(node, list(prefix), results)
        return results

    def _dfs(self, node, path, results):
        if node.is_end:
            results.append(''.join(path))
        for char, child in node.children.items():
            path.append(char)
            self._dfs(child, path, results)
            path.pop()


# ── TRIE WITH WILDCARD SEARCH ───────────────────────────────
# '.' matches any character (like regex)

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        def dfs(j, node):
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    return any(dfs(i + 1, child) for child in node.children.values())
                if c not in node.children:
                    return False
                node = node.children[c]
            return node.is_end

        return dfs(0, self.root)


# ── USAGE EXAMPLE ───────────────────────────────────────────

trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")

print(trie.search("app"))            # True
print(trie.search("ap"))             # False (not a complete word)
print(trie.starts_with("app"))       # True
print(trie.find_all_with_prefix("app"))  # ['app', 'apple', 'application']
