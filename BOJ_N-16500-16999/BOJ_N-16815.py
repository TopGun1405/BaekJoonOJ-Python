def main():
    S = input()

    left = S[:S.index("*")]
    
    print(left.count("(") - left.count(")"))


if __name__ == "__main__":
    main()
