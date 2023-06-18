def main():
    N, M, K = map(int, input().split())
    same = 0
    if M >= K:
        same += K
    else:
        same += M
    if N - M >= N - K:
        same += N - K
    else:
        same += N - M
    print(same)


if __name__ == "__main__":
    main()
