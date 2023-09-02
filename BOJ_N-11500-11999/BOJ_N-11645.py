def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        names = set(input() for _ in range(n))
        print(len(names))


if __name__ == "__main__":
    main()
