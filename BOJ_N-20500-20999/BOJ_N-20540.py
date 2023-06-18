def main():
    mbti = input()
    m = {'I': 'E', 'E': 'I', 'N': 'S', 'S': 'N',
         'F': 'T', 'T': 'F', 'P': 'J', 'J': 'P'}
    for s in mbti:
        print(m[s], end='')


if __name__ == "__main__":
    main()
