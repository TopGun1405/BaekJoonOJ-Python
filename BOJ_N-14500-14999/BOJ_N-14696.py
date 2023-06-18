def main():
    N = int(input())

    for _ in range(N):
        A = input().split()[1:]
        B = input().split()[1:]

        for s in ['4', '3', '2', '1']:
            if A.count(s) > B.count(s):
                print('A')
                break
            elif A.count(s) < B.count(s):
                print('B')
                break
            if s == '1':
                print('D')


if __name__ == "__main__":
    main()
