def main():
    a = input()
    b = input()

    nums = [max(int(n1), int(n2)) for n1, n2 in zip(a, b)]
    print(*nums, sep='')


if __name__ == "__main__":
    main()
