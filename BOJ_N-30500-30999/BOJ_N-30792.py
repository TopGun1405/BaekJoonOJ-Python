def main():
    n = int(input())
    support = int(input())
    unsupported = sorted(map(int, input().split()), reverse=True)

    for rank, vote in enumerate(unsupported):
        if vote < support:
            print(rank + 1)
            break
    else:
        print(1 if support > unsupported[0] else n)


if __name__ == "__main__":
    main()
