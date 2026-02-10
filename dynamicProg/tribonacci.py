def find_tribonacci(n):

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    NMinus3 = 0
    NMinus2 = 1
    NMinus1 = 1

    for i in range(3, n+1):
        N = NMinus1 + NMinus2 + NMinus3
        NMinus1, NMinus2, NMinus3 = N, NMinus1, NMinus2
    return N

def main():
    n = [4, 5, 25, 17, 19]
    for i in range(len(n)):
        print((i + 1), ".\tThe ", (n[i]), "th Tribonacci number is:  ",
              find_tribonacci(n[i]), sep="")
        print("-"*100, "\n")


if __name__ == '__main__':
    main()
