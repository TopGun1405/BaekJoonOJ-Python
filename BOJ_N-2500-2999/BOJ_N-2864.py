def main():
    A, B = map(list, input().split())
    A5, B5 = [i if i != '6' else '5' for i in A], [i if i != '6' else '5' for i in B]
    A6, B6 = [i if i != '5' else '6' for i in A], [i if i != '5' else '6' for i in B]
    print(int(''.join(A5)) + int(''.join(B5)), int(''.join(A6)) + int(''.join(B6)))


if __name__ == "__main__":
    main()
