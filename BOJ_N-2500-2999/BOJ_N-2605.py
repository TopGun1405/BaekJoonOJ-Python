def main():
    students = []
    N = int(input())
    n = list(map(int, input().split()))
    for i in range(N):
        students.insert(n[i], i + 1)
    print(*students[::-1])


if __name__ == "__main__":
    main()
