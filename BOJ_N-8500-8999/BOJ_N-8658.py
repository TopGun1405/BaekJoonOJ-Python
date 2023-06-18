def main():
    n = int(input())
    for p in range(2, n):
        if n % p:
            for q in range(n - 1, 1, -1):
                if n % q:
                    print(p, q)
                    break
            break


if __name__ == "__main__":
    main()
