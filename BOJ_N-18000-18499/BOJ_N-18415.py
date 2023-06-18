def main():
    N = int(input())
    S = list(input())
    for i in range(N):
        if ''.join(S[i:i+3]) == "joi":
            S[i:i+3] = ['J', 'O', 'I']
    print(''.join(S))


if __name__ == "__main__":
    main()
