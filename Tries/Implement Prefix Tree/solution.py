class TrieNode:
    def __init__(self):
        self.children = {}  # 使用字典來存放子節點
        self.is_end_of_word = False  # 標記該節點是否為單字結尾

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() # 初始化前綴樹的根節點
       
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # 如果字符不在當前節點的子節點中，則新增它
            if char not in node.children:
                node.children[char] = TrieNode()
            # 移動到下一個字符的節點
            node = node.children[char]
        # 在單字結尾設置標記
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # 如果字符不在當前節點的子節點中，則表示單字不存在
            if char not in node.children:
                return False
            # 移動到下一個字符的節點
            node = node.children[char]
        # 檢查是否有設置單字結尾標記
        return node.is_end_of_word
               
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            # 如果字符不在當前節點的子節點中，則表示前綴不存在
            if char not in node.children:
                return False
            # 移動到下一個字符的節點
            node = node.children[char]
        # 成功找到整個前綴，返回 True
        return True
