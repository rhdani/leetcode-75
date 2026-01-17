def print_matrix(matrix):
    for row in matrix:
        print(row)

def rotate_image(matrix):

    n = len(matrix)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix

# Driver code
def main():

    inputs = [[[1]], [[6, 9], [2, 7]], [[2, 14, 8], [12, 7, 14], [3, 3, 7]],
              [[3, 1, 1, 7], [15, 12, 13, 13], [4, 14, 12, 4], [10, 5, 11, 12]],
              [[10, 1, 14, 11, 14], [13, 4, 8, 2, 13], [10, 19, 1, 6, 8], [20, 10, 8, 2, 12], [15, 6, 8, 8, 18]]]

    for i in range(len(inputs)):

      print(i + 1, ".\tMatrix:", sep = "")
      print_matrix(inputs[i])

      print("\n\tRotated matrix:", sep = "")
      print_matrix(rotate_image(inputs[i]))

      print("-" * 100)

if __name__ == "__main__":
    main()
