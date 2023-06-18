def main():
    stud = [0 for _ in range(30)]
    for i in range(28):
        stud[int(input()) - 1] = 1

    for i in range(30):
        if not stud[i]:
            print(i + 1)


if __name__ == "__main__":
    main()
