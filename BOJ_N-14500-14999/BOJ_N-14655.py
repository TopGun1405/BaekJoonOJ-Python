def main():
    N = int(input())
    C1 = list(map(lambda e: abs(int(e)), input().split()))
    C2 = list(map(lambda e: abs(int(e)), input().split()))
    print(sum(C1) + sum(C2))


if __name__ == "__main__":
    main()
