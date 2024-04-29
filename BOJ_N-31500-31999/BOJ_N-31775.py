def main():
    s1 = input()
    s2 = input()
    s3 = input()

    s = sorted([s1[0], s2[0], s3[0]])
    print("GLOBAL" if s == ["k", "l", "p"] else "PONIX")


if __name__ == "__main__":
    main()
