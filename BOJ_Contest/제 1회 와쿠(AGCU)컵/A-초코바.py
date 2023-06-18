def main():
    N, M = map(int, input().split())
    print(["No", "Yes"][N * 100 >= M])


if __name__ == "__main__":
    main()
