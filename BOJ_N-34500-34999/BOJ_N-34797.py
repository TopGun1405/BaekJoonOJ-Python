def main():
    g = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}
    w = {'1': 0.05, '2': 0.025, '3': 0}

    n = int(input())
    gpa, bonus = 0, 0
    for _ in range(n):
        tier = input()
        gpa += g[tier[0]]
        if g[tier[0]] > 1:
            bonus += w[tier[1]]

    print(gpa / n + bonus)


if __name__ == "__main__":
    main()
