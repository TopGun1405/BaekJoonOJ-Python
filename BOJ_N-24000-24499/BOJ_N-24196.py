def main():
    msg = input()
    i = 0
    while i < len(msg):
        print(msg[i], end='')
        i += ord(msg[i]) - 64


if __name__ == "__main__":
    main()
