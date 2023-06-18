def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    s = []
    merge_sort(a, s, 0, len(a) - 1)
    print(s[K - 1] if K <= len(s) else -1)


def merge_sort(a: list, s: list, p: int, r: int) -> None:
    if p < r:
        q = (p + r) // 2
        merge_sort(a, s, p, q)
        merge_sort(a, s, q + 1, r)
        merge(a, s, p, q, r)


def merge(a: list, s: list, p: int, q: int, r: int) -> None:
    tmp = [0] * (r - p + 1)

    i, j, t = p, q+1, 0
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp[t] = a[i]
            s.append(tmp[t])
            t, i = t+1, i+1
        else:
            tmp[t] = a[j]
            s.append(tmp[t])
            t, j = t+1, j+1

    while i <= q:
        tmp[t] = a[i]
        s.append(tmp[t])
        t, i = t+1, i+1

    while j <= r:
        tmp[t] = a[j]
        s.append(tmp[t])
        t, j = t+1, j+1

    i, t = p, 0
    while i <= r:
        a[i] = tmp[t]
        i, t = i+1, t+1


if __name__ == "__main__":
    main()
