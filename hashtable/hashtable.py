class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_head(self, node):
        node.next = self.head
        self.head = node
    
    def find(self, key):
        curr = self.head
        while curr != None:
            if curr.key == key:
                return curr
            else:
                curr = curr.next
        return curr
    
    def remove(self, key):
        curr = self.head
        if curr.key == key:
            self.head = curr.next
            curr.next = None
        prev = curr
        while curr != None:
            if curr.key == key:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next
        return None

    def add_to_head_or_overwrite(self, node):
        eNode = self.find(node.key)
        if eNode != None:
            eNode.value = node.value
        else:
            self.add_to_head(node)

                

        
# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    
    def __init__(self, capacity):
        # Your code here
        if capacity < MIN_CAPACITY:
          return
        self.capacity = capacity
        self.list = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.list)
        
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        i = 0
        count = 0
        while i < len(self.list):
            if self.list[i] != None:
                curr = self.list[i].head
                while curr != None:
                    count = count + 1
                    curr = curr.next
            i = i + 1
        return count / len(self.list)
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hash = 14695981039346656037
        key = key.encode()
        for a in key:
          hash = hash ^ a
          hash = hash * 1099511628211
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        ll = LinkedList()
        hash_key = self.hash_index(key)
        if self.list[hash_key] == None:
            self.list[hash_key] = ll
            self.list[hash_key].add_to_head(HashTableEntry(key, value))
        else:
            return self.list[hash_key].add_to_head_or_overwrite(HashTableEntry(key, value))
        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)
        # Your code here


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hash_key = self.hash_index(key)
        if self.list[hash_key]:
          self.list[hash_key].remove(key)
        else:
          print('Key not found')
        if self.get_load_factor() < .2:
            if self.capacity != MIN_CAPACITY:
                self.resize(self.capacity // 2)
        # Your code here


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash_key = self.hash_index(key)
        if self.list[hash_key] != None:
            if self.list[hash_key].find(key) != None:
                return self.list[hash_key].find(key).value
        else:
            return None
        # Your code here


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        newlist = [None] * new_capacity
        oldList = self.list
        self.list = newlist
        self.capacity = new_capacity
        i = 0
        while i < len(oldList):
            if oldList[i] != None:
                curr = oldList[i].head
                while curr != None:
                    self.put(curr.key, curr.value)
                    curr = curr.next
            i = i + 1



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
