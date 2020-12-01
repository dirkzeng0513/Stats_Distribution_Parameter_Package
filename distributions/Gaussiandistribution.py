import math
import matplotlib.pyplot as plt
from .Generaldistributions import Distribution

class Gaussian(Distribution):
    """
    Gaussian distribution class for distribution parameters

    :arg:
        mean ( float )
        stdev ( float )
        data_list
    """

    def __init__(self):
        Distribution.__init__(self, mu, sigma)

    def calculate_mean(self):
        avg = 1.0 * sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean

    def calculate_stdev(self, sample = True):
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.mean

        sigma = 0

        for d in self.data:
            sigma += (d - mean) ** 2

        sigma = math.sqrt(sigma/n)

        self.stdev = sigma

        return self.stdev

    def __add__(self, other):

        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)

        return result

    def __repr__(self):
        """
        Args: None
        :return: Parameters of a Gaussian distribution
        """
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)



