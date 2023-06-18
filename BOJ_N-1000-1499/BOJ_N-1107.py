def main():
    N = int(input())
    M = int(input())
    if M == 0:
        print(0 if N == 100 else min(abs(N - 100), len(str(N))))
    else:
        broken = set(map(int, input().split()))
        unbroken = set(range(10)) - broken


if __name__ == "__main__":
    main()
