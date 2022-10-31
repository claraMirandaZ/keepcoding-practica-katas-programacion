from process_matrix import process_matrix

matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

if __name__ == "__main__":
    averages = process_matrix(matrix)
    print(matrix)
    print('Averages:')
    print(averages)