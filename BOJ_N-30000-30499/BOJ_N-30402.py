def main():
    pixels = [input().split() for _ in range(15)]
    for row in pixels:
        if 'w' in row:
            print("chunbae")
            break
        elif 'b' in row:
            print("nabi")
            break
        elif 'g' in row:
            print("yeongcheol")
            break


if __name__ == "__main__":
    main()
