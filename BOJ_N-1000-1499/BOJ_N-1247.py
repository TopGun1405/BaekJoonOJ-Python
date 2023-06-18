def main():
    for _ in range(3):
        N = int(input())
        tot = 0
        for _ in range(N):
            n = int(input())
            tot += n
        print("+" if tot > 0 else ("-" if tot < 0 else 0))


if __name__ == "__main__":
    main()
