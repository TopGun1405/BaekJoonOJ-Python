def main():
    N, M = map(int, input().split())
    point = [0] + list(map(int, input().split()))
    p = {i: point[i] for i in range(1, N + 1)}
    student = []
    for i in range(M):
        score = input().split()
        student.append([int(score[0]), 0])
        for j in range(1, N + 1):
            if score[j] == 'O':
                student[i][1] += p[j]
    student.sort(key=lambda k: (k[1], -k[0]), reverse=True)
    print(student[0][0], student[0][1])


if __name__ == "__main__":
    main()
