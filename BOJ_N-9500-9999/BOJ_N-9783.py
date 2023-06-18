def main():
    text = input()
    eMessage = {str(i): "#{}".format(i) for i in range(10)}
    eMessage.update({chr(i): "{:02}".format(i - 96) for i in range(97, 123)})
    eMessage.update({chr(i): "{:02}".format(i - 38) for i in range(65, 91)})
    for t in text:
        print(eMessage[t], end='') if t in eMessage else print(t, end='')


if __name__ == "__main__":
    main()
