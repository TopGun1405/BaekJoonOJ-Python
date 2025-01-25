def main():
    N = int(input())
    basis_JH = input()
    key_JH = input()
    basis_I = input()
    key_I = input()

    key = ""
    for i in range(N):
        if basis_JH[i] == basis_I[i]:
            if key_JH[i] == key_I[i]:
                key += key_JH[i]
            else:
                print("htg!")
                break
    else:
        print(key)


if __name__ == "__main__":
    main()
