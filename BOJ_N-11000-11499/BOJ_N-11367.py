def main():
    n = int(input())
    for _ in range(n):
        name, score = input().split()
        if 97 <= int(score) <= 100:
            print(name, 'A+')
        elif 90 <= int(score) <= 96:
            print(name, 'A')
        elif 87 <= int(score) <= 89:
            print(name, 'B+')
        elif 80 <= int(score) <= 86:
            print(name, 'B')
        elif 77 <= int(score) <= 79:
            print(name, 'C+')
        elif 70 <= int(score) <= 76:
            print(name, 'C')
        elif 67 <= int(score) <= 69:
            print(name, 'D+')
        elif 60 <= int(score) <= 66:
            print(name, 'D')
        else:
            print(name, 'F')


if __name__ == "__main__":
    main()
