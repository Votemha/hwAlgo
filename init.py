import sys

class AvlNode:
    __slots__ = ("key", "left", "right", "height")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AvlTree:
    def __init__(self):
        self.root = None

    def nodeHeight(self, node):
        return node.height if node is not None else 0

    def updateHeight(self, node):
        node.height = 1 + max(self.nodeHeight(node.left), self.nodeHeight(node.right))

    def balanceFactor(self, node):
        return self.nodeHeight(node.right) - self.nodeHeight(node.left)

    def rotateLeft(self, node):
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        self.updateHeight(node)
        self.updateHeight(newRoot)
        return newRoot

    def rotateRight(self, node):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        self.updateHeight(node)
        self.updateHeight(newRoot)
        return newRoot

    def rebalance(self, node):
        self.updateHeight(node)
        balance = self.balanceFactor(node)

        if balance == 2:
            if self.balanceFactor(node.right) < 0:
                node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        if balance == -2:
            if self.balanceFactor(node.left) > 0:
                node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        return node

    def insertNode(self, node, key):
        if node is None:
            return AvlNode(key)

        if key < node.key:
            node.left = self.insertNode(node.left, key)
        elif key > node.key:
            node.right = self.insertNode(node.right, key)
        else:
            return node

        return self.rebalance(node)

    def deleteNode(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self.deleteNode(node.left, key)
        elif key > node.key:
            node.right = self.deleteNode(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = node.right
            while successor.left is not None:
                successor = successor.left

            node.key = successor.key
            node.right = self.deleteNode(node.right, successor.key)

        return self.rebalance(node)

    def add(self, key):
        self.root = self.insertNode(self.root, key)

    def delete(self, key):
        self.root = self.deleteNode(self.root, key)

    def exists(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def nextKey(self, key):
        node = self.root
        result = None
        while node is not None:
            if node.key >= key:
                result = node.key
                node = node.left
            else:
                node = node.right
        return result

    def prevKey(self, key):
        node = self.root
        result = None
        while node is not None:
            if node.key <= key:
                result = node.key
                node = node.right
            else:
                node = node.left
        return result

    def rootKey(self):
        return self.root.key if self.root is not None else None

    def height(self):
        return self.nodeHeight(self.root)

    def preorder(self):
        if self.root is None:
            return "Empty"

        keys = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            keys.append(str(node.key))
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return " ".join(keys)

def main():
    inputData = sys.stdin.buffer
    commandCount = int(inputData.readline())
    tree = AvlTree()
    output = []

    for _ in range(commandCount):
        parts = inputData.readline().split()
        command = parts[0]

        if command == b"add":
            tree.add(int(parts[1]))
        elif command == b"del":
            tree.delete(int(parts[1]))
        elif command == b"exists":
            output.append("YES" if tree.exists(int(parts[1])) else "NO")
        elif command == b"next":
            result = tree.nextKey(int(parts[1]))
            output.append(str(result) if result is not None else "None")
        elif command == b"prev":
            result = tree.prevKey(int(parts[1]))
            output.append(str(result) if result is not None else "None")
        elif command == b"root":
            result = tree.rootKey()
            output.append(str(result) if result is not None else "Empty")
        elif command == b"height":
            output.append(str(tree.height()))
        elif command == b"print":
            output.append(tree.preorder())

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()