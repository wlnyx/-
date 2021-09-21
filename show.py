"""
仿真数据绘图
"""
from matplotlib import pyplot as plt


def show(dataset, center, result):
    for i in range(len(result[0])):
        plt.scatter(result[0][i][0], result[0][i][1], c='green')
    for i in range(len(result[1])):
        plt.scatter(result[1][i][0], result[1][i][1], c='blue')
    plt.show()
