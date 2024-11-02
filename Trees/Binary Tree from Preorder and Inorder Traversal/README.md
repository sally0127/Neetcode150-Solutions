**Binary Tree from Preorder and Inorder Traversal**
-

🔗 Link: Binary Tree from Preorder and Inorder Traversal

💡 Difficulty: Medium

🛠️ Topics: 樹的遍歷(Tree Traversal)、Tree Reconstruction(樹的重建)

===========================================================

You are given two integer arrays preorder and inorder.

    ．preorder is the preorder traversal of a binary tree
    
    ．inorder is the inorder traversal of the same tree
    
    ．Both arrays are of the same size and consist of unique values.

Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:

Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
Output: [1,2,3,null,null,null,4]

Example 2:

Input: preorder = [1], inorder = [1]
Output: [1]

Constraints:

．1 <= inorder.length <= 1000.

．inorder.length == preorder.length

．-1000 <= preorder[i], inorder[i] <= 1000

=========================================================

**UMPIRE Method:**

**Understand**

1.給定： 兩個整數數組 preorder 和 inorder。

    ．preorder 是二元樹的前序遍歷結果。
    
    ．inorder 是同一棵二元樹的中序遍歷結果。

2.目標： 根據這兩個遍歷結果重建二元樹並返回其根節點。

**Match**

1.遞迴 (Recursion)：利用前序遍歷和中序遍歷的特性重建二元樹。

    ．前序遍歷的第一個元素總是根節點。
    
    ．在中序遍歷中找到根節點的位置，並根據這個位置將數組分為左子樹和右子樹。

**Plan**

1.從前序遍歷中獲取根節點的值。

2.在中序遍歷中找到根節點的索引。

3.利用根節點的索引將中序遍歷分成左子樹和右子樹。

4.利用前序遍歷的下一個元素（根的左子樹部分）來構建左子樹，然後用剩下的元素來構建右子樹。

5.使用遞迴進行上述操作，直到所有節點都被處理完。

**Implement**

see solution.py

**Review**

1.確保代碼能夠正確地從給定的前序和中序遍歷重建二元樹。

2.測試代碼的邊界情況，比如空樹或只有一個節點的樹。

**Evaluate**

1.時間複雜度：

    ．在重建二元樹的過程中，我們需要遍歷前序和中序數組。每次遞迴調用都會查找根節點在中序數組中的索引，這個查找的時間複雜度是 O(n)。
    
    ．因此，對於每個節點（n個節點），都需要執行 O(n) 的查找操作，總的時間複雜度是 O(n^2)。
    
    ．但如果使用哈希表來存儲中序遍歷中的元素及其索引，查找根節點的時間複雜度可以降低到 O(1)。這樣的話，整體時間複雜度將是 O(n)。

2.空間複雜度：

    ．空間複雜度主要由遞迴棧的深度和存儲數據的數組所決定。對於一棵高度為 h 的二元樹，遞迴棧的空間複雜度為 O(h)。
    
    ．最壞情況下（當樹是完全不平衡時），h 可以是 n，因此空間複雜度最壞情況下為 O(n)。
    
    ．此外，使用哈希表來存儲中序遍歷的索引將需要 O(n) 的額外空間。

