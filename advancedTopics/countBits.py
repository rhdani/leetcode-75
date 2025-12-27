def count_bits(n):
    baseVal = 1
    retVal = 0
    for i in range(32):
        tmp = n & baseVal
        if tmp > 0:
            retVal+=1
        baseVal = baseVal << 1
    # Replace this placeholder return statement with your code
    return retVal

# Driver code
def main():
  # The array below represents the following unsigned integers:[3, 25, 725, 2500, 3253, 2147483647]
  unsigned_integers =[0b00000000000000000000000000000011,
                      0b00000000000000000000000000011001,
                      0b00000000000000000000001011010101,
                      0b00000000000000000000100111000100,
                      0b00000000000000000000110010110101,
                      0b01111111111111111111111111111111]
  
  for i in range(len(unsigned_integers)):
    print(i+1, ".\tThe unsigned integer: ", unsigned_integers[i])
    
    one_bits = count_bits(unsigned_integers[i])
    
    binary_rep = format(unsigned_integers[i], '032b')
    print("\n\t32-bit binary representation of", unsigned_integers[i] ,": ", binary_rep)
    print("\n\tNumber of 1 bits: ", one_bits)
    print("-" * 100)

if __name__ == '__main__':
  main()

