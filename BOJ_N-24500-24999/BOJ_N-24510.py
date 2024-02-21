def main():
    C = int(input())

    maxLoop = 0
    for _ in range(C):
        loop = input()
        maxLoop = max(maxLoop, loop.count("for") + loop.count("while"))

    print(maxLoop)


if __name__ == "__main__":
    main()
