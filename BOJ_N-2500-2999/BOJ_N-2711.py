def main():
    T = int(input())
    for _ in range(T):
        i, text = input().split()
        text = list(text)
        del text[int(i) - 1]
        print(''.join(text))


if __name__ == "__main__":
    main()
