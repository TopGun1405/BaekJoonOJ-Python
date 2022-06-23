def main():
    T = int(input())

    # A : 300s, B : 60s, C : 10s
    # 300A + 60B + 10C = T
    A, B, C = 0, 0, 0
    if T >= 300:
        A = T // 300
        T = T - 300 * A
    if 60 <= T < 300:
        B = T // 60
        T = T - 60 * B
    if 10 <= T < 60:
        C = T // 10
        T = T - 10 * C

    print("{} {} {}".format(A, B, C) if T == 0 else -1)


if __name__ == "__main__":
    main()
