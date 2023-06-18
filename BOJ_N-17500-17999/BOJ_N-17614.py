def main():
    # only Pypy3
    N = int(input())
    c = 0
    for i in range(1, N + 1):
        c += str(i).count('3') + str(i).count('6') + str(i).count('9')
    print(c)

    # for Python


if __name__ == "__main__":
    main()
