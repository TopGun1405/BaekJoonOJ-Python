def main():
    N = int(input())
    M = input()
    K = int(input())

    if '1' not in M or K == 0:
        print("YES")
    else:
        cnt = 0
        for m in M[::-1]:
            if m == '1':
                break
            elif m == '0':
                cnt += 1
        print("YES" if cnt >= K else "NO")


if __name__ == "__main__":
    main()
