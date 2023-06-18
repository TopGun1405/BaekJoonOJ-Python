def main():
    A, B = map(int, input().split())
    div = str(A // B) + '.'
    A = A % B * 10
    for _ in range(1000):
        div += str(A // B)
        A = A % B * 10
    print(div)


if __name__ == "__main__":
    main()
