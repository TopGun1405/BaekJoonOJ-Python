def main():
    text = ''
    while True:
        s = input()
        if s == '':
            break
        text += s
    text = text.replace(' ', '')

    alp = [0 for _ in range(26)]
    for i in text:
        alp[ord(i) - 97] += 1

    m = max(alp)
    for i in range(26):
        if alp[i] == m:
            print(chr(97 + i), end='')


if __name__ == "__main__":
    main()
