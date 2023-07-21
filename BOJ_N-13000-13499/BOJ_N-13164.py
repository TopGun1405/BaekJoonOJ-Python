def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    diff = sorted([hi - hj for hi, hj in zip(H[1:], H[:-1])], reverse=True)
    print(sum(diff[K-1:]))


if __name__ == "__main__":
    main()
