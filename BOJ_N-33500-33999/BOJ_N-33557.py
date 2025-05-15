def main():
    T = int(input())
    for _ in range(T):
        A, B = input().split()

        ans = int(A) * int(B)
        if len(A) > len(B):
            B = "1" * (len(A) - len(B)) + B
        elif len(B) > len(A):
            A = "1" * (len(B) - len(A)) + A

        ans_d = []
        for a, b in zip(A, B):
            ans_d.append(str(int(a) * int(b)))

        print(1 if ans == int("".join(ans_d)) else 0)


if __name__ == "__main__":
    main()
