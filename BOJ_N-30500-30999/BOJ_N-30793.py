def main():
    px, rx = map(int, input().split())

    vx = px / rx
    if vx < 0.2:
        print("weak")
    elif 0.2 <= vx < 0.4:
        print("normal")
    elif 0.4 <= vx < 0.6:
        print("strong")
    else:
        print("very strong")


if __name__ == "__main__":
    main()
