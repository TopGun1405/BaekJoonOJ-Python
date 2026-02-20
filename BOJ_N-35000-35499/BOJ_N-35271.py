def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ar, st = [0] * (M + 1), [0] * N
    for i in range(N):
        f, s, t = map(int, input().split())
        if ar[f] < A[f-1]:
            ar[f] += 1
            st[i] = f

        elif ar[s] < A[s-1]:
            ar[s] += 1
            st[i] = s

        elif ar[t] < A[t-1]:
            ar[t] += 1
            st[i] = t

        else:
            st[i] = -1

    print(*st)


if __name__ == "__main__":
    main()
