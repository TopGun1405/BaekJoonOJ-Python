def main():
    n = int(input())
    a = list(map(int, input().split()))
    front = a.count(0)
    back = n - front
    print([front, back][front > back])


if __name__ == "__main__":
    main()
