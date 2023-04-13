def main():

    def preOrder(node):
        if node != '.':
            print(node, end='')
            preOrder(bTree[node][0])
            preOrder(bTree[node][1])

    def inOrder(node):
        if node != '.':
            inOrder(bTree[node][0])
            print(node, end='')
            inOrder(bTree[node][1])

    def postOrder(node):
        if node != '.':
            postOrder(bTree[node][0])
            postOrder(bTree[node][1])
            print(node, end='')

    N = int(input())
    bTree = dict()
    for _ in range(N):
        root, left, right = input().split()
        bTree.update({root: [left, right]})

    preOrder('A')
    print()
    inOrder('A')
    print()
    postOrder('A')


if __name__ == "__main__":
    main()
