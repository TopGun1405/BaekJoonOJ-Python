def main():
    N = int(input())
    nodes = [3**n for n in range(14, -1, -1)]
    for _ in range(N):
        K = int(input())
        val = []
        for node in list(filter(lambda e: e <= K, nodes)):
            if node <= K:
                val.append(K // node)
                K = K % node
            else:
                val.append(0)
        print(*val)


if __name__ == "__main__":
    main()
