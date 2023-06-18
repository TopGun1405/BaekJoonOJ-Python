def main():
    N = list(map(int, input()))
    # N.sort(reverse=True)
    # print(*N, sep='')

    print(*sorted(map(int, input()))[::-1], sep='')


if __name__ == "__main__":
    main()
