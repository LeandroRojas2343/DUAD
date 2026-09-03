class Node:
    def __init__(self, value):
        self.value = value


class DoubleEndedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_left(self, value):
        new = Node(value)
        new.next = self.head
        new.prev = None

        if self.head is None:
            # the deque was empty: new is both head and tail
            self.tail = new
        else:
            # link from the old head back to the new node
            self.head.prev = new

        # in any case, new becomes the new head
        self.head = new
        self.size += 1

    def push_right(self, value):
        new = Node(value)
        new.prev = self.tail
        new.next = None

        if self.tail is None:
            # the deque was empty: new is both head and tail
            self.head = new
            self.tail = new
        else:
            # link from the old tail forward to the new node
            self.tail.next = new
            self.tail = new

        self.size += 1

    def pop_left(self):
        if self.head is None:
            raise IndexError("pop_left from empty deque")

        node = self.head
        value = node.value

        if node.next is None:
            # there was only one element
            self.head = None
            self.tail = None
        else:
            # there are more elements: update head and disconnect links
            self.head = node.next
            self.head.prev = None
            node.next = None

        self.size -= 1
        return value

    def pop_right(self):
        if self.tail is None:
            raise IndexError("pop_right from empty deque")

        node = self.tail
        value = node.value

        if node.prev is None:
            # there was only one element
            self.head = None
            self.tail = None
        else:
            # there are more elements: update tail and disconnect links
            self.tail = node.prev
            self.tail.next = None
            node.prev = None

        self.size -= 1
        return value

    def print_deque(self):
        current = self.head
        if current is None:
            print("Empty deque")
            return

        output = str(current.value)
        current = current.next
        while current is not None:
            output += " <- " + str(current.value)
            current = current.next
        print(output)


def main():
    dq = DoubleEndedQueue()
    dq.push_right("A")
    dq.push_right("B")
    dq.push_left("C")
    dq.print_deque()
    print("pop_left ->", dq.pop_left())
    print("pop_right ->", dq.pop_right())
    dq.print_deque()
    print("size:", dq.size)


main()

