def main():
    text = input()
    rotLetters = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
    for c in text:
        if c not in rotLetters:
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    main()
