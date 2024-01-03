def main():
    N = int(input())
    extensions = {}
    for _ in range(N):
        fileName = input()
        ext = fileName.split(".")[1]
        try:
            extensions[ext] += 1
        except KeyError:
            extensions[ext] = 1

    for name, cnt in sorted(extensions.items(), key=lambda k: k[0]):
        print(name, cnt)


if __name__ == "__main__":
    main()
