def main():
    ab = input()
    A = ab.count('A')
    print('{} : {}'.format(A, len(ab) - A))


if __name__ == "__main__":
    main()
