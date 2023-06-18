def main():
    T = int(input())
    for _ in range(T):
        x1, y1, f1, x2, y2, f2 = map(int, input().split())
        print(f1 + abs(x2 - x1) + abs(y2 - y1) + f2)


if __name__ == "__main__":
    main()
