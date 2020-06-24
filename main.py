import time
from sys import argv
import os
from prettytable import PrettyTable

from runner import Runner
from point import Point


def load_data(input_path):
    """
    Loads data from given csv
    :param input_path: path to csv file
    :return: returns data as list of Point
    """
    points = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for row in f.readlines():
            row = row.strip()
            values = row.split(' ')
            points.append(Point(values[0], values[1:]))
    return points


def run_kmeans():
    if len(argv) < 5:
        print('Not enough arguments provided. Please provide 5 arguments: K-begin, K-end,'
              ' num_iterations, path_to_input, max seeds')
        exit(1)
    k_begin = int(argv[1])
    k_end = int(argv[2])
    if k_begin >= k_end:
        print("Please choose a proper range for k values.")
        exit(1)
    num_iterations = int(argv[3])
    input_path = argv[4]
    if len(argv) == 6:
        max_seeds = int(argv[5])
    else:
        max_seeds = 10

    if k_begin <= 1 or num_iterations <= 0:
        print('Please provide correct parameters')
        exit(1)
    if not os.path.exists(input_path):
        print('Input file does not exist')
        exit(1)
    points = load_data(input_path)
    if (k_end - k_begin + 1) >= len(points):
        print('Please set K less than size of dataset')
        exit(1)

    # arrange data in chart and run tests
    details = []
    for k in range(k_begin, k_end + 1):
        test = Runner(k, num_iterations, points, max_seeds)
        details.append(test.run_test())
    chart = PrettyTable(["Seeds", "K", "Iterations", "Minimal SSE", "Mean SSE", "Maximal SSE"])
    for row in details:
        chart.add_row(row)
    print(chart)

    # runner = KMeans(k, num_iterations)
    # runner.run(points, random_seed)
    # runner.print_results()


if __name__ == '__main__':
    run_kmeans()
