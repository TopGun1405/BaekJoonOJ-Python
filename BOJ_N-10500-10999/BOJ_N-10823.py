def main():
    S = ''
    while True:
        try:
            S += input()
        except EOFError:
            break
    print(sum(map(int, S.split(','))))


if __name__ == "__main__":
    main()
