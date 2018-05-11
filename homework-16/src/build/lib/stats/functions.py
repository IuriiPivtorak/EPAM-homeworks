"""
Statistical operations module

"""

import numpy as np
import collections
from collections import Counter
from math import floor
import matplotlib.pyplot as plt


def mean(x):
    """
    Calculates mean of object.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :returns: float -- mean of x.
    """
    if isinstance(x, collections.Iterable):
        try:
            return sum(x) / len(x)
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable with float or int values')


def median(x):
    """
    Calculates median value of object.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :returns: float -- median of x.
    """
    if isinstance(x, collections.Iterable):
        try:
            n = len(x)
            sorted_x = sorted(x)
            mid = n // 2
            if n % 2 == 1:
                return float(sorted_x[mid])
            else:
                return float((sorted_x[mid] + sorted_x[mid - 1]) / 2)
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable with float or int values')


def mode(x):
    """
    Calculates mode of object

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :returns: list -- list of most common elements of object.
    """
    if isinstance(x, collections.Iterable):
        counts = Counter(x)
        max_val = max(counts.values())
        return [k for k, count in counts.items() if count == max_val]
    else:
        raise TypeError('object should be iterable')


def quartile(x, p):
    """
    Calculates quartiles of object.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :param p: quartile you need to find.
    :type p: float.
    :returns: int or float -- element of object.
    """
    if isinstance(x, collections.Iterable):
        try:
            if 0 <= p < 1:
                p_idx = int(p * len(x))
                return sorted(x)[p_idx]
            else:
                raise ValueError('quartile value should be between 0 and 1')
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def data_range(x):
    """
    Calculates maximum distance between elements of object.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :returns: int or float -- difference between max and min elements.
    """
    if isinstance(x, collections.Iterable):
        try:
            return max(x) - min(x)
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def box_plot(x):
    """
    Plots boxplot of object.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :returns: None -- plots boxplot.
    """
    if isinstance(x, collections.Iterable):
        try:
            plt.boxplot(x)
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def variance(x):
    """
    Calculates variance of object.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :returns: float -- result of calculation.
    """
    if isinstance(x, collections.Iterable):
        try:
            m = mean(x)
            return sum([(d-m) ** 2 for d in x]) / (len(x) - 1)
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def std(x):
    """
    Calculates standard deviation of object.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :returns: float -- result of calculation.
    """
    if isinstance(x, collections.Iterable):
        try:
            return variance(x) ** 0.5
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def dot(x, y):
    """
    Calculates dot product of 2 objects.

    :param x: first object.
    :type x: list, tuple, set and any iterable object.
    :param y: second object.
    :type y: list, tuple, set and any iterable object.
    :returns: int or float -- dot product.
    """
    if isinstance(x, collections.Iterable) and isinstance(y, collections.Iterable):
        try:
            return sum([i * j for i, j in zip(x, y)])
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def covariance(x, y):
    """
    Calculates covariance of 2 objects.

    :param x: first object.
    :type x: list, tuple, set and any iterable object.
    :param y: second object.
    :type y: list, tuple, set and any iterable object.
    :returns: int of float -- covariance.
    """
    if isinstance(x, collections.Iterable) and isinstance(y, collections.Iterable):
        try:
            m_x = mean(x)
            m_y = mean(y)
            dev_x = [i - m_x for i in x]
            dev_y = [i - m_y for i in y]
            return dot(dev_x, dev_y) / (len(x)-1)
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def correlation(x, y):
    """
    Calculates correlation of 2 objects.

    :param x: first object.
    :type x: list, tuple, set and any iterable object.
    :param y: second object.
    :type y: list, tuple, set and any iterable object.
    :returns: int of float -- correlation.
    """
    if isinstance(x, collections.Iterable) and isinstance(y, collections.Iterable):
        try:
            std_x = std(x)
            std_y = std(y)
            if std_x > 0 and std_y > 0:
                return covariance(x, y) / std_x / std_y
            return 0
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def make_buckets(x, bucket_size):
    """
    Splits object in buckets.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :param bucket_size: number of buckets.
    :type bucket_size: int.
    :returns: collections.Counter class object -- buckets.
    """
    if isinstance(x, collections.Iterable):
        if isinstance(bucket_size, int) and bucket_size > 0:
            try:
                return Counter([bucket_size * floor(i / bucket_size) for i in x])
            except TypeError:
                raise TypeError('elements of object should be int or float values')
        else:
            raise ValueError('bucket size should be positive int value')
    else:
        raise TypeError('object should be iterable')


def hist(x, bucket_size, title='', xlabel='', ylabel=''):
    """
    Plots histogram of object.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :param bucket_size: number of buckets.
    :type bucket_size: int.
    :param title: name of histogram.
    :type title: str.
    :param xlabel: name of x axis.
    :type xlabel: str.
    :param ylabel: name of y axis.
    :type ylabel: str.
    :returns: None -- histogram plot.
    """
    if isinstance(x, collections.Iterable):
        try:
            hist_data = make_buckets(x, bucket_size)
            plt.bar(list(hist_data.keys()), list(hist_data.values()), width=bucket_size)
            plt.xlabel=xlabel
            plt.ylabel=ylabel
            plt.title(title)
        except TypeError:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def plot(x, y):
    """
    Function which plots line graph based on x and y as axises.

    :param x: object x
    :type x: list, tuple, set and any iterable object.
    :param y: object y
    :type y: list, tuple, set and any iterable object.
    :returns: None -- line plot.
    """
    if isinstance(x, collections.Iterable) and isinstance(y, collections.Iterable):
        if all(isinstance(x, (int, float)) for x in x) \
                and all(isinstance(y, (int, float)) for y in y):
            plt.plot(x, y)
        else:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def pdf(x):
    """
    Plots probability density function of object.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :returns: None -- pdf plot.
    """
    if isinstance(x, collections.Iterable):
        if all(isinstance(x, (int, float)) for x in x):
            histogr, bins = np.histogram(x, bins=20, range=(min(x), max(x)))
            bin_centers = (bins[1:]+bins[:-1])*0.5
            plt.plot(bin_centers, histogr)
        else:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')


def cdf(x):
    """
    Plots cumulative distribution function of object.

    :param x: object.
    :type x: list, tuple, set and any iterable object.
    :returns: None -- cdf plot.
    """
    if isinstance(x, collections.Iterable):
        if all(isinstance(x, (int, float)) for x in x):
            counts, bin_edges = np.histogram(x, bins=20)
            graph = np.cumsum(counts)
            plt.plot(bin_edges[1:], graph/graph[-1])
        else:
            raise TypeError('elements of object should be int or float values')
    else:
        raise TypeError('object should be iterable')
