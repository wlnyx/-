import csv
from kmeans import *
from show import *


def main():
    f = open(r'data/test.csv', 'r')
    reader = csv.reader(f)
    dataset = []
    for row in reader:
        row = [int(x) for x in row]
        dataset.append(row)
    result, center = KMeans(dataset, 2).cluster()
    show(dataset, center, result)


if __name__ == '__main__':
    main()
