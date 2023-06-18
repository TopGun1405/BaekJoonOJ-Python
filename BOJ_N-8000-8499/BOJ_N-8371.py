def main():
    n = int(input())
    text1 = input()
    text2 = input()
    incorrect = 0
    for i in range(n):
        if text2[i] != text1[i]:
            incorrect += 1
    print(incorrect)


if __name__ == "__main__":
    main()
