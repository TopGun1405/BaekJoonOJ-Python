def main():
    n, k, T_0 = map(int, input().split())
    d = [0] + list(map(int, input().split()))

    T = [T_0] + [0] * n
    for i in range(n):
        if T[i] > k:
            T[i+1] = T[i] + d[i+1] - abs(T[i] - k)

        elif T[i-1] < k:
            T[i+1] = T[i] + d[i+1] + abs(T[i] - k)

        else:
            T[i+1] = T[i] + d[i+1]

    print(sum([abs(T_n - k) for T_n in T[1:]]))


if __name__ == "__main__":
    main()
