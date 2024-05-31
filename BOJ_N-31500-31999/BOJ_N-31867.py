def main():
    N = int(input())
    K = input()

    odd, even = 0, 0
    for i in range(N):
        if int(K[i]) % 2 == 1:
            odd += 1
        else:
            even += 1

    print(0 if even > odd else (1 if even < odd else -1))


if __name__ == "__main__":
    main()
