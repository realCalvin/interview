class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        temp = Node()
        if self.head == None:  # insert first element
            temp.val = data
            self.head = temp
            self.tail = temp
            self.head.next = self.tail
        else:  # insert at end of linked list
            temp.val = data
            self.tail.next = temp
            self.tail = temp

    def remove(self, data):
        temp = self.head
        if self.head.val == data:
            self.head = self.head.next
        else:
            while temp:
                if temp.next.val == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next

    def printList(self):
        temp = self.head

        while temp:
            print(temp.val, end=" ")
            temp = temp.next


def main():
    l = LinkedList()
    l.insert(7)
    l.insert(3)
    l.insert(2)
    l.insert(5)
    l.remove(2)
    l.printList()


if __name__ == "__main__":
    main()
