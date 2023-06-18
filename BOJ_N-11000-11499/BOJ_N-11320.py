def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(int(round((A * A * (3 ** 0.5)) / (B * B * (3 ** 0.5)))))


if __name__ == "__main__":
    main()
