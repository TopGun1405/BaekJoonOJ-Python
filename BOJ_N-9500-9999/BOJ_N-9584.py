def main():
    sc_code = input()
    n = int(input())

    output = []
    for _ in range(n):
        code = input()
        for i in range(len(code)):
            if sc_code[i] != "*" and code[i] != sc_code[i]:
                break
        else:
            output.append(code)

    print(len(output))
    print(*output, sep="\n")


if __name__ == "__main__":
    main()
