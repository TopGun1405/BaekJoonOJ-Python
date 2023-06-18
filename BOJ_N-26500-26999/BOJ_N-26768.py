def main():
    litera = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
    W = list(input())
    for i in range(len(W)):
        if W[i] in litera:
            W[i] = litera[W[i]]
    print(''.join(W))


if __name__ == "__main__":
    main()
