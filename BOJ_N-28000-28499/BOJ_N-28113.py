def main():
    N, A, B = map(int, input().split())
    print("Bus" if A < B else ("Subway" if A > B else "Anything"))


if __name__ == "__main__":
    main()
