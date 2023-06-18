def main():
    N, I = map(int, input().split())
    handle = sorted([input() for _ in range(N)])
    print(handle[I - 1])


if __name__ == "__main__":
    main()
