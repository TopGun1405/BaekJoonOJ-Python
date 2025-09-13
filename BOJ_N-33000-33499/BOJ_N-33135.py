def main():
    S = input()

    t = "".join(sorted(set(S)))

    print(len(S) - len(t))


if __name__ == "__main__":
    main()
