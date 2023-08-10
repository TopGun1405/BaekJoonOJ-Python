def main():
    n = int(input())
    frame = 0
    for _ in range(n):
        hi, wi = map(int, input().split())
        frame = max(frame, hi * wi)
    print(frame)


if __name__ == "__main__":
    main()
