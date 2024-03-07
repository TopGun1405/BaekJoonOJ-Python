def main():
    T = int(input())
    for t in range(T):
        B = int(input())
        bit = input().replace("O", "0").replace("I", "1")

        msg = [chr(int(bit[i*8:i*8+8], 2)) for i in range(B)]
        print(f"Case #{t + 1}: {''.join(msg)}")


if __name__ == "__main__":
    main()
