def main():
    # a, b, c, d = map(int, input().split())
    abcd = sorted(map(int, input().split()))
    print(sum(abcd) - abcd[0] + 1)


if __name__ == "__main__":
    main()
