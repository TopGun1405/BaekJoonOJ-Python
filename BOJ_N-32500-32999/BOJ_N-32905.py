def main():
    n, m = map(int, input().split())
    correct = True
    for _ in range(n):
        task = input().split()
        if task.count("A") != 1:
            correct = False

    print("Yes" if correct else "No")


if __name__ == "__main__":
    main()
