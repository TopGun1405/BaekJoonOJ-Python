def main():
    z = 0
    for i in range(5):
        name = input()
        if 'FBI' in name:
            print(i + 1, end=' ')
            z += 1
    if not z:
        print("HE GOT AWAY!")


if __name__ == "__main__":
    main()
