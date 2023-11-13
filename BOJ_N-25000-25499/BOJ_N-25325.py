def main():
    n = int(input())

    students = {name: 0 for name in input().split()}
    for _ in range(n):
        info = input().split()
        for name in info:
            students[name] += 1

    students = sorted(students.items(), key=lambda k: (-k[1], k[0]))
    for student in students:
        print(*student)


if __name__ == "__main__":
    main()
