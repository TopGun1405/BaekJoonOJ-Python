def main():
    n = int(input())
    p, q, r, s = map(int, input().split())
    a_1 = int(input())

    a_n = [0] * (n + 1)
    for i in range(1, n+1):
        if i == 1:
            a_n[i] = a_1
            continue

        if i % 2 == 0:
            a_n[i] = p * a_n[i//2] + q
        else:
            a_n[i] = r * a_n[i//2] + s

    print(sum(a_n))


if __name__ == "__main__":
    main()
