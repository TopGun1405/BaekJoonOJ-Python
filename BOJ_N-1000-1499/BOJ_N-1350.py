def main():
    N = int(input())
    files = list(map(int, input().split()))
    cluster = int(input())

    result = 0
    for i in files:
        result += i // cluster + (1 if i % cluster > 0 else 0)

    print(cluster * result)


if __name__ == "__main__":
    main()
