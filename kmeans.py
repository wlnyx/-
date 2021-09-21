"""
k-means
"""
import sys
import numpy as np
import random as random


class KMeans:
    def __init__(self, dataset, k):
        self.dataset = dataset
        self.k = k
        self.center = self.start_center(dataset, k)

    @staticmethod
    def distance(p1, p2):
        """
        欧氏距离计算
        """
        temp = 0
        for i in range(len(p1)):
            temp += pow(p1[i] - p2[i], 2)
        return pow(temp, 0.5)

    @staticmethod
    def upd_center(array):
        """
        更新中心点
        """
        temp = 0
        if len(array) == 0:
            return 0
        for x in array:
            temp += x
        temp = temp / len(array)
        return list(temp)

    @staticmethod
    def start_center(dataset, k):
        """
        初始随机选取中心点
        """
        center = []
        indexes = random.sample(range(0, len(dataset)), k)
        for i in indexes:
            center.append(dataset[i])
        return center

    def cluster(self):
        """
        聚类
        """
        result = []  # 聚类结果
        for i in range(self.k):
            result.append([])
        # self.center = self.start_center(self.dataset, self.k)
        for point in self.dataset:
            min_dist = sys.maxsize
            index = -1
            for i in range(self.k):
                dist = self.distance(self.center[i], point)
                if dist < min_dist:
                    min_dist = dist
                    index = i
            result[index].append(point)
        new_center = []
        for array in result:
            new_center.append(self.upd_center(np.array(array)))
        if new_center == self.center:
            return result, self.center
        self.center = new_center
        return self.cluster()