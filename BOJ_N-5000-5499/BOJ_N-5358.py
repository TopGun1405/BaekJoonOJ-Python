def main():
    while True:
        try:
            name = list(input())
            change = {'i': 'e', 'e': 'i', 'I': 'E', 'E': 'I'}
            for i in range(len(name)):
                if name[i] in change:
                    name[i] = change[name[i]]
            print(''.join(name))
        except EOFError:
            break


if __name__ == "__main__":
    main()
