def main():
    N = int(input())
    S = list(input())
    for i in range(N-1):
        if S[i:i+2] == ['j', 'j']:
            S[i:i+2] = ['J', 'J']
        elif S[i:i+2] == ['o', 'o']:
            S[i:i+2] = ['O', 'O']
        elif S[i:i+2] == ['i', 'i']:
            S[i:i+2] = ['I', 'I']
    print(''.join(S))


if __name__ == "__main__":
    main()
