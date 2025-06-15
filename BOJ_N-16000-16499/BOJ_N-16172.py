def main():
    S = input()
    K = input()

    for n in range(10):
        S = S.replace(str(n), "")

    print(1 if K in S else 0)


if __name__ == "__main__":
    main()
