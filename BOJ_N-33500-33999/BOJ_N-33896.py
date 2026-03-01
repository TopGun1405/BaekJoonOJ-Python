def main():
    n = int(input())
    students = []
    for _ in range(n):
        name, score, risk, cost = map(lambda e: int(e) if e.isdigit() else e, input().split())
        students.append([name, (score**3 // (cost * (risk + 1))), cost])

    students.sort(key=lambda k: (-k[1], k[2], k[0]))

    print(students[1][0])


if __name__ == "__main__":
    main()
