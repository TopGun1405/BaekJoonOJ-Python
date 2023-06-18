def main():
    T = int(input())
    for _ in range(T):
        A = sorted(map(int, input().split()))
        print(A[-3])


if __name__ == "__main__":
    main()
