def main():
    S = input()
    suffix = sorted([S[i:] for i in range(len(S))])
    print(*suffix, sep='\n')


if __name__ == "__main__":
    main()
