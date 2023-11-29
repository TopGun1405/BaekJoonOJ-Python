def main():
    N, Q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(Q):
        l, r = map(int, input().split())
        a_lr = a[l-1:r]
        delta = sum(map(lambda n: abs(n[1] - n[0]), zip(a_lr[:-1], a_lr[1:])))
        print(delta)


if __name__ == "__main__":
    main()
