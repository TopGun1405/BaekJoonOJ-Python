def main():
    N = list(map(lambda n : n ** 2, map(int, input().split())))
    print(sum(N) % 10)


if __name__ == "__main__":
    main()
