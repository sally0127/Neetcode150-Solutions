**Copy Linked List with Random Pointer**
-
🔗 Link: Copy Linked List with Random Pointer

💡 Difficulty: Medium

🛠️ Topics: 深拷貝技術在鏈結串列中的應用,如何處理鏈結串列中的隨機指標,雙遍歷的鏈結串列操作技巧

============================================================

You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

．The original value val of the copied node

．A next pointer to the new node corresponding to the next pointer of the original node

．A random pointer to the new node corresponding to the random pointer of the original node

Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

Example 1:

Input: head = [[3,null],[7,3],[4,0],[5,1]]
Output: [[3,null],[7,3],[4,0],[5,1]]

Example 2:

Input: head = [[1,null],[2,2],[3,2]]
Output: [[1,null],[2,2],[3,2]]

Constraints:

．0 <= n <= 100

．-100 <= Node.val <= 100

．random is null or is pointing to some node in the linked list.

==================================================================

**UMPIRE Method:**

**Understand**

我们需要实现一个链表的深拷贝。链表的每个节点有两个指针：next 和 random。next指向下一个节点，而random可能指向链表中的任何一个节点，甚至是空节点 (null)。

需要注意的是：

1.每个节点的拷贝节点是一个全新的对象，不应该指向原链表中的节点。

2.next 和 random 指针的关系在新链表中要保持一致。

3.目标是返回新链表的头节点，使其具有相同的结构和数值，但不与原链表共享任何节点。

**Match**

针对链表的深拷贝问题，我们可以借鉴一些常见的链表问题解决方法，例如：

1.哈希表 - 可以使用哈希表存储每个原节点与其拷贝节点之间的映射关系，以便快速查找 random 指针。

2.双指针或三指针法 - 有时可以在不使用额外空间的情况下，通过巧妙的指针操作实现深拷贝。

**Plan**

我们可以通过以下步骤来实现这个深拷贝：

1.创建节点映射：

．遍历原链表的每个节点，为每个节点创建一个对应的拷贝节点并存储到哈希表中，以便于之后处理 random 指针。

2.设置 next 和 random 指针：

．再次遍历原链表，对于每个原节点的拷贝节点，设置其 next 指针和 random 指针，使其指向相应的拷贝节点。

3.返回新链表的头节点。

**Implement**

see solution.py

**Review**

在代码中，我们遍历了链表两次：

1.第一次遍历用来创建每个节点的拷贝，并存入哈希表。

2.第二次遍历用来赋值 next 和 random 指针。

哈希表确保了我们可以在常数时间内找到每个原节点的拷贝节点。时间复杂度为 O(n)，空间复杂度也为 O(n)，因为我们使用了哈希表来存储节点映射关系。

**Evaluate**

这个解决方案实现了深拷贝，符合题目的所有要求：

．时间复杂度为 O(n)，因为我们遍历了链表两次。

．空间复杂度为 O(n)，因为我们使用了哈希表来存储映射关系。



