def main():
    n = int(input())
    a, b = [], []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    print("yes" if a == sorted(a) and b == sorted(b) else "no")


if __name__ == "__main__":
    main()
