import sys


sys.setrecursionlimit(10**9)


def main():

    def recursion(V):
        if not V:
            return

        L, M, R = [], V[0], []
        for i in range(1, len(V)):
            if V[i] > M:
                L, R = V[1:i], V[i:]
                break
        else:
            L = V[1:]

        recursion(L)
        recursion(R)
        print(M)

    nodes = []
    while True:
        try:
            v = int(input())
            nodes.append(v)
        except EOFError:
            recursion(nodes)
            break



if __name__ == "__main__":
    main()
