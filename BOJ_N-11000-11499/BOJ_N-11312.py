def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print((A // B) ** 2)


if __name__ == "__main__":
    main()
