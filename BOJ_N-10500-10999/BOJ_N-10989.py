def main():
    N = int(input())

    ##############
    # solution 1 #
    ##############

    # num = [int(input()) for _ in range(N)]
    # counting_sort(num)
    # print(*num, sep='\n')

    ##############
    # solution 2 #
    ##############

    counting_sort_v2()


def counting_sort(s):
    count = [0] * (max(s) + 1)

    for i in s:
        count[i] = count[i] + 1

    s.clear()
    for i in range(len(count)):
        if i != 0:
            for j in range(count[i]):
                s.append(i)


def counting_sort_v2():
    count = [0] * 10_001
    max_i = 0
    for _ in range(N):
        n = int(input())
        if max_i < n:
            max_i = n
        count[n] += 1
    count = count[:max_i + 1]
    for i in range(len(count)):
        if count[i] == 0:
            continue
        else:
            for j in range(count[i]):
                print(i)


if __name__ == "__main__":
    main()
