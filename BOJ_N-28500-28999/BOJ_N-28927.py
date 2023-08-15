def main():
    t1, e1, f1 = map(int, input().split())
    t2, e2, f2 = map(int, input().split())
    ma, me = t1*3 + e1*20 + f1*120, t2*3 + e2*20 + f2*120
    if ma > me:
        print("Max")
    elif ma < me:
        print("Mel")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
