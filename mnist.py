import csv
from kmeans import *
from img import *


def main():
    f = open(r'data/Sample.csv', 'r')
    reader = csv.reader(f)
    dataset = []
    file_path1 = 'cluster1'
    file_path2 = 'cluster2'
    file_path3 = 'cluster3'
    for row in reader:
        row = [int(x) for x in row]
        dataset.append(row)
    result, center = KMeans(dataset, 3).cluster()
    for i in range(200):
        packimg(result[0][i], i, file_path1)
        packimg(result[1][i], i, file_path2)
        packimg(result[2][i], i, file_path3)


if __name__ == '__main__':
    main()
