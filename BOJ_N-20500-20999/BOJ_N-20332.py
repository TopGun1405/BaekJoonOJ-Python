def main():
    n = int(input())
    w = list(map(int, input().split()))
    print("no" if sum(w) % 3 else "yes")


if __name__ == "__main__":
    main()
