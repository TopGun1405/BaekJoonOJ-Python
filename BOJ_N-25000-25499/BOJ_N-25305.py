def main():
    N, k = map(int, input().split())
    score = sorted(map(int, input().split()), reverse=True)
    print(score[k - 1])


if __name__ == "__main__":
    main()
