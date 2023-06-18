def main():
    T = int(input())
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for _ in range(T):
        x, y = map(int, input().split())
        print("Yes" if 0 <= x <= 23 and 0 <= y <= 59 else "No", end=' ')
        if 1 <= x <= 12:
            print("Yes" if 1 <= y <= days[x] else "No")
        else:
            print("No")


if __name__ == "__main__":
    main()
