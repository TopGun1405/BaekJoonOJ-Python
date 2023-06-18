def main():
    T = int(input())
    for _ in range(T):
        act = input()
        print(len(act[:act.index('D')]) if 'D' in act else len(act))


if __name__ == "__main__":
    main()
