def main():
    # https://velog.io/@learningssik/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-10986-%ED%8C%8C%EC%9D%B4%EC%8D%AC
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    group = [0] * M
    tot = 0

    for i in range(N):
        tot += A[i]
        group[tot % M] += 1

    count = group[0]
    for n in group:
        count += n * (n - 1) // 2
    print(count)


if __name__ == "__main__":
    main()
