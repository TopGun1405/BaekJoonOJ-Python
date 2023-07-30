def main():
    # more
    nA, nB = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    C = A - B
    print(len(C))
    print(*sorted(C))


if __name__ == "__main__":
    main()
