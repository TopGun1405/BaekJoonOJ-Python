def main():
    N = int(input())
    cute = 0
    for _ in range(N):
        c = int(input())
        if c == 1:
            cute += 1
    print("Junhee is cute!" if cute > N // 2 else "Junhee is not cute!")


if __name__ == "__main__":
    main()
