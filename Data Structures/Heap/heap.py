

class Heap:
    def __init__(self, heapArr=[], size=0):
        self.heapArr = heapArr
        self.size = size

    def buildHeap(self):  # MAX HEAP
        print("BUILDING HEAP")
        for i in range((self.size//2)-1,  -1, -1):
            self.heapify(i)

    def heapify(self, i):
        # check if larger than children
        leftChild = 2*i+1
        rightChild = 2*i+2
        largest = i
        if leftChild < len(self.heapArr) and self.heapArr[leftChild] > self.heapArr[largest]:
            largest = leftChild
        if rightChild < len(self.heapArr) and self.heapArr[rightChild] > self.heapArr[largest]:
            largest = rightChild
        if largest != i:
            self.heapArr[i], self.heapArr[largest] = self.heapArr[largest], self.heapArr[i]
            self.heapify(largest)

    def print(self):
        for i in self.heapArr:
            print(i, end=" ")


def main():
    arr = [4, 7, 1, 2, 12, 4, 8, 9, 3]
    maxHeap = Heap(arr, len(arr))
    maxHeap.print()
    maxHeap.buildHeap()
    maxHeap.print()


if __name__ == '__main__':
    main()
