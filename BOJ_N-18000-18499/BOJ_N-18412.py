def main():
    N, A, B = map(int, input().split())
    S = list(input())
    S[A-1:B] = S[A-1:B][::-1]
    print(''.join(S))


if __name__ == "__main__":
    main()
