class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = self.left

        self.parent = None
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self


class InOrderIterator:
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False
        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        pass

    def __iter__(self):
        pass





if __name__ == "__main__":
    node = Node(2,
                Node(1),
                Node(3))
