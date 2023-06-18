def main():
    word = input()
    print(["false", "true"][word == word[::-1]])


if __name__ == "__main__":
    main()
