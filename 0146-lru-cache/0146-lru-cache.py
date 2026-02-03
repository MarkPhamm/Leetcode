class Node: 
    def __init__(self, key = 0, val =0):
        self.next = None
        self.prev = None 
        self.key = key
        self.val = val
class LRUCache:
    def _add_to_front(self, node):
        # Head <-> A <-> Tail 
        # Head <-> X <-> A <-> Tail 
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


    def _delete_node(self, node):
        # Head <-> X <-> A <-> Tail 
        # Head <-> X <-> Tail 
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None 
        node.prev = None

    def _move_to_front(self, node):
        self._delete_node(node)
        self._add_to_front(node) 

    def _remove_last(self):
        node = self.tail.prev
        self._delete_node(node)
        return node

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail 
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.val
        return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        else: 
            if len(self.cache) >= self.cap:
                last = self._remove_last()
                del(self.cache[last.key])
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node) 

            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)