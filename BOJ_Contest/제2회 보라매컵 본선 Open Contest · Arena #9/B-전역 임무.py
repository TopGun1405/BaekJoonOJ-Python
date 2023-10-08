def main():
    N, M, P = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(N)]
    for s_i in s:
        s_i.sort()
        for s_ij in s_i:
            if s_ij == -1:
                P *= 2
            elif s_ij <= P:
                P += s_ij
            elif s_ij > P:
                break
        else:
            continue
        break
    else:
        print(1)
        exit(0)
    print(0)


if __name__ == "__main__":
    main()
