def main():
    N = int(input())
    S = input()
    print(S[:N-1] if S[-1] == 'G' else S + 'G')


if __name__ == "__main__":
    main()
