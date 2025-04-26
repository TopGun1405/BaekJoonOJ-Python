def main():
    f, f_r = [0] * 10, [0] * 10
    n = list(map(int, input().split()))
    for i in range(10):
        f[i], f_r[n[i]] = n[i], i

    fA, fB = input().split()

    a = "".join(str(f_r[int(c)]) for c in fA)
    b = "".join(str(f_r[int(c)]) for c in fB)

    print("".join(str(f[int(c)]) for c in str(int(a) + int(b))))


if __name__ == "__main__":
    main()
