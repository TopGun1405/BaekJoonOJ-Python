def main():
    N, K = map(int, input().split())
    fruit = sorted(map(int, input().split()))
    for f in fruit:
        if f <= K:
            K += 1
        else:
            break
    print(K)


if __name__ == "__main__":
    main()
