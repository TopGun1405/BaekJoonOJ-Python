def main():
    N = int(input())
    A = list(map(int, input().split()))
    U, D = map(int, input().split())

    ans = ["A"] * N
    for i in range(N):
        if A[i] == 1:
            if U == 0:
                print("NO")
                break
            ans[i] = "U"
            U -= 1
        elif A[i] == 2:
            if D == 0:
                print("NO")
                break
            ans[i] = "D"
            D -= 1
        else:
            ans[i] = " "

    else:
        for i in range(N):
            if ans[i] != " ":
                continue
            if U:
                ans[i] = "U"
                U -= 1
            elif D:
                ans[i] = "D"
                D -= 1
        print("YES")
        print("".join(ans))


if __name__ == "__main__":
    main()
