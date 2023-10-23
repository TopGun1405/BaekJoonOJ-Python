def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    M = int(input())
    C = list(map(int, input().split()))

    qStack = list(map(lambda n: n[1], filter(lambda el: el[0] == 0, zip(A, B))))

    # queueStack = []
    # for Ai, Bi in zip(A, B):
    #     if Ai == 0:
    #         queueStack.append(Bi)

    if len(qStack) > M:
        print(*qStack[::-1][:M])
    else:
        print(*(qStack[::-1] + C[:M-len(qStack)]))


if __name__ == "__main__":
    main()
