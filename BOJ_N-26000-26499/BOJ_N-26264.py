def main():
    N = int(input())
    ans = input()
    sc = ans.count("security")
    print("security!" if sc > N - sc
          else ("bigdata?" if N - sc > sc
                else "bigdata? security!"))


if __name__ == "__main__":
    main()
