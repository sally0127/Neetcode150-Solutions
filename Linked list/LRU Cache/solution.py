class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # HashMap to store key -> Node
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        """Add a node right after head."""
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.value = value
            self._add(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove LRU entry from the tail
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)


=====================================================================

关键部分：

．双向链表：

  ．head 和 tail 是虚拟节点，帮助管理链表。
  
  ．_add 和 _remove 是辅助函数，分别用于在链表中插入和删除节点。

哈希表：

  ．cache 是哈希表，用于存储 key 到节点的映射，方便在 O(1) 时间内查找。

LRU 淘汰机制：

  ．当缓存达到容量上限时，删除链表尾部的节点（最少使用的节点）。

======================================================================

其實 **雙向鏈表** 和 **HashMap** 是並行設置的，並不是說一定要「設定好 LRU 才能建立 HashMap」。兩者是互相配合工作的，具體的流程如下：

1. **設定雙向鏈表**：這部分負責資料的順序管理。雙向鏈表會用來保存哪些資料是最近使用的，哪些是最久未使用的。

2. **設定 HashMap**：HashMap 提供快速查找資料的能力。我們可以直接通過 key 快速定位到雙向鏈表中的節點（node），不需要遍歷整個鏈表來查找。

3. **LRU 機制（算法）**：LRU 算法本質上是依賴這兩個資料結構來實現。當你執行 `get` 或 `put` 操作時，雙向鏈表和 HashMap 一起工作：
   - **查找資料** 時，先用 HashMap 快速找到對應的節點。
   - 然後利用雙向鏈表將這個節點移動到前面，標記為「最近使用」。
   - 當需要刪除最久未使用的資料時，從雙向鏈表尾部刪除節點，並在 HashMap 中移除對應的鍵值對。

### 結論：
**雙向鏈表和 HashMap** 是 LRU 算法的基礎組件，這兩者必須同時設置，才能實現 LRU 的功能。你不需要「先完成 LRU 再設定 HashMap」，而是這兩者共同組成了 LRU 緩存的核心架構。

==========================================================================

你提到的「為什麼在程式碼中要先設定雙向鏈表，再設定 LRU，然後才是 HashMap」，其實更多是從程式的結構和邏輯需求來考慮的，並不是說它們之間有嚴格的先後順序限制。

讓我們一步步看：

### 1. **先設定雙向鏈表**
   - 雙向鏈表的設置先行，是因為它需要承擔管理資料順序的責任。在 LRU 中，每次 `get` 或 `put` 都會涉及資料順序的調整（比如將最近使用的資料移到前面，或刪除最久未使用的資料）。因此，我們必須先有一個能執行這些動作的雙向鏈表結構。

   - 設置雙向鏈表包含初始化鏈表頭部和尾部的節點（通常是虛擬節點），因為這樣可以方便插入或刪除節點，並且能處理空的情況而不需要特別檢查。

### 2. **設置 LRU 機制**
   - LRU 算法是基於雙向鏈表來管理最近使用的資料順序，因此在我們設定 LRU 機制的時候，雙向鏈表的設置是基礎。如果沒有雙向鏈表，我們就無法進行節點的插入、刪除或移動。

   - 這裡是實作 LRU 核心邏輯，比如當 `get` 操作時，把查找到的節點移動到鏈表的前面，或是當 `put` 時，將新資料插入鏈表。

### 3. **最後加入 HashMap**
   - HashMap 的設置是為了在 LRU 缓存中實現 **O(1)** 的查找能力。它的作用是保存每個 key 對應的節點，這樣我們可以快速找到節點來執行對應的操作（比如在雙向鏈表中移動、更新節點等）。

   - HashMap 本身不涉及順序管理，它的唯一目的就是加速查找資料。所以在這裡，雙向鏈表和 LRU 的核心邏輯是優先要解決的問題，因為我們必須知道如何管理資料順序，然後再結合 HashMap 來加速這個過程。

### 總結程式設計順序的原因：
1. **雙向鏈表的設置** 是因為我們需要一個高效的資料結構來處理資料的插入、刪除和順序管理，這是 LRU 算法的核心基礎。
2. **LRU 邏輯設置** 是在鏈表的基礎上實作具體的「最近使用」和「最久未使用」的順序邏輯。
3. **HashMap 設置** 是為了讓我們能夠在 **O(1)** 時間內快速找到雙向鏈表中的節點，提升查找效率。

所以，雖然雙向鏈表、LRU 和 HashMap 是共同實現 LRU 缓存的組成部分，但從程式設計角度來說，我們是先建立管理資料順序的結構，再引入能快速查找資料的結構。

