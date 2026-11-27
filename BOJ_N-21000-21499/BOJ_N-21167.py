def main():
    while True:
        try:
            R, S = map(float, input().split())
        except EOFError:
            break
        V = ((R * (S + 0.16)) / 0.067) ** 0.5
        
        print(round(V))


if __name__ == "__main__":
    main()
