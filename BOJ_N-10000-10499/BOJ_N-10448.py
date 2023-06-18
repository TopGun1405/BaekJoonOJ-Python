def main():
    tri = [n * (n + 1) // 2 for n in range(1, 46)]
    eur = [0] * 1001

    for a in tri:
        for b in tri:
            for c in tri:
                if a + b + c <= 1000:
                    eur[a + b + c] = 1

    T = int(input())
    for _ in range(T):
        K = int(input())
        print(eur[K])


if __name__ == "__main__":
    main()
