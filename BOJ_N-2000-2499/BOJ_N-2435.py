def main():
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    nums = [sum(D[i:i+K]) for i in range(N-K+1)]
    print(max(nums))


if __name__ == "__main__":
    main()
