def main():
    lamb = int(input())
    if 620 <= lamb <= 780:
        print("Red")
    elif 590 <= lamb < 620:
        print("Orange")
    elif 570 <= lamb < 590:
        print("Yellow")
    elif 495 <= lamb < 570:
        print("Green")
    elif 450 <= lamb < 495:
        print("Blue")
    elif 425 <= lamb < 450:
        print("Indigo")
    elif 380 <= lamb < 425:
        print("Violet")


if __name__ == "__main__":
    main()
