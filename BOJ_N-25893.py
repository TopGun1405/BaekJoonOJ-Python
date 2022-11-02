def main():
    n = int(input())
    for _ in range(n):
        s1, s2, s3 = map(int, input().split())
        print(s1, s2, s3)
        if s1 >= 10 and s2 >= 10 and s3 >= 10:
            print("triple-double")
        elif (s1 >= 10 and s2 >= 10) or (s2 >= 10 and s3 >= 10) or (s3 >= 10 and s1 >= 10):
            print("double-double")
        elif s1 >= 10 or s2 >= 10 or s3 >= 10:
            print("double")
        else:
            print("zilch")
        if _ != n - 1:
            print()


if __name__ == "__main__":
    main()
