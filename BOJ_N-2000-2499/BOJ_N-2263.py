def main():

    def preOrder(inStart, inEnd, postStart, postEnd):
        if inStart > inEnd or postStart > postEnd:
            return

        node = postOrder[postEnd]
        leftNum = nodeNums[node] - inStart
        rightNum = inEnd - nodeNums[node]

        print(node, end=' ')
        preOrder(inStart, inStart + (leftNum - 1), postStart, postStart + (leftNum - 1))
        preOrder(inEnd - (rightNum - 1), inEnd, postEnd - rightNum, postEnd - 1)

    n = int(input())
    inOrder = list(map(int, input().split()))
    postOrder = list(map(int, input().split()))

    nodeNums = [0] * (n + 1)
    for i in range(n):
        nodeNums[inOrder[i]] = i

    preOrder(0, n - 1, 0, n - 1)


if __name__ == "__main__":
    main()
