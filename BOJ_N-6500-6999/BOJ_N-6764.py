def main():
    fish = [int(input()) for _ in range(4)]
    print("Fish At Constant Depth" if fish[3] == fish[2] == fish[1] == fish[0]
          else ("Fish Rising" if fish[3] > fish[2] > fish[1] > fish[0]
                else ("Fish Diving" if fish[3] < fish[2] < fish[1] < fish[0]
                      else "No Fish")))


if __name__ == "__main__":
    main()
