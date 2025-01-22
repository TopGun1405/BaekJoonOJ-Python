def main():
    AA, BB, CCCC = map(int, input().split("/"))

    if AA > 12:
        print("EU")
    elif BB > 12:
        print("US")
    else:
        print("either")


if __name__ == "__main__":
    main()
