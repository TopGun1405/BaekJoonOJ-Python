def main():
    N = int(input())
    K = int(input())
    pos = sorted(map(int, input().split()))

    if K >= N:
        print(0)
    else:
        dis = sorted([pi - pj for pi, pj in zip(pos[1:], pos[:-1])], reverse=True)
        print(sum(dis[K-1:]))


if __name__ == "__main__":
    main()
