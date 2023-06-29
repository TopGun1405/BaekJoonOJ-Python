def main():
    N = sorted(input(), reverse=True)
    if '0' not in N:
        print(-1)
    else:
        tot = sum(map(int, N))
        if tot % 3 != 0:
            print(-1)
        else:
            print(''.join(N))


if __name__ == "__main__":
    main()
