def main():
    P, Q = map(int, input().split())
    for p in range(1, P + 1):
        for q in range(1, Q + 1):
            if P % p == Q % q == 0:
                print(p, q)


if __name__ == "__main__":
    main()
