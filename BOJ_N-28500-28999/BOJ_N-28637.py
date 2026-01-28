def main():
    n = int(input())
    for _ in range(n):
        s = input()

        tmp, snake_case = "", []
        for i in range(len(s)):
            if s[i].isupper():
                if i == 0:
                    tmp += s[i].lower()
                    continue
                else:
                    snake_case.append(tmp)
                    tmp = s[i].lower()
            else:
                tmp += s[i]
        snake_case.append(tmp)

        print("_".join(snake_case))


if __name__ == "__main__":
    main()
