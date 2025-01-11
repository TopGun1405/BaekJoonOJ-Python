def main():
    N = int(input())
    pasta = set(input().split())
    used = set(input().split())

    print(*(pasta - used))


if __name__ == "__main__":
    main()
