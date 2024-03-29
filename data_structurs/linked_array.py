class Node:
    def __init__(self, ele):
        self.next = None
        self.ele = ele


class LinkedList:
    def __init__(self):
        self.head = None

    def append_left(self, node):
        if self.head is None:
            self.head = node
            return

        tmp_head = self.head
        self.head = node
        self.head.next = tmp_head

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            tmp_node = self.head
            while tmp_node.next:
                tmp_node = tmp_node.next
            tmp_node.next = node

    def traverse(self):
        if self.head is None:
            print('empty list')
            return
        tmp_node = self.head
        print(tmp_node.ele)
        while tmp_node.next:
            tmp_node = tmp_node.next
            print(tmp_node.ele)


linked = LinkedList()
linked.append(Node(1))
linked.append(Node(10))
linked.append(Node(20))
linked.append(Node(30))
linked.append(Node(2))
linked.append(Node(3))
linked.append(Node(40))
linked.traverse()
print('*' * 10)
left = LinkedList()
left.append_left(Node(1))
left.append_left(Node(10))
left.append_left(Node(20))
left.append_left(Node(30))
left.append_left(Node(2))
left.append_left(Node(3))
left.append_left(Node(40))
left.traverse()

array = Array()
for i in range(11):
    array.append(i)
print(array._array)
