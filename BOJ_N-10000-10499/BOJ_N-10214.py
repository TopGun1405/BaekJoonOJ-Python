def main():
    T = int(input())
    for _ in range(T):
        y, k = 0, 0
        for _ in range(9):
            Y, K = map(int, input().split())
            y += Y
            k += K
        print("Yonsei" if y > k else ("Korea" if y < k else "Draw"))


if __name__ == "__main__":
    main()
