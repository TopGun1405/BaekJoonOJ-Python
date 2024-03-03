def main():
    S = input()
    if S[0] == S[-1] == '"':
        S = S[1:-1]
        print(S if S else "CE")
    else:
        print("CE")


if __name__ == "__main__":
    main()
