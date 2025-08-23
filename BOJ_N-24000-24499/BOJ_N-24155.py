def main():
    n = int(input())
    s = [int(input()) for _ in range(n)]

    idx = {}
    score = sorted(s, reverse=True)
    for i in range(n):
        if score[i] not in idx:
            idx[score[i]] = i+1
        else:
            continue

    for s_i in s:
        print(idx[s_i])


if __name__ == "__main__":
    main()
