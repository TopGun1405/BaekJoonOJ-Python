def main():
    N = int(input())
    absented = []
    for _ in range(N):
        name = input()
        if name == "Present!":
            absented.pop()
        else:
            absented.append(name)
    print("\n".join(absented) if absented else "No Absences")


if __name__ == "__main__":
    main()
