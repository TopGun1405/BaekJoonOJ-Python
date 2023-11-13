def main():
    N = int(input())
    A = list(map(int, input().split()))
    student = {}
    for Ai in A:
        if student.get(Ai, 0):
            if student[Ai] == 1:
                student[Ai] += 1
        else:
            student.update({Ai: 1})
    print(sum(student.values()))


if __name__ == "__main__":
    main()
