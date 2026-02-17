def main():
    N, K = map(int, input().split())
    S = input().split("1")

    for s in S:
        if len(s) >= K:
            print(0)
            break
    else:
        print(1)


if __name__ == "__main__":
    main()
