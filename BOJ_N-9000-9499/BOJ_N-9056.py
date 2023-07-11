def main():
    T = int(input())
    for _ in range(T):
        A, B = map(set, input().split())
        print("YES" if len(A) == len(B) and A & B == A else "NO")


if __name__ == "__main__":
    main()
