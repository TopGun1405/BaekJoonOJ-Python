def main():
    K = int(input())
    for i in range(1, K + 1):
        if 1 + i + i ** 2 == K:
            print(i)
            break


if __name__ == "__main__":
    main()
