def main():
    s = input()
    t = input()
    print(1 if s * len(t) == t * len(s) else 0)


if __name__ == "__main__":
    main()
