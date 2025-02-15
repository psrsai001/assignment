class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: None | Node = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def size(self):
        temp = self.head
        s = 0
        while temp:
            s += 1
            temp = temp.next
        return s

    def insert_begining(self, x) -> None:
        temp = self.head
        new_node = Node(x)
        if temp:
            new_node.next = temp
            self.head = new_node
        else:
            self.head = new_node
        print(f"Inserted {x} in the beginning of the list")

    def insert_end(self, x) -> None:
        temp = self.head
        new_node = Node(x)
        if not temp:
            self.head = new_node
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        print(f"Inserted {x} in the end of the list")

    def middle_element(self):
        slow = fast = self.head

        # Move slow by one step and fast by two steps
        while fast and fast.next:
            if slow:
                slow = slow.next
            fast = fast.next.next

        if slow:
            print(slow.data, "is the middle element")

    def delete_val(self, x):
        temp = self.head
        prev = None
        if not temp:
            print("LL is empty")
            return
        else:
            while temp and temp.data != x:
                prev = temp
                temp = temp.next
            if not temp:
                print(f"{ x } not found")
                return
            if not prev:
                self.head = temp.next
            if prev and temp:
                prev.next = temp.next
            print(f"{x} node is deleted")

    def reverse(self):
        cur = self.head
        if not cur:
            print("LL is empty")
            return
        next = cur
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
        print("reversed")

    def __str__(self):
        temp = self.head
        res = []
        if not temp:
            return "None\n\n"
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        return " -> ".join(res) + " -> None\n\n"
