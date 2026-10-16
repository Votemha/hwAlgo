import sys

from avlTree import AvlTree


def processCommand(tree, parts):
    command = parts[0]

    if command == "add":
        tree.add(int(parts[1]))

    elif command == "del":
        tree.delete(int(parts[1]))

    elif command == "exists":
        return "YES" if tree.exists(int(parts[1])) else "NO"

    elif command == "next":
        result = tree.nextKey(int(parts[1]))
        return str(result) if result is not None else "None"

    elif command == "prev":
        result = tree.prevKey(int(parts[1]))
        return str(result) if result is not None else "None"

    elif command == "root":
        result = tree.rootKey()
        return str(result) if result is not None else "Empty"

    elif command == "height":
        return str(tree.height())

    elif command == "print":
        keys = tree.preorder()
        return " ".join(map(str, keys)) if keys else "Empty"

    return None


def main():
    tree = AvlTree()
    commandCount = int(sys.stdin.readline())
    output = []

    for _ in range(commandCount):
        parts = sys.stdin.readline().split()
        result = processCommand(tree, parts)

        if result is not None:
            output.append(result)

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()