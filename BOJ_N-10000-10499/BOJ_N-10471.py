def main():
    W, P = map(int, input().split())
    L = [0] + list(map(int, input().split())) + [W]

    partition = []
    for i in range(P+1):
        for j in range(i+1, P+2):
            partition.append(L[j] - L[i])

    print(*sorted(set(partition)))


if __name__ == "__main__":
    main()
