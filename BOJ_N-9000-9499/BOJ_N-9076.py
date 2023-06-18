def main():
    T = int(input())
    for _ in range(T):
        N = sorted(map(int, input().split()))
        print("KIN" if N[3] - N[1] >= 4 else N[1] + N[2] + N[3])


if __name__ == "__main__":
    main()
