def main():
    word = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
    c = list(input())
    i = 0
    while True:
        if i == len(c):
            break
        if c[i] in word:
            c.remove(c[i])
        else:
            i += 1
    print(''.join(c))


if __name__ == "__main__":
    main()
