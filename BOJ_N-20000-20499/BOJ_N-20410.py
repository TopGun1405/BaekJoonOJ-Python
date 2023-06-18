def main():
    m, Seed, X1, X2 = map(int, input().split())
    for a in range(m + 1):
        for c in range(m + 1):
            if (a * Seed + c) % m == X1:
                if (a * X1 + c) % m == X2:
                    print(a, c)
                    break
        else:
            continue
        break


if __name__ == "__main__":
    main()
