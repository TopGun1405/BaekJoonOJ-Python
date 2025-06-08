def main():
    l1, r1, l2, r2, k = map(int, input().split())

    L, R = max(l1, l2), min(r1, r2)
    
    print((R - L + 1) - R // k + (L - 1) // k if R >= L else 0)


if __name__ == "__main__":
    main()
