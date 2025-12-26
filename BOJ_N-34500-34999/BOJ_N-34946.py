def main():
    A, B, C, D = map(int, input().split())

    shuttle, walk = A + B, C
    if shuttle <= D and walk <= D:
        print("~.~")
    elif not shuttle <= D and not walk <= D:
        print("T.T")
    elif shuttle <= D and not walk <= D:
        print("Shuttle")
    elif not shuttle <= D and walk <= D:
        print("Walk")


if __name__ == "__main__":
    main()
