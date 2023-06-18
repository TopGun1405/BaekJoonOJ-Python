def main():
    while True:
        pw = input()
        if pw == "END":
            break
        print(pw[::-1])


if __name__ == "__main__":
    main()
