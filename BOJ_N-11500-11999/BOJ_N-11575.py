def main():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        s = input()
        A = ord("A")
        print("".join([chr(A + ((ord(c) - A) * a + b) % 26) for c in s]))


if __name__ == "__main__":
    main()
