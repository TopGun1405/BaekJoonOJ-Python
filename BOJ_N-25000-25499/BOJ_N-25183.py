def main():
    N = int(input())
    S = input()

    cnt = 1
    for i in range(N-1):
        if abs(ord(S[i]) - ord(S[i+1])) == 1:
            cnt += 1
        else:
            cnt = 1

        if cnt == 5:
            print("YES")
            break
    else:
        print("NO")


if __name__ == "__main__":
    main()
