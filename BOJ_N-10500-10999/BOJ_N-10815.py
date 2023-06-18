def main():
    N = int(input())
    num = list(map(int, input().split()))
    M = int(input())
    find = list(map(int, input().split()))

    num.sort()
    for e in find:
        founded = binary_search(num, e)
        if founded == -1:
            print(0, end=' ')
        else:
            print(1, end=' ')

    ###################
    # better solution #
    ###################

    # N = int(input())
    # num = set(input().split())
    # M = int(input())
    # find = input().split()
    # check = [0] * M
    #
    # for i in range(M):
    #     if find[i] in num:
    #         check[i] = 1
    #
    # print(*check, sep=' ')


def binary_search(s, key):
    length = len(s)
    low = 0
    high = length - 1
    location = -1

    while low <= high and location == -1:
        mid = round((low + high) / 2)
        if key == s[mid]:
            location = mid
        elif key < s[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return location


if __name__ == "__main__":
    main()
