def main():
    N = int(input())
    student = list(map(int, input().split()))
    print(*list(filter(lambda k: student.count(k) == 1, student)))


if __name__ == "__main__":
    main()
