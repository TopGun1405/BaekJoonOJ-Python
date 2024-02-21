def main():
    while True:
        S = input()
        if S == "*":
            break
        S = list(map(lambda c: c[0].lower(), S.split()))
        print("Y" if len(set(S)) == 1 else "N")


if __name__ == "__main__":
    main()
