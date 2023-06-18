def main():
    K, D, A = map(int, input().split('/'))
    print("hasu" if D == 0 else ("hasu" if K + A < D else "gosu"))


if __name__ == "__main__":
    main()
