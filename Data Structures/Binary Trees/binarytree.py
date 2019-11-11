
import queue


class Node:
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node()
        if self.head == None:
            node.val = data
            self.head = node
        else:
            temp = self.head
            node = Node()
            while temp:
                if data == temp.val:
                    print("Value already exists.")
                    break
                elif data > temp.val:
                    # insert
                    if temp.right == None:
                        node.val = data
                        temp.right = node
                        break
                    else:
                        temp = temp.right
                elif data < temp.val:
                    # insert
                    if temp.left == None:
                        node.val = data
                        temp.left = node
                        break
                    else:
                        temp = temp.left

    def print(self):
        q = queue.Queue()
        q.put(self.head)
        values = []
        while not q.empty():
            temp = q.get()
            if temp:
                values.append(temp.val)
            else:
                values.append("null")
            if temp:
                q.put(temp.left)
                q.put(temp.right)
        print(values)


def main():
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(4)
    bt.insert(3)
    bt.insert(2)
    bt.insert(6)
    bt.insert(99)
    bt.print()


if __name__ == '__main__':
    main()
