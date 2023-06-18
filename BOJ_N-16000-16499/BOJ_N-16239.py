def main():
    K = int(input())
    N = int(input())
    for i in range(1, N):
        print(i)
        K -= i
    print(K)


if __name__ == "__main__":
    main()
