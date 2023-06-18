def main():
    while True:
        try:
            s, t = map(list, input().split())

            print("Yes" if s in t else "No")
        except:
            break


if __name__ == "__main__":
    main()
