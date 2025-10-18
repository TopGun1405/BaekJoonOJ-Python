def main():
    eye = input()

    S = eye.split("()")

    print("correct" if len(S[0]) == len(S[1]) else "fix")


if __name__ == "__main__":
    main()
