def main():
    N = list(map(int, input().split()))
    print("Good" if N == sorted(N) else "Bad")


if __name__ == "__main__":
    main()
