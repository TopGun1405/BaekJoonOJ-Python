def main():
    N, M = map(int, input().split())
    h = map(int, input().split())
    a = map(int, input().split())
    print(max(h) + max(a))


if __name__ == "__main__":
    main()
