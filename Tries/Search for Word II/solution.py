class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

class Solution:
    def findWords(self, board, words):
        def backtrack(row, col, node, path):
            char = board[row][col]
            curr_node = node.children[char]
            path += char

            if curr_node.is_end_of_word:
                result.add(path)
                curr_node.is_end_of_word = False

            board[row][col] = "#"
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] in curr_node.children:
                    backtrack(new_row, new_col, curr_node, path)

            board[row][col] = char

        # 建立 Trie
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        result = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie.root.children:
                    backtrack(row, col, trie.root, "")

        return list(result)
