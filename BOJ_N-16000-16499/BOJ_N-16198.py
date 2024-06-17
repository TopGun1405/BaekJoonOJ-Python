def main():

    def gather_energy(energy):
        if len(W) == 2:
            res['MAX'] = max(energy, res['MAX'])
            return
        for i in range(1, len(W)-1):
            W_i = W.pop(i)
            gather_energy(energy + W[i-1] * W[i])
            W.insert(i, W_i)

    N = int(input())
    W = list(map(int, input().split()))

    res = {'MAX': 0}
    gather_energy(0)

    print(res['MAX'])


if __name__ == "__main__":
    main()
