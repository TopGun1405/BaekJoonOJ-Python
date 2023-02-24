def main():
    T = int(input())
    setA = setB = setC = 0
    for _ in range(T):
        A, B, C = map(int, input().split())
        setA, setB, setC = setA+A, setB+B, setC+C
        minSet = min(setA, setB, setC)
        if minSet >= 30:
            print(minSet)
            setA, setB, setC = setA-minSet, setB-minSet, setC-minSet
        else:
            print("NO")


if __name__ == "__main__":
    main()
