def main():
    n = int(input())
    num = list(map(int, input().split()))
    k = int(input())
    sum_num = [0]
    for i in num:
        sum_num.append(sum_num[-1] + i)
    up = 0
    for i in range(len(sum_num)):
        for j in range(i, len(sum_num)):
            if sum_num[j] - sum_num[i] > k:
                up += 1
    print(up)


if __name__ == "__main__":
    main()
