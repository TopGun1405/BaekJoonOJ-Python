def main():
    N = int(input())
    A, B, C, D = map(int, input().split())
    S = input()

    s = ""
    ing = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    for i in range(N):
        if s and s == S[i]:
            print("No")
            break
        s = S[i]
        ing[S[i]] += 1
    else:
        if S[0] != "a" or S[-1] != "a":
            print("No")
        elif ing['a'] > A or ing['b'] > B or ing['c'] > C or ing['d'] > D:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
