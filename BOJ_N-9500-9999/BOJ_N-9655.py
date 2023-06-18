def main():
    N = int(input())
    # rock = [-1, 1, 0, 1] + [-1] * 997
    # for i in range(4, N + 1):
    #     if rock[i - 1] == 1 or rock[i - 3]:
    #         rock[i] = 0
    #     else:
    #         rock[i] = 1
    # print("CY" if rock[N] == 0 else "SK")
    print("CY" if N % 2 == 0 else "SK")


if __name__ == "__main__":
    main()
