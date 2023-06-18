def main():
    S = list(input())
    U, F = S.index('U'), S[::-1].index('F')
    print('-' * U + 'U' + 'C' * (len(S) - U - F - 2) + 'F' + '-' * F)


if __name__ == "__main__":
    main()
