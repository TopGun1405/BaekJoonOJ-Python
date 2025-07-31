def main():
    N, B = map(int, input().split())
    H = sorted([int(input()) for _ in range(N)], reverse=True)

    cnt, height = 0, 0
    for H_i in H:
        if height >= B:
            print(cnt)
            break
        cnt += 1
        height += H_i


if __name__ == "__main__":
    main()
