def main():
    N = int(input())
    for i in range(N):
        print('* ' * (N - N // 2))
        print(' *' * (N // 2))


if __name__ == "__main__":
    main()
