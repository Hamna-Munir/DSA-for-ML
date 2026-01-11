# Doubly Linked List

## 1. Concept Explanation
A Doubly Linked List is a linear data structure where each node contains:
- Data
- A reference to the **previous node**
- A reference to the **next node**

Unlike a Singly Linked List, traversal is possible in **both forward and backward directions**, which makes certain operations more efficient.

---

## 2. Visual / Example

NULL ← [Prev | Data | Next] ⇄ [Prev | Data | Next] ⇄ [Prev | Data | Next] → NULL


Each node:
- Knows its previous node
- Knows its next node
- Allows bidirectional traversal

---

## 3. Time & Space Complexity

| Operation             | Time Complexity |
|-----------------------|-----------------|
| Access (by index)     | O(n)            |
| Insertion (head)      | O(1)            |
| Insertion (tail)      | O(1)            |
| Deletion (known node) | O(1)            |
| Traversal             | O(n)            |

**Space Complexity:**  
- O(n) for storing `n` nodes  
- Slightly more memory than singly linked lists due to extra pointers

---

## 4. Python Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("NULL")


# Example usage
dll = DoublyLinkedList()
dll.insert_at_head(3)
dll.insert_at_head(2)
dll.insert_at_head(1)
dll.traverse_forward()
```
---

## 5. Common Interview Problems

Typical interview problems include:

- Reverse a doubly linked list

- Delete a given node in O(1) time

- Convert a doubly linked list to an array

- Implement LRU Cache using a doubly linked list

- Find pairs with a given sum

These problems test memory management and pointer correctness.

---
## 6. ML Connection

Doubly linked lists inspire structures used in:

- Cache systems (e.g., LRU cache)

- Memory-efficient data access

- Graph traversal optimizations

Understanding bidirectional links helps in building efficient ML system pipelines.

---

## 7. Practice Tasks

1. Insert nodes at the tail

2. Delete a node by value

3. Traverse backward from the tail

4. Reverse a doubly linked list

5. Implement an LRU cache using a doubly linked list

---

**Author:**  
Hamna Munir
