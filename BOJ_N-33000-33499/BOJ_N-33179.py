def main():
    n = int(input())
    pages = list(map(lambda e: int(e) + (1 if int(e) % 2 == 1 else 0), input().split()))
    print(sum(pages) // 2)


if __name__ == "__main__":
    main()
