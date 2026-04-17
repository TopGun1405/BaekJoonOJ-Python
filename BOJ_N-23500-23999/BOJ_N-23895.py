def main():
    T = int(input())
    for x in range(1, T+1):
        N, B = map(int, input().split())
        A = sorted(map(int, input().split()))

        cnt = 0
        for A_i in A:
            if B - A_i < 0:
                break
            B -= A_i
            cnt += 1

        print(f"Case #{x}: {cnt}")


if __name__ == "__main__":
    main()
