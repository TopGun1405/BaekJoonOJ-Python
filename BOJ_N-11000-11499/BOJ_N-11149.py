def main():
    code = {chr(n): n - 97 for n in range(97, 123)}
    code[' '] = 26
    code_rev = {val: key for key, val in code.items()}

    T = int(input())
    for _ in range(T):
        msg = input().split()

        decode = []
        for s in msg:
            val = 0
            for c in s:
                val += code[c]
            decode.append(code_rev[val % 27])

        print("".join(decode))


if __name__ == "__main__":
    main()
