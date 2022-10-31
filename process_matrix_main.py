from process_matrix import process_matrix

# matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
# matrix = [[22, 33, 44, 55], [77, 88, 99, 11]]
matrix = [[1, 2, 3, 4, 5, 6]]
# matrix = []
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8]]

if __name__ == "__main__":
    averages = process_matrix(matrix)
    print('Given this matrix:')
    print(matrix)
    print('These are its averages:')
    print(averages)