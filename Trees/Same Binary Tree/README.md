**Same Binary Tree**
-
🔗 Link: Same Binary Tree

💡 Difficulty: Easy

🛠️ Topics: 遞迴比較（Recursive Comparison）、結構相同性（Structural Equivalence）、二元樹的遍歷（Tree Traversal）、邊界條件（Base Cases）

========================================

Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [4,7], q = [4,null,7]
Output: false

Example 3:

Input: p = [1,2,3], q = [1,3,2]
Output: false

Constraints:

．0 <= The number of nodes in both trees <= 100.

．-100 <= Node.val <= 100

================================================

**UMPIRE Method:**

**Understand**

1.問題描述：給定兩個二元樹 p 和 q，如果它們的結構完全相同且每個節點的值相同，則返回 true；否則返回 false。

2.定義：樹 p 和樹 q 被視為相同，當且僅當它們的節點數量、結構和每個對應節點的值都相同。

**Match**

1.遞迴方法：使用深度優先搜尋（DFS）來比較兩棵樹的結構和節點值。如果兩棵樹的根節點相同，則遞迴比較其左右子樹。

**Plan**

1.檢查 p 和 q 是否都為 None，如果是，則返回 true。

2.檢查 p 和 q 中任一樹是否為 None，如果只有一棵樹是 None，則返回 false。

3.檢查 p 和 q 的根節點值是否相同。如果不同，則返回 false。

4.使用遞迴，分別比較 p 的左子樹和 q 的左子樹，及 p 的右子樹和 q 的右子樹，返回兩者的比較結果。

**Implement**

see solution.py

**Review**

1.邊界情況：檢查兩棵樹都是空樹的情況，返回 true；如果其中一棵是空樹而另一棵不是，則返回 false。

2.結構檢查：保證樹的結構在遞迴過程中被檢查。

**Evaluate**

．時間複雜度：時間複雜度為 O(n)，其中 n 是樹中節點的數量，因為每個節點都會被訪問一次。

．空間複雜度：空間複雜度為 O(h)，其中 h 是樹的高度，因為最壞的情況下，遞迴的深度等於樹的高度。


