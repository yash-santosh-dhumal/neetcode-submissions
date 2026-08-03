class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)      # Dummy head
        self.tail = Node(0, 0)      # Dummy tail

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the linked list
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert node before tail (Most Recently Used)
    def add(self, node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.add(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]

            node.value = value

            self.remove(node)
            self.add(node)

        else:
            if len(self.cache) == self.capacity:
                lru = self.head.next

                self.remove(lru)
                del self.cache[lru.key]

            node = Node(key, value)

            self.cache[key] = node
            self.add(node)