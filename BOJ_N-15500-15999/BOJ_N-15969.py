def main():
    N = int(input())
    score = list(map(int, input().split()))
    print(max(score) - min(score))


if __name__ == "__main__":
    main()
