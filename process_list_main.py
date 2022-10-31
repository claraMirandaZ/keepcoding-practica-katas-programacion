from process_list import process_list

numbers = [2, 4, 6, 1, 2, 3]

if __name__ == "__main__":
    averages = process_list(numbers)
    print(numbers)
    print('Averages:')
    print(averages)

    # for i in range(15):
    #     averages = process_list(averages)
    #     print(averages)